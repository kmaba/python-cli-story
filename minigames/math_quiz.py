"""
Math quiz mini-game with various problem types.
Tests arithmetic, algebra, and basic math concepts.
"""

import random
from game.ui import (
    clear_screen, print_title, print_colored, Colors,
    get_input, print_success, print_error, print_info
)


def generate_arithmetic_problem():
    """Generate a random arithmetic problem."""
    operation = random.choice(['+', '-', '*'])
    
    if operation == '+':
        a = random.randint(10, 99)
        b = random.randint(10, 99)
        answer = a + b
        question = f"What is {a} + {b}?"
    elif operation == '-':
        a = random.randint(50, 99)
        b = random.randint(10, a - 1)
        answer = a - b
        question = f"What is {a} - {b}?"
    else:  # multiplication
        a = random.randint(5, 15)
        b = random.randint(5, 15)
        answer = a * b
        question = f"What is {a} × {b}?"
    
    return question, answer


def generate_algebra_problem():
    """Generate a simple algebra problem."""
    problem_type = random.choice(['solve_x', 'evaluate'])
    
    if problem_type == 'solve_x':
        # ax + b = c format
        a = random.randint(2, 10)
        b = random.randint(1, 20)
        x = random.randint(1, 10)
        c = a * x + b
        question = f"Solve for x: {a}x + {b} = {c}"
        answer = x
    else:  # evaluate
        # Evaluate expression
        x = random.randint(1, 10)
        a = random.randint(2, 5)
        b = random.randint(1, 10)
        answer = a * x + b
        question = f"If x = {x}, what is {a}x + {b}?"
    
    return question, answer


def generate_word_problem():
    """Generate a word problem."""
    problems = [
        {
            "question": "Sarah has 15 apples. She gives 3 apples to each of her 4 friends. How many apples does she have left?",
            "answer": 3
        },
        {
            "question": "A book costs $12. If you buy 3 books and have $50, how much money will you have left?",
            "answer": 14
        },
        {
            "question": "There are 24 students in a class. If they form groups of 4, how many groups are there?",
            "answer": 6
        },
        {
            "question": "A train travels 60 miles per hour. How many miles does it travel in 3 hours?",
            "answer": 180
        },
        {
            "question": "Tom scored 85, 90, and 88 on three tests. What is his average score?",
            "answer": 87
        }
    ]
    
    problem = random.choice(problems)
    return problem["question"], problem["answer"]


def play_math_quiz(player):
    """Play the math quiz mini-game."""
    clear_screen()
    print_title("🔢 Math Class: Quick Quiz")
    
    print_colored("Solve these math problems as quickly as you can!", Colors.CYAN)
    print_colored("Show your work mentally and enter your answer.\n", Colors.WHITE)
    
    num_questions = 5
    correct_count = 0
    
    # Generate a mix of problems
    problem_generators = [
        generate_arithmetic_problem,
        generate_arithmetic_problem,
        generate_algebra_problem,
        generate_algebra_problem,
        generate_word_problem
    ]
    
    random.shuffle(problem_generators)
    
    for i in range(num_questions):
        print_colored(f"\nQuestion {i + 1} of {num_questions}", Colors.BRIGHT_BLUE, Colors.BOLD)
        
        question, correct_answer = problem_generators[i]()
        print_colored(question, Colors.WHITE)
        
        # Get user answer
        while True:
            try:
                user_input = get_input("\nYour answer: ")
                user_answer = int(user_input)
                break
            except ValueError:
                print_error("Please enter a valid number!")
        
        # Check answer
        if user_answer == correct_answer:
            print_success("✓ Correct!")
            correct_count += 1
        else:
            print_error(f"✗ Incorrect! The correct answer is {correct_answer}.")
        
        if i < num_questions - 1:
            input("\nPress Enter for the next question...")
    
    # Calculate results
    print("\n" + "=" * 60)
    print_colored("📊 Results:", Colors.BRIGHT_CYAN, Colors.BOLD)
    print_colored(f"   Correct: {correct_count}/{num_questions}", Colors.WHITE)
    
    percentage = (correct_count / num_questions) * 100
    print_colored(f"   Score: {percentage:.0f}%", Colors.BRIGHT_YELLOW)
    print("=" * 60)
    
    # Award points based on performance
    if percentage == 100:
        print_success("\n🌟 Perfect score! You're a math wizard!")
        points = 20
    elif percentage >= 80:
        print_success("\n✨ Excellent work! Great math skills!")
        points = 15
    elif percentage >= 60:
        print_info("\n👍 Good job! Keep practicing!")
        points = 10
    elif percentage >= 40:
        print_info("\n📝 Not bad! Math takes practice.")
        points = 5
    else:
        print_info("\n🤔 Keep studying! You'll improve!")
        points = 3
    
    player.add_grade_points('math', points)
    print_colored(f"\nMath grade +{points}!", Colors.BRIGHT_GREEN)
    
    player.complete_minigame('math_quiz')
    
    return {
        'correct': correct_count,
        'total': num_questions,
        'percentage': percentage,
        'points': points
    }


if __name__ == "__main__":
    # Test the game
    from game.player import Player
    
    test_player = Player("Test Student")
    result = play_math_quiz(test_player)
    print(f"\nTest results: {result}")
    print(f"Player stats: {test_player.get_stats_summary()}")
