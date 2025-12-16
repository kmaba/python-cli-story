#!/usr/bin/env python3
"""
Demo script for School Days game.
Shows game features without requiring user interaction.
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from game.player import Player
from game.ui import print_title, print_colored, Colors, print_separator
from utils.time_system import TimeSystem
from utils.wordlist import load_words, get_random_word


def demo_player_system():
    """Demonstrate the player system."""
    print_title("Player System Demo")
    
    player = Player("Demo Student")
    
    print_colored("Initial Player Stats:", Colors.BRIGHT_CYAN)
    stats = player.get_stats_summary()
    for key, value in stats.items():
        print_colored(f"  {key}: {value}", Colors.WHITE)
    
    print_separator()
    
    print_colored("\nAdding grade points...", Colors.YELLOW)
    player.add_grade_points('english', 15)
    player.add_grade_points('math', 20)
    print_colored(f"English: 75% → {player.grades['english']}%", Colors.GREEN)
    print_colored(f"Math: 75% → {player.grades['math']}%", Colors.GREEN)
    print_colored(f"New GPA: {player.get_gpa()}/4.0", Colors.BRIGHT_GREEN)
    
    print_separator()
    
    print_colored("\nChanging social stats...", Colors.YELLOW)
    player.change_popularity(25)
    player.set_relationship("Alex", 75)
    print_colored(f"Popularity: 50 → {player.popularity}", Colors.GREEN)
    print_colored(f"Relationship with Alex: {player.get_relationship('Alex')}", Colors.GREEN)
    
    print_separator()
    
    print_colored("\nAdding items to inventory...", Colors.YELLOW)
    player.add_item("Textbook")
    player.add_item("Pencil")
    player.add_item("Calculator")
    print_colored(f"Inventory: {', '.join(player.inventory)}", Colors.GREEN)


def demo_time_system():
    """Demonstrate the time system."""
    print_title("Time System Demo")
    
    time_sys = TimeSystem()
    
    print_colored("School Schedule:", Colors.BRIGHT_CYAN)
    print(time_sys.get_schedule_display())
    
    print_separator()
    
    print_colored("\nAdvancing through the day...", Colors.YELLOW)
    for i in range(4):
        print_colored(f"Period {time_sys.current_period}: {time_sys.get_current_period_name()} at {time_sys.get_current_time()}", Colors.WHITE)
        time_sys.advance_period()
    
    print_colored(f"\nCurrent period: {time_sys.current_period} - {time_sys.get_current_period_name()}", Colors.BRIGHT_GREEN)


def demo_word_system():
    """Demonstrate the word puzzle system."""
    print_title("Word System Demo")
    
    words = load_words()
    print_colored(f"Loaded {len(words)} five-letter words for puzzles", Colors.BRIGHT_CYAN)
    
    print_separator()
    
    print_colored("\nRandom word examples:", Colors.YELLOW)
    for i in range(5):
        word = get_random_word(words)
        print_colored(f"  {i+1}. {word}", Colors.WHITE)
    
    print_separator()
    
    print_colored("\nWordle-style hint system:", Colors.YELLOW)
    from utils.wordlist import get_word_hints, format_guess_with_hints
    
    target = "HELLO"
    guesses = ["HOUSE", "HELPS", "HELLO"]
    
    print_colored(f"Target word: {target}", Colors.BRIGHT_GREEN)
    print_colored("\nGuesses with hints:", Colors.CYAN)
    
    for guess in guesses:
        hints = get_word_hints(target, guess)
        formatted = format_guess_with_hints(guess, hints)
        print(f"  {formatted}")
    
    print_colored("\n  Legend:", Colors.DIM)
    print_colored("  Green = Correct position", Colors.BRIGHT_GREEN)
    print_colored("  Yellow = Wrong position", Colors.BRIGHT_YELLOW)
    print_colored("  Gray = Not in word", Colors.BRIGHT_BLACK)


def demo_game_features():
    """Demonstrate key game features."""
    print_title("Game Features Overview")
    
    print_colored("📚 Story Features:", Colors.BRIGHT_CYAN)
    features = [
        "Multiple branching story paths",
        "Character relationship tracking",
        "Time-based progression through school day",
        "Achievement system",
        "Multiple endings based on choices"
    ]
    for feature in features:
        print_colored(f"  ✓ {feature}", Colors.GREEN)
    
    print_separator()
    
    print_colored("🎮 Mini-Games:", Colors.BRIGHT_CYAN)
    games = [
        "Word Puzzle - Wordle-style word guessing",
        "Typing Test - Speed and accuracy challenge",
        "Grammar Challenge - Fix sentence errors",
        "Math Quiz - Arithmetic and algebra problems",
        "Science Quiz - Biology, chemistry, and physics"
    ]
    for game in games:
        print_colored(f"  ✓ {game}", Colors.GREEN)
    
    print_separator()
    
    print_colored("📊 Tracking Systems:", Colors.BRIGHT_CYAN)
    systems = [
        "Grade tracking (5 subjects)",
        "GPA calculation (4.0 scale)",
        "Popularity/social stats",
        "Energy and stress levels",
        "Inventory management",
        "Achievement collection"
    ]
    for system in systems:
        print_colored(f"  ✓ {system}", Colors.GREEN)


def main():
    """Run all demos."""
    print_colored("\n" + "=" * 70, Colors.BRIGHT_BLACK)
    print_colored("School Days - Interactive Demo".center(70), Colors.BRIGHT_MAGENTA)
    print_colored("=" * 70 + "\n", Colors.BRIGHT_BLACK)
    
    print_colored("This demo showcases the game's systems without requiring user input.\n", Colors.CYAN)
    print_colored("Press Enter to continue through each section...\n", Colors.YELLOW)
    
    try:
        input()
        demo_player_system()
        
        input("\nPress Enter for next demo...")
        demo_time_system()
        
        input("\nPress Enter for next demo...")
        demo_word_system()
        
        input("\nPress Enter for next demo...")
        demo_game_features()
        
        print("\n" + "=" * 70)
        print_colored("Demo Complete!".center(70), Colors.BRIGHT_GREEN)
        print_colored("=" * 70, Colors.BRIGHT_BLACK)
        
        print_colored("\n🎮 Ready to play? Run: python main.py", Colors.BRIGHT_CYAN)
        print_colored("📖 Need help? Check: QUICKSTART.md\n", Colors.CYAN)
        
    except KeyboardInterrupt:
        print_colored("\n\nDemo interrupted. Thanks!", Colors.YELLOW)


if __name__ == "__main__":
    main()
