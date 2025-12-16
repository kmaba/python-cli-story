"""
Science quiz mini-game covering biology, chemistry, and physics.
Multiple choice questions with educational explanations.
"""

import random
from game.ui import (
    clear_screen, print_title, print_colored, Colors,
    get_choice, print_choices, print_success, print_error, print_info
)


# Science questions with multiple choice answers
SCIENCE_QUESTIONS = [
    {
        "question": "What is the chemical symbol for water?",
        "options": ["H2O", "CO2", "O2", "H2"],
        "correct": 0,
        "explanation": "Water is composed of 2 hydrogen atoms and 1 oxygen atom, hence H2O."
    },
    {
        "question": "Which organ pumps blood throughout the human body?",
        "options": ["Liver", "Lungs", "Heart", "Kidney"],
        "correct": 2,
        "explanation": "The heart is a muscular organ that pumps blood through the circulatory system."
    },
    {
        "question": "What is the speed of light in a vacuum?",
        "options": ["300,000 km/s", "150,000 km/s", "500,000 km/s", "100,000 km/s"],
        "correct": 0,
        "explanation": "Light travels at approximately 300,000 kilometers per second in a vacuum."
    },
    {
        "question": "What gas do plants absorb from the atmosphere?",
        "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"],
        "correct": 2,
        "explanation": "Plants absorb CO2 during photosynthesis and release oxygen."
    },
    {
        "question": "How many bones are in the adult human body?",
        "options": ["186", "206", "226", "246"],
        "correct": 1,
        "explanation": "Adults have 206 bones, while babies are born with about 270 that fuse over time."
    },
    {
        "question": "What is the smallest unit of life?",
        "options": ["Atom", "Molecule", "Cell", "Organ"],
        "correct": 2,
        "explanation": "The cell is the basic structural and functional unit of all living organisms."
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Venus", "Mars", "Jupiter", "Saturn"],
        "correct": 1,
        "explanation": "Mars appears red due to iron oxide (rust) on its surface."
    },
    {
        "question": "What type of energy does a moving object have?",
        "options": ["Potential", "Kinetic", "Thermal", "Chemical"],
        "correct": 1,
        "explanation": "Kinetic energy is the energy of motion."
    },
    {
        "question": "What is the process by which plants make food?",
        "options": ["Respiration", "Photosynthesis", "Digestion", "Fermentation"],
        "correct": 1,
        "explanation": "Photosynthesis converts light energy into chemical energy stored in glucose."
    },
    {
        "question": "Which element has the atomic number 1?",
        "options": ["Helium", "Hydrogen", "Carbon", "Oxygen"],
        "correct": 1,
        "explanation": "Hydrogen is the lightest and most abundant element in the universe."
    },
    {
        "question": "What is the force that pulls objects toward Earth?",
        "options": ["Magnetism", "Friction", "Gravity", "Tension"],
        "correct": 2,
        "explanation": "Gravity is the force of attraction between objects with mass."
    },
    {
        "question": "What is the largest organ in the human body?",
        "options": ["Liver", "Brain", "Heart", "Skin"],
        "correct": 3,
        "explanation": "The skin is the largest organ, protecting the body and regulating temperature."
    },
    {
        "question": "What are the three states of matter?",
        "options": ["Solid, Liquid, Gas", "Hot, Cold, Warm", "Hard, Soft, Medium", "Big, Small, Tiny"],
        "correct": 0,
        "explanation": "Matter commonly exists in solid, liquid, and gas states (plasma is a fourth state)."
    },
    {
        "question": "What is the center of an atom called?",
        "options": ["Electron", "Proton", "Nucleus", "Neutron"],
        "correct": 2,
        "explanation": "The nucleus contains protons and neutrons, while electrons orbit around it."
    },
    {
        "question": "Which vitamin does sunlight help your body produce?",
        "options": ["Vitamin A", "Vitamin B", "Vitamin C", "Vitamin D"],
        "correct": 3,
        "explanation": "Sunlight helps the skin produce Vitamin D, important for bone health."
    }
]


def play_science_quiz(player):
    """Play the science quiz mini-game."""
    clear_screen()
    print_title("🔬 Science Class: Knowledge Challenge")
    
    print_colored("Test your science knowledge across biology, chemistry, and physics!", Colors.CYAN)
    print_colored("Choose the best answer for each question.\n", Colors.WHITE)
    
    # Select 5 random questions
    questions = random.sample(SCIENCE_QUESTIONS, min(5, len(SCIENCE_QUESTIONS)))
    
    correct_count = 0
    total_questions = len(questions)
    
    for i, q in enumerate(questions, 1):
        print_colored(f"\nQuestion {i} of {total_questions}", Colors.BRIGHT_BLUE, Colors.BOLD)
        print_colored(q['question'], Colors.WHITE)
        
        print_choices(q['options'])
        
        choice = get_choice("Your answer (1-4): ", 4)
        
        if choice - 1 == q['correct']:
            print_success("✓ Correct!")
            print_colored(f"💡 {q['explanation']}", Colors.GREEN)
            correct_count += 1
        else:
            print_error("✗ Incorrect!")
            print_colored(f"The correct answer is: {q['options'][q['correct']]}", Colors.YELLOW)
            print_colored(f"💡 {q['explanation']}", Colors.CYAN)
        
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
        print_success("\n🌟 Perfect score! You're a science genius!")
        points = 20
    elif percentage >= 80:
        print_success("\n✨ Excellent! You really know your science!")
        points = 15
    elif percentage >= 60:
        print_info("\n👍 Good job! Keep learning!")
        points = 10
    elif percentage >= 40:
        print_info("\n📝 Not bad! Science is fascinating!")
        points = 5
    else:
        print_info("\n🤔 Keep studying! Science is everywhere!")
        points = 3
    
    player.add_grade_points('science', points)
    print_colored(f"\nScience grade +{points}!", Colors.BRIGHT_GREEN)
    
    player.complete_minigame('science_quiz')
    
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
    result = play_science_quiz(test_player)
    print(f"\nTest results: {result}")
    print(f"Player stats: {test_player.get_stats_summary()}")
