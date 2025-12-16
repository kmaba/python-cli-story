"""
Typing test mini-game for English class.
Measures typing speed and accuracy.
"""

import time
import random
from game.ui import (
    clear_screen, print_title, print_colored, Colors,
    get_input, print_success, print_error, print_info
)


# Sample sentences for typing test
SENTENCES = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a powerful and versatile programming language.",
    "Education is the key to unlocking your potential.",
    "Practice makes perfect when learning new skills.",
    "Reading books expands your mind and imagination.",
    "Science helps us understand the world around us.",
    "Mathematics is the language of the universe.",
    "Hard work and dedication lead to success.",
    "Creativity and innovation drive human progress.",
    "Knowledge is power, and learning never stops.",
]


def calculate_wpm(text, time_taken):
    """Calculate words per minute."""
    word_count = len(text.split())
    minutes = time_taken / 60
    return round(word_count / minutes) if minutes > 0 else 0


def calculate_accuracy(original, typed):
    """Calculate typing accuracy percentage."""
    if len(original) == 0:
        return 0
    
    correct_chars = sum(1 for i, char in enumerate(typed) if i < len(original) and char == original[i])
    accuracy = (correct_chars / len(original)) * 100
    return round(accuracy, 1)


def play_typing_test(player):
    """Play the typing test mini-game."""
    clear_screen()
    print_title("⌨️  English Class: Typing Speed Test")
    
    print_colored("Type the following sentence as quickly and accurately as you can!", Colors.CYAN)
    print_colored("Press Enter when you're ready to start...\n", Colors.YELLOW)
    input()
    
    # Select a random sentence
    sentence = random.choice(SENTENCES)
    
    print_colored("Type this sentence:", Colors.BRIGHT_BLUE)
    print_colored(f"\n  \"{sentence}\"\n", Colors.BRIGHT_WHITE, Colors.BOLD)
    
    # Start timer
    start_time = time.time()
    
    # Get user input
    typed = get_input("Start typing: ")
    
    # End timer
    end_time = time.time()
    time_taken = end_time - start_time
    
    # Calculate results
    wpm = calculate_wpm(sentence, time_taken)
    accuracy = calculate_accuracy(sentence, typed)
    
    # Display results
    print("\n" + "=" * 50)
    print_colored("📊 Results:", Colors.BRIGHT_CYAN, Colors.BOLD)
    print_colored(f"   Time: {time_taken:.1f} seconds", Colors.WHITE)
    print_colored(f"   Speed: {wpm} WPM", Colors.BRIGHT_YELLOW)
    print_colored(f"   Accuracy: {accuracy}%", Colors.BRIGHT_GREEN)
    print("=" * 50)
    
    # Determine performance level and award points
    points = 0
    
    if accuracy >= 95 and wpm >= 40:
        print_success("\n🌟 Outstanding! You're a typing master!")
        points = 20
    elif accuracy >= 90 and wpm >= 30:
        print_success("\n✨ Excellent work! Very impressive!")
        points = 15
    elif accuracy >= 80 and wpm >= 20:
        print_info("\n👍 Good job! Keep practicing!")
        points = 10
    elif accuracy >= 70:
        print_info("\n📝 Not bad! You'll improve with practice.")
        points = 5
    else:
        print_error("\n🤔 Keep practicing! Accuracy is important.")
        points = 3
    
    player.add_grade_points('english', points)
    print_colored(f"\nEnglish grade +{points}!", Colors.BRIGHT_GREEN)
    
    player.complete_minigame('typing_test')
    
    return {
        'wpm': wpm,
        'accuracy': accuracy,
        'time': time_taken,
        'points': points
    }


if __name__ == "__main__":
    # Test the game
    from game.player import Player
    
    test_player = Player("Test Student")
    result = play_typing_test(test_player)
    print(f"\nTest results: {result}")
    print(f"Player stats: {test_player.get_stats_summary()}")
