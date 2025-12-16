# TODO List - School Days Game

## 🎯 High Priority

### Core Game Engine
- [ ] Create `game/engine.py` - Main game loop and state management
- [ ] Create `game/story.py` - Story content and branching narrative
- [ ] Create `game/player.py` - Player state, inventory, stats
- [ ] Create `game/ui.py` - CLI formatting and display utilities
- [ ] Create `main.py` - Entry point and initialization

### Story Development
- [ ] Write opening sequence (morning, getting ready for school)
- [ ] Create at least 4 major decision points
- [ ] Design 3+ different endings
- [ ] Add 15+ story nodes with choices
- [ ] Integrate humor in dialogue and descriptions
- [ ] Create memorable NPCs (teachers, students, principal)

### Mini-Games (Required for MVP)
- [ ] **Typing Test** (`minigames/typing_test.py`)
  - Random sentence generation
  - WPM calculation
  - Accuracy tracking
  - Timer implementation

- [ ] **Sentence Correction** (`minigames/sentence_fix.py`)
  - 5+ sentences with grammatical errors
  - Multiple choice format
  - Explanation of correct answer
  - Scoring system

- [ ] **Math Quiz** (`minigames/math_quiz.py`)
  - Random problem generation
  - Multiple difficulty levels
  - Arithmetic, algebra basics
  - Time limit per question

- [ ] **Science Quiz** (`minigames/science_quiz.py`)
  - Multiple choice questions
  - Topics: Biology, Chemistry, Physics
  - Educational hints
  - Score tracking

- [ ] **Word Puzzle** (`minigames/word_puzzle.py`)
  - Wordle-like mechanics
  - 5-letter word list integration
  - Color feedback (correct/present/absent)
  - 6 attempts limit

### ASCII Hallway Navigation
- [ ] Create `utils/hallway.py` - Hallway display system
- [ ] Design 2D hallway map (arrays)
- [ ] Implement player movement (WASD/Arrow keys)
- [ ] Add room markers (classrooms, cafeteria, gym, etc.)
- [ ] Collision detection for walls
- [ ] Visual updates as player moves
- [ ] Integration with story (unlock areas progressively)

### Time System
- [ ] Create `utils/time_system.py` - In-game time tracking
- [ ] Implement class schedule
- [ ] Show current time in UI
- [ ] Time-based story events
- [ ] Late/on-time mechanics
- [ ] Bell system for class periods

### Supporting Files
- [ ] Create `data/words.txt` - 5-letter words from Scrabble list
- [ ] Create `utils/wordlist.py` - Word loading utilities
- [ ] Add `__init__.py` files for all packages

## 🎨 Medium Priority

### UI Enhancements
- [ ] Add color support using `colorama` alternative (ANSI codes)
- [ ] Create bordered text boxes for important messages
- [ ] Add loading animations
- [ ] Implement clear screen functionality
- [ ] Design title screen ASCII art
- [ ] Create consistent formatting templates

### Story Enhancement
- [ ] Add side quests
- [ ] Create collectible items
- [ ] Implement relationship system with NPCs
- [ ] Add random events
- [ ] Write flavor text for exploration

### Game Features
- [ ] Save/Load game state (pickle or JSON)
- [ ] Stats screen (grades, relationships, achievements)
- [ ] Achievement system
- [ ] Multiple save slots
- [ ] Game over conditions

## 🌟 Low Priority (Nice to Have)

### Additional Mini-Games
- [ ] Music class rhythm game
- [ ] PE dodgeball simulation
- [ ] Cafeteria food choosing mini-game
- [ ] Locker combination puzzle

### Polish
- [ ] Sound effects using beep (system bell)
- [ ] ASCII art for different locations
- [ ] Easter eggs and hidden content
- [ ] Difficulty settings
- [ ] Tutorial/Help system

### Documentation
- [ ] Add code comments
- [ ] Write developer guide
- [ ] Create gameplay walkthrough
- [ ] Add troubleshooting section

## ✅ Completed
- [x] Project structure planned
- [x] README.md created
- [x] TODO.md created
- [x] All directories created (game/, minigames/, utils/, data/)
- [x] Core game engine implemented
- [x] Player management system complete
- [x] Time tracking system complete
- [x] Story engine with 31 story nodes
- [x] All 5 mini-games implemented and tested
- [x] Word list with 528 words loaded
- [x] UI utilities with color support
- [x] Hallway navigation system
- [x] Test suite created (all tests passing)
- [x] Quick start guide created
- [x] Demo script created
- [x] License added
- [x] .gitignore configured

## 📊 Progress Tracking

**Overall Progress**: 95%

### By Component
- Core Engine: 100% ✅
- Story Content: 100% ✅
- Mini-Games: 100% ✅
- Navigation: 100% ✅
- Time System: 100% ✅
- UI/Polish: 95% ✅
- Documentation: 100% ✅

## 🐛 Known Issues
- None yet (project just started!)

## 💡 Ideas for Future Versions
- Multiplayer mode (compare scores)
- More school years (sophomore, junior, senior)
- Different schools with unique stories
- Mobile version
- Web-based version

---

**Last Updated**: 2025-12-16

**Next Review**: After Phase 1 completion

## 👥 Task Assignment (for agent delegation)

### Agent 1: Core Engine Developer
- Responsible for: game engine, player management, main loop
- Files: `game/engine.py`, `game/player.py`, `main.py`

### Agent 2: Story Writer
- Responsible for: narrative content, dialogue, branching paths
- Files: `game/story.py`

### Agent 3: Mini-Game Developer
- Responsible for: all mini-game implementations
- Files: `minigames/*.py`

### Agent 4: UI/Navigation Developer
- Responsible for: CLI interface, hallway navigation, time system
- Files: `game/ui.py`, `utils/hallway.py`, `utils/time_system.py`

### Agent 5: Integration & Testing
- Responsible for: combining components, testing, bug fixes
- Files: All files for integration
