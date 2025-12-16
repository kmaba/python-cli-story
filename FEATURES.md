# Features Documentation - School Days

Complete list of all features and systems in the game.

## 🎮 Core Game Features

### Story Engine
- **31 Story Nodes**: Interconnected narrative points
- **Branching Paths**: Multiple routes through the story
- **Dynamic Choices**: Player choices affect the narrative
- **Multiple Endings**: Different outcomes based on decisions
- **Time-Based Progression**: Story advances through school day

### Player System
- **Name Customization**: Choose your student name
- **Grade Tracking**: Monitor performance in 5 subjects
  - English
  - Math  
  - Science
  - History
  - PE
- **GPA Calculation**: Automatic 4.0 scale conversion
- **Social Stats**:
  - Popularity (0-100)
  - Energy (0-100)
  - Stress (0-100)
- **Relationship System**: Track friendships with NPCs
- **Inventory Management**: Collect and use items
- **Achievement Tracking**: Earn special achievements
- **Story Flags**: Track major decisions and events

## 🕐 Time Management System

### Class Schedule
- **8 Periods**: From Homeroom to After School
- **Realistic Timing**: Proper school day progression
- **Period Names**: 
  - Homeroom (8:00 AM)
  - First through Sixth Period
  - Lunch Break
  - After School Activities

### Time Features
- Current period tracking
- Time display in UI
- Late detection system
- Schedule display

## 🎯 Mini-Games (All 5 Implemented)

### 1. Word Puzzle (Wordle-Style)
- **Objective**: Guess a 5-letter word in 6 attempts
- **Features**:
  - 528-word dictionary
  - Color-coded hints (Green/Yellow/Gray)
  - Validation against word list
  - Score based on attempts
- **Rewards**: Up to 25 points to English grade

### 2. Typing Test
- **Objective**: Type sentences quickly and accurately
- **Features**:
  - 10 diverse sentences
  - WPM (Words Per Minute) calculation
  - Accuracy percentage tracking
  - Timer system
- **Scoring**:
  - Outstanding: 95%+ accuracy, 40+ WPM (20 points)
  - Excellent: 90%+ accuracy, 30+ WPM (15 points)
  - Good: 80%+ accuracy, 20+ WPM (10 points)
  - Fair: 70%+ accuracy (5 points)
- **Rewards**: Up to 20 points to English grade

### 3. Grammar Challenge
- **Objective**: Correct grammatical errors in sentences
- **Features**:
  - 6 different error types
  - Multiple choice format
  - Educational explanations
  - 3 random problems per game
