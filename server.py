#!/usr/bin/env python3
import asyncio, json, uuid, time, random
import websockets
from typing import Dict, List, Optional

PORT = 8765
LOBBY: Dict[str, "Room"] = {}        # room_id -> Room
CLIENTS: Dict[any, "Player"] = {}    # websocket -> Player

# ---------- data classes ----------
class Player:
    def __init__(self, ws, name: str, role: str):
        self.ws = ws
        self.name = name
        self.role = role          # "player" | "judge"
        self.roastbucks = 0
        self.powerups = {p:0 for p in ["extra_burn","mic_drop","taxes","reverse_roast",
                                       "silent_mode","judges_favor","savage_mode"]}
        self.skip_turns = 0
        self.earned_this_round = 0

class Room:
    def __init__(self, rid: str, mode: str):
        self.id = rid
        self.mode = mode               # "1v1nj" | "1v1" | "2v2" | "3v3" | "4v4"
        self.players: List[Player] = []
        self.judges: List[Player] = []
        self.bracket = []              # player names in current bracket order
        self.current_match: Optional[tuple] = None   # (p1, p2)
        self.timer_task = None
        self.votes = {}                # judge_name -> winner_name
        self.stage = 1
        self.time_limit = 90           # seconds per round
        self.round_earning_multiplier = 1

    # util
    def broadcast(self, msg):
        for p in self.players + self.judges:
            asyncio.create_task(p.ws.send(json.dumps(msg)))

    def player_count_needed(self) -> int:
        return int(self.mode.split("v")[0]) * 2          # "2v2" -> 4

    def judge_count_needed(self) -> int:
        return 0 if self.mode == "1v1nj" else 1

    def full(self) -> bool:
        return (len(self.players) == self.player_count_needed() and
                len(self.judges)  == self.judge_count_needed())

    # bracket logic
    def start_next(self):
        if len(self.bracket) <= 1:
            self.broadcast({"type":"game_over","winner":self.bracket[0]})
            return
        self.current_match = (self.bracket[0], self.bracket[1])
        self.votes.clear()
        self.broadcast({"type":"new_match","match":self.current_match})
        self.timer_task = asyncio.create_task(self.round_timer())

    async def round_timer(self):
        await asyncio.sleep(self.time_limit)
        self.broadcast({"type":"times_up"})
        await asyncio.sleep(5)   # grace
        self.resolve_match()

    def resolve_match(self):
        # auto-vote for no-judge rooms
        if self.mode == "1v1nj":
            winner = random.choice([self.current_match[0], self.current_match[1]])
            self.votes["server"] = winner

        if not self.votes: return
        tally = {}
        for v in self.votes.values():
            tally[v] = tally.get(v,0)+1
        winner = max(tally, key=tally.get)
        loser  = self.current_match[0] if self.current_match[1]==winner else self.current_match[1]

        # rewards
        for p in self.players:
            if p.name == winner:
                p.roastbucks += 5 * self.stage
                p.earned_this_round += 5 * self.stage
            elif p.name == loser:
                pass
        self.bracket = [n for n in self.bracket if n != loser]
        self.stage += 1
        self.broadcast({"type":"bracket","bracket":self.bracket})
        self.start_next()

# ---------- websocket handler ----------
async def handler(ws, path):
    room_id = path.strip("/")
    # first message must be join_request
    raw = await ws.recv()
    msg = json.loads(raw)
    if msg["type"] != "join_request":
        await ws.close()
        return

    mode = msg["mode"]
    name = msg["name"]

    # create room if needed
    if room_id not in LOBBY:
        LOBBY[room_id] = Room(room_id, mode)
    room = LOBBY[room_id]

    # role decision
    role = "player"
    if room.mode == "1v1nj":
        # no judges ever
        role = "player"
    else:
        # fill judges first, then players
        if len(room.judges) < room.judge_count_needed():
            role = "judge"
        else:
            role = "player"

    # refuse if full
    if (role == "player" and len(room.players) >= room.player_count_needed()) or \
       (role == "judge"  and len(room.judges)  >= room.judge_count_needed()):
        await ws.send(json.dumps({"type":"err","msg":"Room full"}))
        await ws.close()
        return

    # accept
    p = Player(ws, name, role)
    CLIENTS[ws] = p
    if role == "player":
        room.players.append(p)
        room.bracket.append(name)
    else:
        room.judges.append(p)

    # send lobby state
    room.broadcast({"type":"lobby","mode":room.mode,
                    "players":[pl.name for pl in room.players],
                    "judges":[j.name for j in room.judges]})

    # start first match if ready
    if room.full() and room.current_match is None:
        room.start_next()

    # message loop
    try:
        async for raw in ws:
            msg = json.loads(raw)
            if msg["type"] == "chat":
                p.earned_this_round += 1
                p.roastbucks += 1
                room.broadcast({"type":"chat","from":p.name,"text":msg["text"]})

            elif msg["type"] == "vote":
                if p.role == "judge":
                    room.votes[p.name] = msg["winner"]

            elif msg["type"] == "buy_powerup":
                prices = {"extra_burn":50,"mic_drop":30,"taxes":120,"reverse_roast":45,
                          "silent_mode":10,"judges_favor":50,"savage_mode":750}
                pu = msg["powerup"]
                if pu in prices and p.roastbucks >= prices[pu]:
                    p.roastbucks -= prices[pu]
                    p.powerups[pu] += 1
                    await ws.send(json.dumps({"type":"bought","powerup":pu,"bucks":p.roastbucks}))

    finally:
        # cleanup on disconnect
        if p in room.players: room.players.remove(p)
        if p in room.judges:  room.judges.remove(p)
        if p.name in room.bracket: room.bracket.remove(p.name)
        del CLIENTS[ws]
        room.broadcast({"type":"lobby","mode":room.mode,
                        "players":[pl.name for pl in room.players],
                        "judges":[j.name for j in room.judges]})
        if not room.players and not room.judges:
            del LOBBY[room_id]

# ---------- run ----------
start_server = websockets.serve(handler, "0.0.0.0", PORT)
asyncio.get_event_loop().run_until_complete(start_server)
print(f"Smokeout server listening on :{PORT}")
asyncio.get_event_loop().run_forever()
