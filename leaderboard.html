<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Leaderboard - Smokeout</title>
    
    <!-- External Libraries -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/animejs/3.2.1/anime.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/typed.js/2.0.12/typed.min.js"></script>
    <script src="https://unpkg.com/splitting@1.0.6/dist/splitting.js"></script>
    <link rel="stylesheet" href="https://unpkg.com/splitting@1.0.6/dist/splitting.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/echarts/5.4.0/echarts.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.4.0/p5.min.js"></script>
    
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Roboto+Mono:wght@300;400;700&family=Inter:wght@300;400;500;600;700&family=Russo+One&display=swap" rel="stylesheet">
    
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Inter', sans-serif;
            background: #1a1a1a;
            color: #f5f5f5;
            overflow-x: hidden;
            min-height: 100vh;
        }

        /* Navigation */
        .navbar {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            background: rgba(26, 26, 26, 0.95);
            backdrop-filter: blur(10px);
            padding: 1rem 2rem;
            z-index: 1000;
            border-bottom: 2px solid #ff6b35;
        }

        .nav-content {
            display: flex;
            justify-content: space-between;
            align-items: center;
            max-width: 1200px;
            margin: 0 auto;
        }

        .logo {
            font-family: 'Orbitron', monospace;
            font-size: 1.5rem;
            font-weight: 900;
            color: #ff6b35;
            text-shadow: 0 0 10px rgba(255, 107, 53, 0.5);
        }

        .nav-links {
            display: flex;
            gap: 2rem;
            list-style: none;
        }

        .nav-links a {
            color: #f5f5f5;
            text-decoration: none;
            font-weight: 500;
            transition: color 0.3s ease;
            position: relative;
        }

        .nav-links a:hover {
            color: #ff6b35;
        }

        .nav-links a::after {
            content: '';
            position: absolute;
            bottom: -5px;
            left: 0;
            width: 0;
            height: 2px;
            background: #ff6b35;
            transition: width 0.3s ease;
        }

        .nav-links a:hover::after {
            width: 100%;
        }

        /* Main Content */
        .main-content {
            margin-top: 80px;
            padding: 2rem;
            max-width: 1200px;
            margin-left: auto;
            margin-right: auto;
        }

        /* Header */
        .page-header {
            text-align: center;
            margin-bottom: 3rem;
        }

        .page-title {
            font-family: 'Orbitron', monospace;
            font-size: clamp(2.5rem, 6vw, 4rem);
            font-weight: 900;
            margin-bottom: 1rem;
            background: linear-gradient(45deg, #ff6b35, #00d4ff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .page-subtitle {
            font-size: 1.2rem;
            color: #999;
            max-width: 600px;
            margin: 0 auto;
        }

        /* Category Tabs */
        .category-tabs {
            display: flex;
            justify-content: center;
            margin-bottom: 3rem;
            gap: 1rem;
            flex-wrap: wrap;
        }

        .tab-button {
            background: rgba(26, 26, 26, 0.8);
            border: 2px solid #333;
            color: #f5f5f5;
            padding: 1rem 2rem;
            border-radius: 25px;
            cursor: pointer;
            transition: all 0.3s ease;
            font-weight: 600;
            font-family: 'Inter', sans-serif;
        }

        .tab-button:hover {
            border-color: #ff6b35;
            background: rgba(255, 107, 53, 0.1);
        }

        .tab-button.active {
            border-color: #ff6b35;
            background: linear-gradient(45deg, #ff6b35, #ff8c42);
            color: white;
        }

        /* Stats Overview */
        .stats-overview {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 2rem;
            margin-bottom: 3rem;
        }

        .stat-card {
            background: rgba(26, 26, 26, 0.8);
            border: 2px solid #333;
            border-radius: 15px;
            padding: 2rem;
            text-align: center;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }

        .stat-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255, 107, 53, 0.1), transparent);
            transition: left 0.5s ease;
        }

        .stat-card:hover::before {
            left: 100%;
        }

        .stat-card:hover {
            border-color: #ff6b35;
            transform: translateY(-5px);
            box-shadow: 0 10px 30px rgba(255, 107, 53, 0.2);
        }

        .stat-icon {
            font-size: 3rem;
            margin-bottom: 1rem;
            display: block;
        }

        .stat-value {
            font-family: 'Orbitron', monospace;
            font-size: 2.5rem;
            font-weight: 900;
            color: #ff6b35;
            margin-bottom: 0.5rem;
        }

        .stat-label {
            font-size: 1.1rem;
            color: #999;
            margin-bottom: 1rem;
        }

        .stat-change {
            font-size: 0.9rem;
            padding: 0.3rem 0.8rem;
            border-radius: 15px;
            font-weight: 600;
        }

        .stat-change.positive {
            background: rgba(0, 255, 136, 0.2);
            color: #00ff88;
        }

        .stat-change.negative {
            background: rgba(255, 7, 58, 0.2);
            color: #ff073a;
        }

        /* Leaderboard Table */
        .leaderboard-container {
            background: rgba(26, 26, 26, 0.8);
            border: 2px solid #333;
            border-radius: 20px;
            overflow: hidden;
            margin-bottom: 3rem;
        }

        .leaderboard-header {
            background: linear-gradient(45deg, #ff6b35, #ff8c42);
            padding: 2rem;
            text-align: center;
        }

        .leaderboard-title {
            font-family: 'Orbitron', monospace;
            font-size: 2rem;
            font-weight: 700;
            color: white;
            margin-bottom: 0.5rem;
        }

        .leaderboard-subtitle {
            color: rgba(255, 255, 255, 0.8);
            font-size: 1rem;
        }

        .search-bar {
            padding: 1.5rem 2rem;
            background: rgba(0, 0, 0, 0.3);
            border-bottom: 1px solid #333;
        }

        .search-input {
            width: 100%;
            max-width: 400px;
            background: rgba(0, 0, 0, 0.5);
            border: 2px solid #333;
            color: #f5f5f5;
            padding: 1rem;
            border-radius: 25px;
            font-size: 1rem;
            margin: 0 auto;
            display: block;
            transition: border-color 0.3s ease;
        }

        .search-input:focus {
            outline: none;
            border-color: #ff6b35;
            box-shadow: 0 0 10px rgba(255, 107, 53, 0.3);
        }

        .leaderboard-table {
            width: 100%;
            border-collapse: collapse;
        }

        .leaderboard-table th {
            background: rgba(0, 0, 0, 0.5);
            color: #ff6b35;
            font-family: 'Orbitron', monospace;
            font-weight: 700;
            padding: 1.5rem 1rem;
            text-align: left;
            border-bottom: 2px solid #333;
        }

        .leaderboard-table td {
            padding: 1.5rem 1rem;
            border-bottom: 1px solid #333;
            transition: background 0.3s ease;
        }

        .leaderboard-table tr:hover td {
            background: rgba(255, 107, 53, 0.05);
        }

        .rank-cell {
            font-family: 'Orbitron', monospace;
            font-weight: 700;
            font-size: 1.2rem;
            color: #ff6b35;
        }

        .rank-cell.top-3 {
            font-size: 1.5rem;
        }

        .rank-1 { color: #ffd700; }
        .rank-2 { color: #c0c0c0; }
        .rank-3 { color: #cd7f32; }

        .player-cell {
            display: flex;
            align-items: center;
            gap: 1rem;
        }

        .player-avatar {
            width: 50px;
            height: 50px;
            border-radius: 50%;
            background: linear-gradient(45deg, #ff6b35, #00d4ff);
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 700;
            color: white;
            font-size: 1.2rem;
        }

        .player-info {
            flex: 1;
        }

        .player-name {
            font-weight: 600;
            font-size: 1.1rem;
            color: #f5f5f5;
            margin-bottom: 0.2rem;
        }

        .player-level {
            font-size: 0.9rem;
            color: #999;
        }

        .stats-cell {
            text-align: center;
        }

        .stats-cell .value {
            font-family: 'Orbitron', monospace;
            font-weight: 700;
            font-size: 1.1rem;
            color: #00d4ff;
            display: block;
            margin-bottom: 0.2rem;
        }

        .stats-cell .label {
            font-size: 0.8rem;
            color: #999;
        }

        .achievement-cell {
            display: flex;
            gap: 0.5rem;
            flex-wrap: wrap;
        }

        .achievement-badge {
            background: rgba(255, 107, 53, 0.2);
            border: 1px solid #ff6b35;
            color: #ff6b35;
            padding: 0.3rem 0.6rem;
            border-radius: 12px;
            font-size: 0.8rem;
            font-weight: 600;
        }

        /* Chart Container */
        .chart-container {
            background: rgba(26, 26, 26, 0.8);
            border: 2px solid #333;
            border-radius: 20px;
            padding: 2rem;
            margin-bottom: 3rem;
        }

        .chart-title {
            font-family: 'Orbitron', monospace;
            font-size: 1.5rem;
            font-weight: 700;
            color: #00d4ff;
            margin-bottom: 2rem;
            text-align: center;
        }

        .chart {
            width: 100%;
            height: 400px;
        }

        /* Personal Stats */
        .personal-stats {
            background: rgba(0, 212, 255, 0.1);
            border: 2px solid #00d4ff;
            border-radius: 20px;
            padding: 2rem;
            margin-bottom: 3rem;
        }

        .personal-stats h3 {
            font-family: 'Orbitron', monospace;
            font-size: 1.5rem;
            font-weight: 700;
            color: #00d4ff;
            margin-bottom: 2rem;
            text-align: center;
        }

        .personal-stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1.5rem;
        }

        .personal-stat-item {
            background: rgba(0, 0, 0, 0.3);
            padding: 1.5rem;
            border-radius: 10px;
            text-align: center;
        }

        .personal-stat-value {
            font-family: 'Orbitron', monospace;
            font-size: 1.8rem;
            font-weight: 700;
            color: #00d4ff;
            margin-bottom: 0.5rem;
        }

        .personal-stat-label {
            color: #999;
            font-size: 0.9rem;
        }

        /* Footer */
        .footer {
            background: rgba(26, 26, 26, 0.9);
            border-top: 2px solid #333;
            padding: 2rem;
            text-align: center;
            margin-top: 4rem;
        }

        .footer p {
            color: #666;
            font-size: 0.9rem;
        }

        /* Responsive Design */
        @media (max-width: 768px) {
            .nav-links {
                display: none;
            }
            
            .category-tabs {
                gap: 0.5rem;
            }
            
            .tab-button {
                padding: 0.8rem 1.5rem;
                font-size: 0.9rem;
            }
            
            .stats-overview {
                grid-template-columns: 1fr;
            }
            
            .leaderboard-table {
                font-size: 0.9rem;
            }
            
            .leaderboard-table th,
            .leaderboard-table td {
                padding: 1rem 0.5rem;
            }
            
            .player-cell {
                flex-direction: column;
                align-items: flex-start;
                gap: 0.5rem;
            }
            
            .achievement-cell {
                justify-content: center;
            }
        }

        /* Animations */
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .fade-in-up {
            animation: fadeInUp 0.6s ease-out;
        }

        @keyframes slideInLeft {
            from {
                opacity: 0;
                transform: translateX(-30px);
            }
            to {
                opacity: 1;
                transform: translateX(0);
            }
        }

        .slide-in-left {
            animation: slideInLeft 0.6s ease-out;
        }

        /* Background Canvas */
        #background-canvas {
            position: fixed;
            top: 0;
            left: 0;
            z-index: -1;
            opacity: 0.2;
        }
    </style>
<base target="_blank">
</head>
<body>
    <!-- Background Canvas -->
    <div id="background-canvas"></div>

    <!-- Navigation -->
    <nav class="navbar">
        <div class="nav-content">
            <div class="logo">SMOKEOUT</div>
            <ul class="nav-links">
                <li><a href="index.html">Home</a></li>
                <li><a href="battle.html">Battle</a></li>
                <li><a href="leaderboard.html">Leaderboard</a></li>
                <li><a href="shop.html">Shop</a></li>
            </ul>
        </div>
    </nav>

    <!-- Main Content -->
    <div class="main-content">
        <!-- Page Header -->
        <div class="page-header">
            <h1 class="page-title" data-splitting>LEADERBOARD</h1>
            <p class="page-subtitle">
                Track the ultimate roast warriors and see where you stand in the global rankings
            </p>
        </div>

        <!-- Category Tabs -->
        <div class="category-tabs">
            <button class="tab-button active" data-category="roastbucks">Roastbucks</button>
            <button class="tab-button" data-category="roasts">Total Roasts</button>
            <button class="tab-button" data-category="time">Time Played</button>
            <button class="tab-button" data-category="wins">Wins</button>
            <button class="tab-button" data-category="level">Level</button>
        </div>

        <!-- Stats Overview -->
        <div class="stats-overview">
            <div class="stat-card fade-in-up">
                <span class="stat-icon">👑</span>
                <div class="stat-value">RoastMaster</div>
                <div class="stat-label">Current Champion</div>
                <div class="stat-change positive">+250 RB this week</div>
            </div>
            <div class="stat-card fade-in-up">
                <span class="stat-icon">🔥</span>
                <div class="stat-value">12,847</div>
                <div class="stat-label">Total Roasts This Week</div>
                <div class="stat-change positive">+15% from last week</div>
            </div>
            <div class="stat-card fade-in-up">
                <span class="stat-icon">💰</span>
                <div class="stat-value">458,392</div>
                <div class="stat-label">Total Roastbucks Earned</div>
                <div class="stat-change positive">+8% from last week</div>
            </div>
            <div class="stat-card fade-in-up">
                <span class="stat-icon">⏱️</span>
                <div class="stat-value">1,247h</div>
                <div class="stat-label">Total Play Time</div>
                <div class="stat-change positive">+23% from last week</div>
            </div>
        </div>

        <!-- Personal Stats -->
        <div class="personal-stats">
            <h3>Your Statistics</h3>
            <div class="personal-stats-grid">
                <div class="personal-stat-item">
                    <div class="personal-stat-value" id="player-rank">--</div>
                    <div class="personal-stat-label">Your Rank</div>
                </div>
                <div class="personal-stat-item">
                    <div class="personal-stat-value" id="player-roastbucks">0</div>
                    <div class="personal-stat-label">Roastbucks</div>
                </div>
                <div class="personal-stat-item">
                    <div class="personal-stat-value" id="player-roasts">0</div>
                    <div class="personal-stat-label">Total Roasts</div>
                </div>
                <div class="personal-stat-item">
                    <div class="personal-stat-value" id="player-level">1</div>
                    <div class="personal-stat-label">Current Level</div>
                </div>
                <div class="personal-stat-item">
                    <div class="personal-stat-value" id="player-time">0h</div>
                    <div class="personal-stat-label">Time Played</div>
                </div>
                <div class="personal-stat-item">
                    <div class="personal-stat-value" id="player-wins">0</div>
                    <div class="personal-stat-label">Total Wins</div>
                </div>
            </div>
        </div>

        <!-- Leaderboard Table -->
        <div class="leaderboard-container">
            <div class="leaderboard-header">
                <h2 class="leaderboard-title">Global Rankings</h2>
                <p class="leaderboard-subtitle">Top performers based on <span id="current-criteria">Roastbucks</span></p>
            </div>
            
            <div class="search-bar">
                <input type="text" class="search-input" placeholder="Search for a player..." id="player-search">
            </div>

            <table class="leaderboard-table">
                <thead>
                    <tr>
                        <th>Rank</th>
                        <th>Player</th>
                        <th>Roastbucks</th>
                        <th>Roasts</th>
                        <th>Level</th>
                        <th>Time Played</th>
                        <th>Achievements</th>
                    </tr>
                </thead>
                <tbody id="leaderboard-body">
                    <!-- Leaderboard rows will be populated by JavaScript -->
                </tbody>
            </table>
        </div>

        <!-- Chart Container -->
        <div class="chart-container">
            <h3 class="chart-title">Weekly Activity Trends</h3>
            <div class="chart" id="activity-chart"></div>
        </div>
    </div>

    <!-- Footer -->
    <footer class="footer">
        <p>&copy; 2024 Smokeout Game. Keep roasting and climb those ranks!</p>
    </footer>

    <!-- Main JavaScript -->
    <script src="main.js"></script>
    
    <script>
        // Leaderboard page functionality
        class LeaderboardPage {
            constructor() {
                this.currentCategory = 'roastbucks';
                this.leaderboardData = this.generateLeaderboardData();
                this.filteredData = [...this.leaderboardData];
                this.initializePage();
            }

            generateLeaderboardData() {
                const names = [
                    'RoastMaster', 'BurnKing', 'SavageQueen', 'FireStarter', 'RoastLegend',
                    'MicDropper', 'WordWarrior', 'JokeJuggernaut', 'Punisher', 'InsultArtist',
                    'ComebackKing', 'DissMaster', 'BurnUnit', 'RoastBeast', 'SarcasmSavant',
                    'IronyMaster', 'WitWizard', 'Burninator', 'RoastRanger', 'DissDestroyer',
                    'JokeJedi', 'PunPunisher', 'SarcasmSniper', 'IronyInfantry', 'WitWarrior'
                ];

                return names.map((name, index) => ({
                    name: name,
                    roastbucks: Math.floor(Math.random() * 5000) + 500,
                    roasts: Math.floor(Math.random() * 300) + 50,
                    level: Math.floor(Math.random() * 20) + 1,
                    timePlayed: Math.floor(Math.random() * 10000) + 1000,
                    wins: Math.floor(Math.random() * 100) + 10,
                    achievements: this.generateAchievements(index)
                }));
            }

            generateAchievements(index) {
                const allAchievements = [
                    'First Roast', 'Roast Master', 'Speed Typer', 'Comeback King',
                    'Judge Favorite', 'Team Player', 'Champion', 'Veteran', 'Legend'
                ];
                
                const count = Math.min(Math.floor(Math.random() * 4) + 1, allAchievements.length);
                return allAchievements.slice(0, count);
            }

            initializePage() {
                this.setupEventListeners();
                this.loadPersonalStats();
                this.displayLeaderboard();
                this.initializeChart();
                this.animateElements();
            }

            setupEventListeners() {
                // Category tabs
                document.querySelectorAll('.tab-button').forEach(button => {
                    button.addEventListener('click', (e) => {
                        this.switchCategory(e.target.dataset.category);
                    });
                });

                // Search functionality
                document.getElementById('player-search').addEventListener('input', (e) => {
                    this.searchPlayers(e.target.value);
                });
            }

            switchCategory(category) {
                // Update active tab
                document.querySelectorAll('.tab-button').forEach(btn => {
                    btn.classList.remove('active');
                });
                document.querySelector(`[data-category="${category}"]`).classList.add('active');

                this.currentCategory = category;
                this.sortLeaderboard(category);
                this.displayLeaderboard();
                
                // Update criteria display
                const criteriaNames = {
                    roastbucks: 'Roastbucks',
                    roasts: 'Total Roasts',
                    time: 'Time Played',
                    wins: 'Wins',
                    level: 'Level'
                };
                document.getElementById('current-criteria').textContent = criteriaNames[category];
            }

            sortLeaderboard(category) {
                const sortKeys = {
                    roastbucks: 'roastbucks',
                    roasts: 'roasts',
                    time: 'timePlayed',
                    wins: 'wins',
                    level: 'level'
                };

                const sortKey = sortKeys[category];
                this.leaderboardData.sort((a, b) => b[sortKey] - a[sortKey]);
            }

            displayLeaderboard() {
                const tbody = document.getElementById('leaderboard-body');
                tbody.innerHTML = '';

                this.filteredData.forEach((player, index) => {
                    const row = document.createElement('tr');
                    row.className = 'fade-in-up';
                    row.style.animationDelay = `${index * 0.1}s`;
                    
                    const rank = index + 1;
                    const rankClass = rank <= 3 ? `rank-${rank}` : '';
                    
                    row.innerHTML = `
                        <td class="rank-cell ${rank <= 3 ? 'top-3' : ''} ${rankClass}">
                            #${rank}
                        </td>
                        <td>
                            <div class="player-cell">
                                <div class="player-avatar">${player.name.charAt(0)}</div>
                                <div class="player-info">
                                    <div class="player-name">${player.name}</div>
                                    <div class="player-level">Level ${player.level}</div>
                                </div>
                            </div>
                        </td>
                        <td class="stats-cell">
                            <span class="value">${player.roastbucks.toLocaleString()}</span>
                            <span class="label">RB</span>
                        </td>
                        <td class="stats-cell">
                            <span class="value">${player.roasts}</span>
                            <span class="label">Roasts</span>
                        </td>
                        <td class="stats-cell">
                            <span class="value">${player.level}</span>
                            <span class="label">Level</span>
                        </td>
                        <td class="stats-cell">
                            <span class="value">${Math.floor(player.timePlayed / 3600)}h</span>
                            <span class="label">Time</span>
                        </td>
                        <td>
                            <div class="achievement-cell">
                                ${player.achievements.map(achievement => 
                                    `<span class="achievement-badge">${achievement}</span>`
                                ).join('')}
                            </div>
                        </td>
                    `;
                    
                    tbody.appendChild(row);
                });
            }

            searchPlayers(query) {
                if (!query.trim()) {
                    this.filteredData = [...this.leaderboardData];
                } else {
                    this.filteredData = this.leaderboardData.filter(player =>
                        player.name.toLowerCase().includes(query.toLowerCase())
                    );
                }
                this.displayLeaderboard();
            }

            loadPersonalStats() {
                const playerData = JSON.parse(localStorage.getItem('smokeout-player-data') || '{}');
                
                // Find player's rank
                const playerIndex = this.leaderboardData.findIndex(player => 
                    player.name === 'Player' // Default player name
                );
                
                document.getElementById('player-rank').textContent = 
                    playerIndex !== -1 ? `#${playerIndex + 1}` : 'Unranked';
                document.getElementById('player-roastbucks').textContent = 
                    playerData.roastbucks || 0;
                document.getElementById('player-roasts').textContent = 
                    playerData.totalRoasts || 0;
                document.getElementById('player-level').textContent = 
                    playerData.level || 1;
                document.getElementById('player-time').textContent = 
                    `${Math.floor((playerData.timePlayed || 0) / 3600)}h`;
                document.getElementById('player-wins').textContent = 
                    playerData.wins || 0;
            }

            initializeChart() {
                if (typeof echarts === 'undefined') return;
                
                const chartDom = document.getElementById('activity-chart');
                const myChart = echarts.init(chartDom);
                
                const option = {
                    backgroundColor: 'transparent',
                    tooltip: {
                        trigger: 'axis',
                        backgroundColor: 'rgba(26, 26, 26, 0.9)',
                        borderColor: '#ff6b35',
                        textStyle: {
                            color: '#f5f5f5'
                        }
                    },
                    legend: {
                        data: ['Roasts', 'Roastbucks', 'New Players'],
                        textStyle: {
                            color: '#f5f5f5'
                        },
                        top: 20
                    },
                    grid: {
                        left: '3%',
                        right: '4%',
                        bottom: '3%',
                        containLabel: true
                    },
                    xAxis: {
                        type: 'category',
                        boundaryGap: false,
                        data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
                        axisLine: {
                            lineStyle: {
                                color: '#333'
                            }
                        },
                        axisLabel: {
                            color: '#999'
                        }
                    },
                    yAxis: {
                        type: 'value',
                        axisLine: {
                            lineStyle: {
                                color: '#333'
                            }
                        },
                        axisLabel: {
                            color: '#999'
                        },
                        splitLine: {
                            lineStyle: {
                                color: '#333'
                            }
                        }
                    },
                    series: [
                        {
                            name: 'Roasts',
                            type: 'line',
                            stack: 'Total',
                            data: [120, 132, 101, 134, 90, 230, 210],
                            lineStyle: {
                                color: '#ff6b35'
                            },
                            itemStyle: {
                                color: '#ff6b35'
                            },
                            areaStyle: {
                                color: {
                                    type: 'linear',
                                    x: 0,
                                    y: 0,
                                    x2: 0,
                                    y2: 1,
                                    colorStops: [{
                                        offset: 0, color: 'rgba(255, 107, 53, 0.3)'
                                    }, {
                                        offset: 1, color: 'rgba(255, 107, 53, 0.1)'
                                    }]
                                }
                            }
                        },
                        {
                            name: 'Roastbucks',
                            type: 'line',
                            stack: 'Total',
                            data: [220, 182, 191, 234, 290, 330, 310],
                            lineStyle: {
                                color: '#00d4ff'
                            },
                            itemStyle: {
                                color: '#00d4ff'
                            },
                            areaStyle: {
                                color: {
                                    type: 'linear',
                                    x: 0,
                                    y: 0,
                                    x2: 0,
                                    y2: 1,
                                    colorStops: [{
                                        offset: 0, color: 'rgba(0, 212, 255, 0.3)'
                                    }, {
                                        offset: 1, color: 'rgba(0, 212, 255, 0.1)'
                                    }]
                                }
                            }
                        },
                        {
                            name: 'New Players',
                            type: 'line',
                            stack: 'Total',
                            data: [150, 232, 201, 154, 190, 330, 410],
                            lineStyle: {
                                color: '#39ff14'
                            },
                            itemStyle: {
                                color: '#39ff14'
                            },
                            areaStyle: {
                                color: {
                                    type: 'linear',
                                    x: 0,
                                    y: 0,
                                    x2: 0,
                                    y2: 1,
                                    colorStops: [{
                                        offset: 0, color: 'rgba(57, 255, 20, 0.3)'
                                    }, {
                                        offset: 1, color: 'rgba(57, 255, 20, 0.1)'
                                    }]
                                }
                            }
                        }
                    ]
                };
                
                myChart.setOption(option);
                
                // Resize chart on window resize
                window.addEventListener('resize', () => {
                    myChart.resize();
                });
            }

            animateElements() {
                // Animate title
                Splitting();
                
                anime({
                    targets: '.page-title .char',
                    translateY: [-50, 0],
                    opacity: [0, 1],
                    easing: 'easeOutExpo',
                    duration: 1200,
                    delay: (el, i) => 100 + 30 * i
                });

                // Animate stat cards
                const observer = new IntersectionObserver((entries) => {
                    entries.forEach(entry => {
                        if (entry.isIntersecting) {
                            entry.target.style.opacity = '1';
                            entry.target.style.transform = 'translateY(0)';
                        }
                    });
                });

                document.querySelectorAll('.stat-card, .personal-stat-item').forEach(card => {
                    card.style.opacity = '0';
                    card.style.transform = 'translateY(30px)';
                    card.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
                    observer.observe(card);
                });
            }
        }

        // Initialize leaderboard page
        document.addEventListener('DOMContentLoaded', function() {
            const leaderboardPage = new LeaderboardPage();
            
            // Initialize background animation
            if (typeof p5 !== 'undefined') {
                new p5((p) => {
                    let particles = [];
                    
                    p.setup = () => {
                        const canvas = p.createCanvas(p.windowWidth, p.windowHeight);
                        canvas.parent('background-canvas');
                        canvas.style('position', 'fixed');
                        canvas.style('top', '0');
                        canvas.style('left', '0');
                        canvas.style('z-index', '-1');
                        
                        for (let i = 0; i < 40; i++) {
                            particles.push({
                                x: p.random(p.width),
                                y: p.random(p.height),
                                size: p.random(2, 5),
                                speedX: p.random(-0.8, 0.8),
                                speedY: p.random(-0.8, 0.8),
                                opacity: p.random(0.2, 0.6)
                            });
                        }
                    };
                    
                    p.draw = () => {
                        p.clear();
                        
                        particles.forEach(particle => {
                            p.fill(0, 212, 255, particle.opacity * 255);
                            p.noStroke();
                            p.circle(particle.x, particle.y, particle.size);
                            
                            particle.x += particle.speedX;
                            particle.y += particle.speedY;
                            
                            if (particle.x < 0 || particle.x > p.width) particle.speedX *= -1;
                            if (particle.y < 0 || particle.y > p.height) particle.speedY *= -1;
                        });
                    };
                    
                    p.windowResized = () => {
                        p.resizeCanvas(p.windowWidth, p.windowHeight);
                    };
                });
            }
        });
    </script>
</body>
</html>
