# Smokeout Game - Project Outline

## File Structure
```
/mnt/okcomputer/output/
├── index.html              # Main menu and game mode selection
├── battle.html             # Battle arena for all game modes
├── leaderboard.html        # Statistics and rankings page
├── shop.html              # Power-up purchase interface
├── main.js                # Core game logic and state management
├── resources/             # Local assets folder
│   └── (no images needed - text only)
└── README.md              # GitHub Pages deployment instructions
```

## Page Breakdown

### 1. index.html - Main Menu Hub
**Purpose**: Game mode selection and player entry point
**Sections**:
- Navigation bar with game title and menu links
- Hero area with animated title and game description
- Game mode selection grid (5 modes: 1v1 Judge, 1v1 No Judge, 2v2, 3v3, 4v4)
- Quick stats display (roastbucks, level, total roasts)
- Featured leaderboard preview (top 5 players)
- Power-up shop quick access button
- How to play instructions panel

**Interactive Elements**:
- Mode selection buttons with hover effects
- Player name input field
- Start game button
- Leaderboard navigation
- Shop navigation

### 2. battle.html - Battle Arena
**Purpose**: Main gameplay interface for all battle modes
**Sections**:
- Game info header (mode, round, timer)
- Team/player display areas with names and stats
- Battle chat/message area showing roast history
- Power-up activation panel
- Message input and submission area
- Judge voting interface (when applicable)
- Round results and progression display
- Bracket visualization (tournament progression)

**Interactive Elements**:
- Message input field with character counter
- Send roast button
- Power-up activation buttons
- Judge vote buttons (yes/no)
- Timer display with countdown
- Turn indicator showing current player

### 3. leaderboard.html - Statistics & Rankings
**Purpose**: Display player statistics and rankings
**Sections**:
- Navigation header
- Statistics category tabs (Total Roasts, Roastbucks, Time Played)
- Player ranking list with search/filter
- Achievement badges and milestones
- Personal statistics dashboard
- Top players highlight section
- Recent activity feed

**Interactive Elements**:
- Category filter tabs
- Player search functionality
- Sort options (ascending/descending)
- Refresh statistics button
- Achievement detail popups

### 4. shop.html - Power-Up Store
**Purpose**: Purchase and manage power-ups
**Sections**:
- Navigation header
- Roastbucks balance display
- Power-up grid with all available items
- Owned power-ups inventory
- Purchase confirmation dialogs
- Power-up descriptions and stats
- Transaction history

**Interactive Elements**:
- Power-up purchase buttons
- Quantity selectors
- Filter by power-up type
- Search power-ups
- Use power-up buttons (for immediate use)

## JavaScript Architecture (main.js)

### Core Classes and Functions

#### Game State Management
- `GameState`: Manages current game mode, players, scores
- `BattleManager`: Handles turn-based gameplay mechanics
- `Timer`: Manages 1:30 turn timers and 15s intermission
- `BracketSystem`: Tournament progression and elimination

#### Player and Team Management
- `Player`: Individual player data, stats, roastbucks
- `Team`: Group management for 2v2, 3v3, 4v4 modes
- `Judge`: Judge system for deciding round winners

#### Power-Up System
- `PowerUp`: Base class for all power-ups
- `PowerUpManager`: Purchase, activation, and effect handling
- `ExtraBurn`, `MicDrop`, `ExtraLine`, etc.: Specific power-up implementations

#### Currency and Progression
- `RoastbucksManager`: Currency tracking and transactions
- `LevelSystem`: Player progression based on roastbucks earned
- `Statistics`: Track roasts sent, time played, wins/losses

#### UI and Interaction
- `UIManager`: Handle all interface updates
- `AnimationController`: Manage visual effects and transitions
- `InputHandler`: Process user input and validation
- `NotificationSystem`: Display game messages and alerts

#### Data Persistence
- `LocalStorage`: Save player progress and statistics
- `GameHistory`: Track recent games and outcomes
- `Settings`: Player preferences and configurations

### Key Features Implementation

#### Battle Mechanics
- Turn-based message system with opponent display
- Real-time timer countdown with visual warnings
- Automatic roastbucks awarding (+1 per message)
- Judge voting system with 15-second intermission
- Bracket advancement and elimination logic

#### Power-Up Effects
- Extra Burn: 2x roastbucks multiplier for round
- Mic Drop: Skip opponent turn functionality
- Extra Line: Allow two-line message input
- Divider: 0.5x opponent roastbucks reduction
- Judge Bias: Force judge vote during intermission
- Reverse Roast: Opponent's message input reversal
- Savage Roast Mode: Ultimate combo with multiple effects

#### Leaderboard System
- Real-time statistics calculation
- Multiple ranking categories
- Achievement tracking and badges
- Player comparison features
- Historical data maintenance

## Visual Effects Integration

### Animation Libraries
- **Anime.js**: UI transitions, button effects, power-up activations
- **Typed.js**: Roast message reveals, dramatic text effects
- **Splitting.js**: Title animations, heading effects
- **ECharts.js**: Leaderboard charts, statistics visualization
- **p5.js**: Background particle effects, dynamic visuals

### Effect Implementation
- Typewriter animation for roast messages
- Pulsing timer with color progression
- Glowing power-up activation effects
- Smooth score counter animations
- Victory screen flash effects
- Particle burst for achievements

## Responsive Design Strategy

### Desktop Layout
- Full split-screen battle view
- Side-by-side team displays
- Expanded power-up panel
- Detailed leaderboard with charts

### Tablet Layout
- Stacked battle view with collapsible panels
- Swipe navigation between sections
- Simplified power-up interface
- Condensed leaderboard display

### Mobile Layout
- Single-column battle view
- Tabbed navigation for different sections
- Touch-optimized power-up buttons
- Minimalist leaderboard with essential stats

## GitHub Pages Deployment

### Configuration Requirements
- Static file hosting compatibility
- No server-side dependencies
- Local storage for data persistence
- Cross-browser compatibility
- Mobile-responsive design

### Performance Optimization
- Minified CSS and JavaScript
- Optimized animation performance
- Efficient data storage and retrieval
- Progressive loading of game assets
- Caching strategies for repeat visits

This comprehensive structure ensures a fully functional, engaging roast battle game that can be easily deployed to GitHub Pages while providing rich gameplay mechanics and smooth user interactions.