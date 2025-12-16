"""
Core game engine for the School Days game.
Manages game initialization, main loop, and overall game flow.
"""

from game.player import Player
from game.story import Story
from game.ui import (
    clear_screen, print_title, print_colored, Colors,
    get_input, show_ascii_art, pause
)
from utils.time_system import TimeSystem


# ASCII art for title screen
TITLE_ART = """
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║    ███████╗ ██████╗██╗  ██╗ ██████╗  ██████╗ ██╗         ║
║    ██╔════╝██╔════╝██║  ██║██╔═══██╗██╔═══██╗██║         ║
║    ███████╗██║     ███████║██║   ██║██║   ██║██║         ║
║    ╚════██║██║     ██╔══██║██║   ██║██║   ██║██║         ║
║    ███████║╚██████╗██║  ██║╚██████╔╝╚██████╔╝███████╗    ║
║    ╚══════╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝    ║
║                                                           ║
║            ██████╗  █████╗ ██╗   ██╗███████╗             ║
║            ██╔══██╗██╔══██╗╚██╗ ██╔╝██╔════╝             ║
║            ██║  ██║███████║ ╚████╔╝ ███████╗             ║
║            ██║  ██║██╔══██║  ╚██╔╝  ╚════██║             ║
║            ██████╔╝██║  ██║   ██║   ███████║             ║
║            ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝             ║
║                                                           ║
║              An Interactive Text Adventure                ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
"""


class GameEngine:
    """Main game engine that orchestrates the game."""
    
    def __init__(self):
        """Initialize the game engine."""
        self.player = None
        self.time_system = None
        self.story = None
        
    def show_title_screen(self):
        """Display the title screen."""
        clear_screen()
        show_ascii_art(TITLE_ART)
        print_colored("\n        🎓 Navigate school life with choices and challenges! 🎓", Colors.BRIGHT_YELLOW)
        print_colored("\n" + "─" * 63, Colors.BRIGHT_BLACK)
        pause("\nPress Enter to start your school day...")
        
    def show_intro(self):
        """Show the game introduction."""
        clear_screen()
        print_title("Welcome to School Days!")
        
        print_colored("""
Welcome to Jefferson High School, where every choice matters!

In this interactive story, you'll experience a day in the life of a high school
student. You'll face challenging tests, interact with friends, and make decisions
that affect your grades, popularity, and overall experience.

FEATURES:
  📚 Multiple choice-driven story paths
  🎮 Fun mini-games integrated into the story
  ⏰ Time-based progression through the school day
  📊 Grade tracking and performance metrics
  🎯 Multiple outcomes based on your choices

CONTROLS:
  • Select choices by entering the number and pressing Enter
  • Follow on-screen prompts for mini-games
  • Take your time - there's no rush!

TIP: Be yourself, have fun, and don't stress too much about grades.
     Sometimes the journey is more important than the destination!
        """, Colors.CYAN)
        
        pause()
    
    def create_player(self):
        """Create a new player character."""
        clear_screen()
        print_title("Character Creation")
        
        print_colored("Before we begin, let's get to know you!\n", Colors.BRIGHT_CYAN)
        
        while True:
            name = get_input("What is your name? ")
            if name and len(name) > 0:
                break
            print_colored("Please enter a valid name.", Colors.RED)
        
        self.player = Player(name)
        
        print_colored(f"\nWelcome, {name}! ", Colors.BRIGHT_GREEN, end='')
        print_colored("Let's begin your school day adventure!", Colors.WHITE)
        
        pause()
    
    def initialize_game(self):
        """Initialize game components."""
        self.time_system = TimeSystem()
        self.story = Story(self.player, self.time_system)
    
    def show_instructions(self):
        """Show quick instructions."""
        clear_screen()
        print_title("Quick Instructions")
        
        print_colored("""
HOW TO PLAY:

1. READ the story text carefully - it sets the scene!

2. CHOOSE your actions by entering the number of your choice

3. PLAY mini-games when they appear:
   • Typing Test: Type sentences quickly and accurately
   • Grammar Challenge: Fix grammatical errors
   • Word Puzzle: Guess the 5-letter word (like Wordle!)
   • Math Quiz: Solve various math problems
   • Science Quiz: Answer science questions

4. WATCH your stats:
   • Grades: Your performance in each subject
   • Popularity: How well-liked you are
   • Energy: How tired you are
   • Stress: How stressed you feel

5. MAKE CHOICES that reflect your play style:
   • The Overachiever: Focus on perfect grades
   • The Social Butterfly: Build relationships
   • The Balanced: Mix academics and social life

Remember: There's no "wrong" way to play. Have fun and enjoy the story!
        """, Colors.CYAN)
        
        pause()
    
    def play(self):
        """Main game loop."""
        # Show title and intro
        self.show_title_screen()
        self.show_intro()
        
        # Create player
        self.create_player()
        
        # Show instructions
        self.show_instructions()
        
        # Initialize game
        self.initialize_game()
        
        # Play the story
        clear_screen()
        print_colored(f"\n✨ Get ready, {self.player.name}! Your adventure begins now! ✨\n", Colors.BRIGHT_MAGENTA, Colors.BOLD)
        pause()
        
        self.story.play()
        
        # Game ended
        self.show_ending()
    
    def show_ending(self):
        """Show the ending screen."""
        print_colored("\n\n" + "═" * 60, Colors.BRIGHT_BLACK)
        print_colored("Thank you for playing School Days!".center(60), Colors.BRIGHT_CYAN, Colors.BOLD)
        print_colored("═" * 60, Colors.BRIGHT_BLACK)
        
        print_colored("\n🎓 We hope you enjoyed this text adventure!", Colors.YELLOW)
        print_colored("💡 Every playthrough can be different - try again with new choices!", Colors.CYAN)
        print_colored("\n📚 Created as an educational Python project", Colors.WHITE)
        print_colored("🌟 Keep learning and exploring!\n", Colors.GREEN)


def start_game():
    """Start a new game."""
    try:
        engine = GameEngine()
        engine.play()
    except KeyboardInterrupt:
        print_colored("\n\n⚠ Game interrupted. Thanks for playing!", Colors.YELLOW)
    except Exception as e:
        print_colored(f"\n\n❌ An error occurred: {e}", Colors.RED)
        print_colored("Please report this issue if it persists.", Colors.YELLOW)
        raise


if __name__ == "__main__":
    start_game()
