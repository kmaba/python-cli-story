"""
UI utilities for the School Days game.
Provides formatting, colors, and display functions using only standard library.
"""

import os
import sys
import time


class Colors:
    """ANSI color codes for terminal output."""
    # Basic colors
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    
    # Bright colors
    BRIGHT_BLACK = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'
    
    # Styles
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'


def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_colored(text, color=Colors.WHITE, style='', end='\n'):
    """Print colored text to the terminal."""
    print(f"{style}{color}{text}{Colors.RESET}", end=end)


def print_title(text):
    """Print a title with formatting."""
    print("\n" + "=" * 60)
    print_colored(text.center(60), Colors.BRIGHT_CYAN, Colors.BOLD)
    print("=" * 60 + "\n")


def print_box(text, width=60, color=Colors.WHITE):
    """Print text inside a box."""
    lines = text.split('\n')
    print("\n┌" + "─" * (width - 2) + "┐")
    for line in lines:
        padding = width - len(line) - 4
        print_colored(f"│ {line}{' ' * padding} │", color)
    print("└" + "─" * (width - 2) + "┘\n")


def print_separator(char='-', length=60):
    """Print a separator line."""
    print(char * length)


def type_text(text, delay=0.03):
    """Print text with a typing effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def print_choices(choices):
    """Print a list of choices with numbers."""
    print()
    for i, choice in enumerate(choices, 1):
        print_colored(f"  {i}. {choice}", Colors.BRIGHT_YELLOW)
    print()


def get_choice(prompt, num_choices):
    """Get a valid choice from the user."""
    while True:
        try:
            print_colored(prompt, Colors.BRIGHT_GREEN, end='')
            choice = input().strip()
            choice_num = int(choice)
            if 1 <= choice_num <= num_choices:
                return choice_num
            else:
                print_colored(f"Please enter a number between 1 and {num_choices}.", Colors.RED)
        except ValueError:
            print_colored("Please enter a valid number.", Colors.RED)
        except KeyboardInterrupt:
            print_colored("\n\nGame interrupted. Goodbye!", Colors.YELLOW)
            sys.exit(0)


def get_input(prompt, color=Colors.BRIGHT_GREEN):
    """Get input from the user with a colored prompt."""
    print_colored(prompt, color, end='')
    try:
        return input().strip()
    except KeyboardInterrupt:
        print_colored("\n\nGame interrupted. Goodbye!", Colors.YELLOW)
        sys.exit(0)


def print_status_bar(player_name, time, location):
    """Print a status bar at the top of the screen."""
    status = f"Student: {player_name} | Time: {time} | Location: {location}"
    print_colored("─" * 60, Colors.BRIGHT_BLACK)
    print_colored(status.center(60), Colors.CYAN)
    print_colored("─" * 60, Colors.BRIGHT_BLACK)


def pause(message="Press Enter to continue..."):
    """Pause and wait for user input."""
    print_colored(f"\n{message}", Colors.DIM)
    try:
        input()
    except KeyboardInterrupt:
        print_colored("\n\nGame interrupted. Goodbye!", Colors.YELLOW)
        sys.exit(0)


def show_ascii_art(art):
    """Display ASCII art."""
    print_colored(art, Colors.BRIGHT_CYAN)


def animate_dots(message="Loading", duration=2, color=Colors.YELLOW):
    """Show an animated loading message."""
    print_colored(message, color, end='')
    for _ in range(duration * 2):
        time.sleep(0.5)
        print_colored(".", color, end='')
        sys.stdout.flush()
    print()


def print_success(message):
    """Print a success message."""
    print_colored(f"✓ {message}", Colors.BRIGHT_GREEN)


def print_error(message):
    """Print an error message."""
    print_colored(f"✗ {message}", Colors.BRIGHT_RED)


def print_warning(message):
    """Print a warning message."""
    print_colored(f"⚠ {message}", Colors.BRIGHT_YELLOW)


def print_info(message):
    """Print an info message."""
    print_colored(f"ℹ {message}", Colors.BRIGHT_BLUE)
