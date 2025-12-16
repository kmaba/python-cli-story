#!/usr/bin/env python3
"""
Simple test script for School Days game.
Verifies all components work correctly.
"""

import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def test_imports():
    """Test that all modules can be imported."""
    print("Testing imports...")
    
    try:
        from game.engine import GameEngine
        from game.story import Story, StoryNode
        from game.player import Player
        from game.ui import Colors, clear_screen, print_colored
        from utils.time_system import TimeSystem
        from utils.hallway import Hallway, SimpleHallway
        from utils.wordlist import load_words, get_random_word
        from minigames import typing_test, sentence_fix, math_quiz, science_quiz, word_puzzle
        print("✓ All imports successful")
        return True
    except Exception as e:
        print(f"✗ Import failed: {e}")
        return False


def test_player():
    """Test player functionality."""
    print("\nTesting player...")
    
    try:
        from game.player import Player
        
        player = Player("Test Student")
        assert player.name == "Test Student"
        assert player.get_gpa() == 3.0
        
        player.add_grade_points('math', 10)
        assert player.grades['math'] == 85
        
        player.change_popularity(20)
        assert player.popularity == 70
        
        player.add_item("Pencil")
        assert player.has_item("Pencil")
        
        print("✓ Player tests passed")
        return True
    except Exception as e:
        print(f"✗ Player test failed: {e}")
        return False


def test_time_system():
    """Test time system."""
    print("\nTesting time system...")
    
    try:
        from utils.time_system import TimeSystem
        
        time_sys = TimeSystem()
        assert time_sys.current_period == 1
        assert time_sys.get_current_period_name() == "Homeroom"
        
        time_sys.advance_period()
        assert time_sys.current_period == 2
        
        print("✓ Time system tests passed")
        return True
    except Exception as e:
        print(f"✗ Time system test failed: {e}")
        return False


def test_wordlist():
    """Test word list loading."""
    print("\nTesting word list...")
    
    try:
        from utils.wordlist import load_words, get_random_word, get_word_hints
        
        words = load_words()
        assert len(words) > 0
        print(f"  Loaded {len(words)} words")
        
        word = get_random_word(words)
        assert len(word) == 5
        assert word.isupper()
        
        # Test hint system
        hints = get_word_hints("HELLO", "HELLO")
        assert all(h == 'correct' for h in hints)
        
        print("✓ Word list tests passed")
        return True
    except Exception as e:
        print(f"✗ Word list test failed: {e}")
        return False


def test_story():
    """Test story creation."""
    print("\nTesting story system...")
    
    try:
        from game.story import Story
        from game.player import Player
        from utils.time_system import TimeSystem
        
        player = Player("Test")
        time_sys = TimeSystem()
        story = Story(player, time_sys)
        
        assert "start" in story.story_nodes
        assert "first_period" in story.story_nodes
        assert "end_of_day" in story.story_nodes
        
        print(f"  Created {len(story.story_nodes)} story nodes")
        print("✓ Story system tests passed")
        return True
    except Exception as e:
        print(f"✗ Story test failed: {e}")
        return False


def test_game_engine():
    """Test game engine creation."""
    print("\nTesting game engine...")
    
    try:
        from game.engine import GameEngine
        
        engine = GameEngine()
        assert engine.player is None
        assert engine.time_system is None
        assert engine.story is None
        
        print("✓ Game engine tests passed")
        return True
    except Exception as e:
        print(f"✗ Game engine test failed: {e}")
        return False


def main():
    """Run all tests."""
    print("=" * 60)
    print("School Days - Component Tests")
    print("=" * 60)
    
    tests = [
        test_imports,
        test_player,
        test_time_system,
        test_wordlist,
        test_story,
        test_game_engine
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        if test():
            passed += 1
        else:
            failed += 1
    
    print("\n" + "=" * 60)
    print(f"Results: {passed} passed, {failed} failed")
    print("=" * 60)
    
    if failed == 0:
        print("\n✅ All tests passed! Game is ready to play.")
        print("\nTo play the game, run: python main.py")
        return 0
    else:
        print("\n❌ Some tests failed. Please fix the issues.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
