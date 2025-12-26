import asyncio, json, uuid, time, random
import websockets
from typing import Dict, List

PORT = 8765
LOBBY = {}          # key = room_id, value = Room()
CLIENTS = {}        # key = websocket, value = Player

class Player:
    def __init__(self, ws, name, role):
        self.ws = ws
        self.name = name
        self.role = role          # "player" or "judge"
        self.roastbucks = 0
        self.powerups = {p:0 for p in ["extra_burn","mic_drop","taxes","reverse_roast",
                                       "silent_mode","judges_favor","savage_mode"]}
        self.skip_turns = 0
        self.earned_this_round = 0   # temp counter

class Room:
    def __init__(self, rid):
        self.id = rid
        self.players: List[Player] = []
        self.judges: List[Player] = []
        self.bracket = []          # list of player names in order
        self.current_match = ()    # tuple (p1_name, p2_name)
        self.timer_task = None
        self.votes = {}            # judge_name -> winner_name
        self.round_earning_multiplier = 1
        self.time_limit = 90       # seconds
        self.stage = 1             # increases each round

    def broadcast(self, msg):
        for p in self.players + self.judges:
            asyncio.create_task(p.ws.send(json.dumps(msg)))

    async def start_timer(self):
        await asyncio.sleep(self.time_limit)
        self.broadcast({"type":"times_up"})
        await asyncio.sleep(5)     # grace to vote
        self.resolve_match()

    def resolve_match(self):
        if not self.votes: return
        tally = {}
        for v in self.votes.values():
            tally[v] = tally.get(v,0)+1
        winner = max(tally, key=tally.get)
        loser  = self.current_match[0] if self.current_match[1]==winner else self.current_match[1]
        # rewards
        for p in self.players:
            if p.name == winner:
                p.roastbucks += 5*self.stage
                p.earned_this_round += 5*self.stage
            elif p.name == loser:
                pass
        # advance bracket
        self.bracket = [n for n in self.bracket if n!=loser]
        self.broadcast({"type":"bracket","bracket":self.bracket})
        self.next_match()

    def next_match(self):
        if len(self.bracket) <= 1:
            self.broadcast({"type":"game_over","winner":self.bracket[0]})
            return
        self.current_match = (self.bracket[0], self.bracket[1])
        self.votes.clear()
        self.stage += 1
        self.broadcast({"type":"new_match","match":self.current_match})

async def handler(ws, path):
    room_id = path.strip("/")
    if room_id not in LOBBY:
        LOBBY[room_id] = Room(room_id)
    room = LOBBY[room_id]
    await ws.send(json.dumps({"type":"join_form"}))
    async for raw:
        msg = json.loads(raw)
        if msg["type"] == "join":
            role = msg["role"]
            name = msg["name"]
            p = Player(ws, name, role)
            CLIENTS[ws] = p
            if role=="player":
                room.players.append(p)
                room.bracket.append(name)
            else:
                room.judges.append(p)
            room.broadcast({"type":"lobby","players":[p.name for p in room.players],
                            "judges":[j.name for j in room.judges]})
            if len(room.players)>=2 and len(room.judges)>=1 and room.current_match==():
                room.next_match()
                room.timer_task = asyncio.create_task(room.start_timer())

        elif msg["type"] == "chat":
            p = CLIENTS[ws]
            p.roastbucks += 1
            p.earned_this_round += 1
            room.broadcast({"type":"chat","from":p.name,"text":msg["text"]})

        elif msg["type"] == "buy_powerup":
            p = CLIENTS[ws]
            pu = msg["powerup"]
            prices = {"extra_burn":50,"mic_drop":30,"taxes":120,"reverse_roast":45,
                      "silent_mode":10,"judges_favor":50,"savage_mode":750}
            if p.roastbucks >= prices[pu]:
                p.roastbucks -= prices[pu]
                p.powerups[pu] += 1
                await ws.send(json.dumps({"type":"bought","powerup":pu,"bucks":p.roastbucks}))

        elif msg["type"] == "vote":
            judge = CLIENTS[ws]
            room.votes[judge.name] = msg["winner"]

        elif msg["type"] == "use_powerup":
            # quick stub – expand as needed
            pass

start_server = websockets.serve(handler, "0.0.0.0", PORT)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