- **Error Types Covered**:
  - Pronoun usage
  - Subject-verb agreement
  - Homophones (their/there/they're)
  - Pronoun case
  - Adverb vs adjective
- **Rewards**: Up to 20 points to English grade

### 4. Math Quiz
- **Objective**: Solve 5 varied math problems
- **Features**:
  - Arithmetic (addition, subtraction, multiplication)
  - Algebra (solve for x, evaluate expressions)
  - Word problems
  - Random problem generation
  - 5 questions per quiz
- **Difficulty**: Progressive from basic to intermediate
- **Rewards**: Up to 20 points to Math grade

### 5. Science Quiz
- **Objective**: Answer multiple-choice science questions
- **Features**:
  - 15-question database
  - 5 random questions per quiz
  - Multi-discipline coverage:
    - Biology (cells, organs, systems)
    - Chemistry (elements, compounds, states)
    - Physics (forces, energy, motion)
  - Educational explanations
- **Rewards**: Up to 20 points to Science grade

## 🏫 Navigation System

### ASCII Hallway
- **2D Grid Map**: School layout with rooms
- **12 Locations**:
  - Classrooms (English, Math, Science, History, Art)
  - Special Rooms (Principal's Office, Cafeteria, Gym)
  - Facilities (Library, Computer Lab, Music Room, Nurse's Office)
- **Movement**: WASD/Arrow key controls
- **Visual Feedback**: Live map updates
- **Room Detection**: Automatic location identification

### Simple Navigation
- **Linear Movement**: Alternative simpler system
- **Quick Travel**: Fast movement between key locations
- **Location Tracking**: Visit history

## 🎨 User Interface

### Visual Features
- **ANSI Color Support**: Full color terminal output
- **Color Palette**: 16 colors + styles
  - Basic: Red, Green, Yellow, Blue, Magenta, Cyan, White
  - Bright variants of all colors
  - Styles: Bold, Dim, Italic, Underline
- **Formatted Output**:
  - Title screens with ASCII art
  - Text boxes with borders
  - Status bars
  - Separators and dividers
  - Progress indicators

### Interactive Elements
- **Typing Effect**: Smooth text animation
- **Choice Menus**: Numbered selection system
- **Loading Animations**: Animated dots
- **Input Validation**: Error handling
- **Clear Screen**: Proper screen management

### Status Display
- Student name
- Current time/period
- Current location
- Grade display
- Stats overview

## 📖 Story Paths

### Major Branches

#### 1. The Morning Choice
- **Rushed Path**: Late start, high stress
- **Calm Path**: Prepared, energized
- **Social Path**: Chat with friends

#### 2. Class Performance
- **Overachiever**: Excel in all tests
- **Balanced**: Mix of success and fun
- **Struggle Path**: Lower grades but learning

#### 3. Social Interactions
- **Friend-Focused**: Build relationships
- **Loner Path**: Solo activities
- **New Friend**: Meet transfer student Jordan

#### 4. Energy Management
- **Prepared**: Study and review
- **Energized**: Rest and eat
- **Stressed**: Rush through

### NPCs (Non-Player Characters)
- **Ms. Rodriguez**: English teacher
- **Mr. Thompson**: Math teacher (enthusiastic)
- **Dr. Chen**: Science teacher
- **Alex**: Best friend
- **Jamie**: Friend in your group
- **Jordan**: New transfer student (optional friend)

## 📊 Statistics & Tracking

### Performance Metrics
- Subject grades (0-100%)
- GPA (0.0-4.0 scale)
- Mini-game completion rate
- Choices made log

### Social Metrics
- Popularity level
- Relationship values with NPCs
- Achievements earned

### Resource Metrics
- Energy level
- Stress level
- Inventory items
- Locations visited

## 🏆 Achievement System

### Unlockable Achievements
- "Made a new friend" - Befriend Jordan
- Perfect mini-game scores
- High GPA attainment
- Story path completions
- Hidden achievements

## 💾 Data & Content

### Word Database
- **528 five-letter words**
- Sourced from Scrabble word list
- Filtered for appropriate content
- All uppercase format

### Story Content
- 31 unique story nodes
- 50+ choice options
- Humor integrated throughout
- Multiple character voices
- Educational content

## 🛠️ Technical Features

### Standard Library Only
- **No External Dependencies**
- Pure Python implementation
- Compatible with Thonny
- Cross-platform support (Windows, Mac, Linux)

### Code Architecture
```
📁 game/          - Core game logic
📁 minigames/     - Mini-game implementations  
📁 utils/         - Utility functions
📁 data/          - Game data files
```

### Error Handling
- Input validation
- Graceful error messages
- Keyboard interrupt handling
- File not found fallbacks

### Testing
- Component tests (6 test suites)
- Import verification
- Functionality validation
- Integration testing

## 🎯 Engagement Features

### Humor
- Witty dialogue
- Funny situations
- Relatable school experiences
- Light-hearted tone

### Replay Value
- Multiple story branches
- Different mini-game challenges
- Various relationship outcomes
- Achievement hunting

### Educational Value
- Real grammar rules
- Math practice
- Science facts
- Typing skills

### Time Management
- Quick playthrough (10-15 minutes)
- Natural story pacing
- Break points for resuming
- Progress through school day

## 🌟 Polish & Quality

### User Experience
- Clear instructions
- Intuitive controls
- Helpful feedback
- Error recovery

### Accessibility
- Text-based (screen reader friendly)
- Keyboard-only controls
- No time pressure (most mini-games)
- Adjustable reading pace

### Documentation
- Comprehensive README
- Quick start guide
- Feature documentation (this file!)
- In-code comments
- Test suite

---

**Total Lines of Code**: ~3,500+
**Total Game Features**: 50+
**Estimated Play Time**: 10-15 minutes per playthrough
**Replayability**: High (multiple paths and outcomes)
