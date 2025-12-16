"""
Wordle-style word puzzle mini-game.
Player has 6 attempts to guess a 5-letter word.
"""

from utils.wordlist import load_words, get_random_word, get_word_hints, format_guess_with_hints
from game.ui import (
    clear_screen, print_title, print_colored, Colors,
    get_input, print_success, print_error, print_info
)


def play_word_puzzle(player):
    """Play the Wordle-style word puzzle game."""
    clear_screen()
    print_title("📚 English Class: Word Puzzle Challenge")
    
    print_colored("Welcome to Word Master! Guess the 5-letter word in 6 tries.", Colors.CYAN)
    print_colored("Green = correct position, Yellow = wrong position, Gray = not in word\n", Colors.WHITE)
    
    # Load words and select target
    words = load_words()
    target_word = get_random_word(words)
    
    attempts = 6
    guesses = []
    
    for attempt in range(1, attempts + 1):
        print_colored(f"\nAttempt {attempt}/{attempts}", Colors.BRIGHT_BLUE)
        
        # Get valid guess
        while True:
            guess = get_input("Enter your 5-letter guess: ").upper()
            
            if len(guess) != 5:
                print_error("Please enter exactly 5 letters!")
                continue
            
            if not guess.isalpha():
                print_error("Please use only letters!")
                continue
            
            if guess not in words:
                print_error("That's not in our word list! Try another word.")
                continue
            
            break
        
        # Check the guess
        hints = get_word_hints(target_word, guess)
        formatted_guess = format_guess_with_hints(guess, hints)
        
        guesses.append((guess, hints))
        
        # Display all previous guesses
        print("\nYour guesses:")
        for g, h in guesses:
            print("  " + format_guess_with_hints(g, h))
        
        # Check if won
        if guess == target_word:
            print_success(f"\n🎉 Congratulations! You guessed the word: {target_word}")
            print_colored(f"You solved it in {attempt} attempt(s)!", Colors.BRIGHT_GREEN)
            
            # Award points based on attempts
            points = max(10, 25 - (attempt * 3))
            player.add_grade_points('english', points)
            print_success(f"English grade +{points}!")
            
            player.complete_minigame('word_puzzle')
            return True
    
    # Failed to guess
    print_error(f"\n😞 Out of attempts! The word was: {target_word}")
    print_colored("Better luck next time!", Colors.YELLOW)
    
    player.add_grade_points('english', 5)
    print_info("English grade +5 for trying!")
    
    player.complete_minigame('word_puzzle')
    return False


if __name__ == "__main__":
    # Test the game
    from game.player import Player
    
    test_player = Player("Test Student")
    result = play_word_puzzle(test_player)
    print(f"\nGame result: {'Won' if result else 'Lost'}")
    print(f"Player stats: {test_player.get_stats_summary()}")
