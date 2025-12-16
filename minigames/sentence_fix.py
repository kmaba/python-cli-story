"""
Sentence correction mini-game for English class.
Find and fix grammatical errors in sentences.
"""

import random
from game.ui import (
    clear_screen, print_title, print_colored, Colors,
    get_choice, print_choices, print_success, print_error, print_info
)


# Sentences with errors and their corrections
SENTENCE_PROBLEMS = [
    {
        "sentence": "Me and my friend went to the store yesterday.",
        "error": "Incorrect pronoun usage",
        "options": [
            "My friend and I went to the store yesterday.",
            "Me and my friend gone to the store yesterday.",
            "My friend and me went to the store yesterday.",
            "I and my friend went to the store yesterday."
        ],
        "correct": 0,
        "explanation": "Use 'I' instead of 'me' as the subject. 'My friend and I' is correct."
    },
    {
        "sentence": "The book on the table belong to Sarah.",
        "error": "Subject-verb agreement",
        "options": [
            "The book on the table belongs to Sarah.",
            "The books on the table belong to Sarah.",
            "The book on the tables belong to Sarah.",
            "The book on the table belonging to Sarah."
        ],
        "correct": 0,
        "explanation": "The subject 'book' is singular, so the verb should be 'belongs', not 'belong'."
    },
    {
        "sentence": "Their going to the movies tonight with there friends.",
        "error": "Homophone confusion",
        "options": [
            "They're going to the movies tonight with their friends.",
            "Their going to the movies tonight with their friends.",
            "They're going to the movies tonight with there friends.",
            "There going to the movies tonight with their friends."
        ],
        "correct": 0,
        "explanation": "'They're' (they are) and 'their' (possessive) are the correct forms here."
    },
    {
        "sentence": "Each of the students have completed their assignment.",
        "error": "Subject-verb agreement",
        "options": [
            "Each of the students has completed their assignment.",
            "Each of the students have completed his assignment.",
            "All of the students have completed their assignment.",
            "Each of the students have completed his or her assignment."
        ],
        "correct": 0,
        "explanation": "'Each' is singular, so it requires the singular verb 'has', not 'have'."
    },
    {
        "sentence": "Between you and I, this test is really difficult.",
        "error": "Incorrect pronoun case",
        "options": [
            "Between you and me, this test is really difficult.",
            "Between you and myself, this test is really difficult.",
            "Between I and you, this test is really difficult.",
            "Between yourself and I, this test is really difficult."
        ],
        "correct": 0,
        "explanation": "After a preposition like 'between', use the object pronoun 'me', not 'I'."
    },
    {
        "sentence": "The team are playing good today.",
        "error": "Multiple errors",
        "options": [
            "The team is playing well today.",
            "The team are playing well today.",
            "The team is playing good today.",
            "The teams is playing good today."
        ],
        "correct": 0,
        "explanation": "'Team' is singular (use 'is'), and 'well' is the correct adverb (not 'good')."
    }
]


def play_sentence_fix(player):
    """Play the sentence correction mini-game."""
    clear_screen()
    print_title("✏️  English Class: Grammar Challenge")
    
    print_colored("Fix the grammatical errors in the following sentences!", Colors.CYAN)
    print_colored("Choose the correct version of each sentence.\n", Colors.WHITE)
    
    # Select 3 random problems
    problems = random.sample(SENTENCE_PROBLEMS, min(3, len(SENTENCE_PROBLEMS)))
    
    correct_count = 0
    total_questions = len(problems)
    
    for i, problem in enumerate(problems, 1):
        print_colored(f"\nQuestion {i} of {total_questions}", Colors.BRIGHT_BLUE, Colors.BOLD)
        print_colored(f"Error type: {problem['error']}", Colors.YELLOW)
        print_colored(f"\nOriginal: \"{problem['sentence']}\"", Colors.RED)
        
        print_choices(problem['options'])
        
        choice = get_choice("Select the correct sentence (1-4): ", 4)
        
        if choice - 1 == problem['correct']:
            print_success("✓ Correct!")
            print_colored(f"Explanation: {problem['explanation']}", Colors.GREEN)
            correct_count += 1
        else:
            print_error("✗ Incorrect!")
            print_colored(f"The correct answer is: {problem['options'][problem['correct']]}", Colors.YELLOW)
            print_colored(f"Explanation: {problem['explanation']}", Colors.CYAN)
        
        if i < total_questions:
            input("\nPress Enter to continue...")
    
    # Calculate results
    print("\n" + "=" * 60)
    print_colored("📊 Results:", Colors.BRIGHT_CYAN, Colors.BOLD)
    print_colored(f"   Correct: {correct_count}/{total_questions}", Colors.WHITE)
    
    percentage = (correct_count / total_questions) * 100
    print_colored(f"   Score: {percentage:.0f}%", Colors.BRIGHT_YELLOW)
    print("=" * 60)
    
    # Award points based on performance
    if percentage == 100:
        print_success("\n🌟 Perfect score! You're a grammar expert!")
        points = 20
    elif percentage >= 66:
        print_success("\n✨ Great job! You know your grammar!")
        points = 15
    elif percentage >= 33:
        print_info("\n👍 Good effort! Keep studying!")
        points = 10
    else:
        print_info("\n📝 Keep practicing! Grammar takes time to master.")
        points = 5
    
    player.add_grade_points('english', points)
    print_colored(f"\nEnglish grade +{points}!", Colors.BRIGHT_GREEN)
    
    player.complete_minigame('sentence_fix')
    
    return {
        'correct': correct_count,
        'total': total_questions,
        'percentage': percentage,
        'points': points
    }


if __name__ == "__main__":
    # Test the game
    from game.player import Player
    
    test_player = Player("Test Student")
    result = play_sentence_fix(test_player)
    print(f"\nTest results: {result}")
    print(f"Player stats: {test_player.get_stats_summary()}")
