#!/usr/bin/env python3
"""
School Days - An Interactive Text Adventure Game

A text-based game set in a high school with multiple choices,
mini-games, and branching narratives.

Usage:
    python main.py
    or
    python3 main.py
"""

import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from game.engine import start_game


def main():
    """Main entry point for the game."""
    print("Starting School Days...")
    start_game()


if __name__ == "__main__":
    main()
