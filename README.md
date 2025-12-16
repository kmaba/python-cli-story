# 🎓 School Days: An Interactive Text Adventure

[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## 📖 Overview

**School Days** is an engaging text-based adventure game that simulates a day in the life of a high school student. Make choices, play mini-games, navigate hallways, and shape your own story through multiple branching pathways!

### ✨ Key Features

- 🎮 **Interactive Storytelling**: Multiple choice-driven pathways with real consequences
- 🏫 **School Setting**: Authentic high school experience with humor and relatable scenarios
- 🎯 **Mini-Games**: 
  - Typing test for English class
  - Sentence correction challenges
  - Math quizzes
  - Science challenges
  - Word puzzle game (Wordle-style)
- 🚶 **ASCII Hallway Navigation**: Move through school corridors with keyboard controls
- ⏱️ **Time Management**: Keep track of your in-game schedule
- 😄 **Humor & Engagement**: Witty dialogue and amusing situations
- 🎨 **Beautiful CLI Interface**: Colorful, intuitive terminal interface using standard Python libraries

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- No external dependencies required! (Uses only Python standard library)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/kmaba/python-cli-story.git
cd python-cli-story
```

2. Run the game:
```bash
python main.py
```

Or on Windows:
```bash
python3 main.py
```

## 🎮 How to Play

1. **Start the Game**: Run `python main.py`
2. **Enter Your Name**: The game will ask for your student name
3. **Make Choices**: Type the number of your choice and press Enter
4. **Play Mini-Games**: Complete challenges to progress through the story
5. **Navigate Hallways**: Use WASD or arrow keys to move through the school
6. **Have Fun**: Explore different pathways and discover multiple endings!

### Controls

- **Menu Selection**: Type the number and press Enter
- **Hallway Navigation**: 
  - W/↑: Move up
  - S/↓: Move down
  - A/←: Move left
  - D/→: Move right
- **Mini-Games**: Follow on-screen instructions

## 📋 Game Structure

### Story Pathways

The game features multiple branching storylines:

1. **The Overachiever Path**: Excel in classes, join clubs, ace all tests
2. **The Social Butterfly Path**: Focus on friendships and social events
3. **The Rebel Path**: Challenge authority and break some rules
4. **The Balanced Path**: Find harmony between academics and social life

### Mini-Games

Each mini-game is designed to be:
- ✅ Quick to complete (1-3 minutes)
- ✅ Integrated into the story
- ✅ Fun and engaging
- ✅ Appropriate difficulty

## 🛠️ Technical Details

### Architecture

```
python-cli-story/
├── main.py                 # Main entry point
├── game/
│   ├── __init__.py
│   ├── engine.py          # Core game engine
│   ├── story.py           # Story content and branching logic
│   ├── player.py          # Player state management
│   └── ui.py              # CLI interface utilities
├── minigames/
│   ├── __init__.py
│   ├── typing_test.py     # English typing mini-game
│   ├── sentence_fix.py    # Grammar correction mini-game
│   ├── math_quiz.py       # Math challenges
│   ├── science_quiz.py    # Science questions
│   └── word_puzzle.py     # Wordle-like game
├── utils/
│   ├── __init__.py
│   ├── hallway.py         # ASCII hallway navigation
│   ├── time_system.py     # In-game time tracking
│   └── wordlist.py        # Word list for puzzles
├── data/
│   └── words.txt          # 5-letter words for Wordle game
├── README.md
└── TODO.md
```

### Design Principles

1. **Standard Library Only**: Compatible with Thonny and basic Python installations
2. **Clean Code**: Well-structured, modular, and maintainable
3. **User-Friendly**: Intuitive interface with clear instructions
4. **Error Handling**: Graceful handling of invalid inputs
5. **Cross-Platform**: Works on Windows, macOS, and Linux

## 🎯 Implementation Plan

### Phase 1: Foundation ✅
- [x] Project structure setup
- [x] README and documentation
- [ ] Core game engine
- [ ] Basic story framework

### Phase 2: Story Content
- [ ] Write main story branches
- [ ] Create character dialogues
- [ ] Add humor and engagement elements
- [ ] Implement choice system

### Phase 3: Mini-Games
- [ ] Typing test implementation
- [ ] Sentence correction game
- [ ] Math quiz system
- [ ] Science challenge
- [ ] Word puzzle (Wordle-style)

### Phase 4: Navigation & Time
- [ ] ASCII hallway system
- [ ] Movement controls
- [ ] Time tracking
- [ ] Schedule integration

### Phase 5: Polish
- [ ] UI enhancements
- [ ] Color and formatting
- [ ] Testing and bug fixes
- [ ] Performance optimization

## 🤝 Contributing

This is a student project, but suggestions and improvements are welcome!

## 📝 License

MIT License - feel free to use this for educational purposes.

## 🎓 Educational Value

This game demonstrates:
- Python programming fundamentals
- Object-oriented design
- State management
- User input handling
- Text parsing and formatting
- Game loop implementation
- Modular code architecture

## 🌟 Credits

Created as an educational text-based adventure game project.

---

**Have fun exploring School Days! 🎒📚**
