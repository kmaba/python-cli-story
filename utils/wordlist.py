"""
Word list utilities for word-based mini-games.
Loads and manages the word list for the Wordle-style game.
"""

import os
import random


def load_words(filename='data/words.txt'):
    """Load words from the word list file."""
    try:
        # Get the path relative to the project root
        current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        filepath = os.path.join(current_dir, filename)
        
        with open(filepath, 'r') as f:
            words = [line.strip().upper() for line in f if line.strip()]
        return words
    except FileNotFoundError:
        # Fallback word list if file not found
        return [
            "ABOUT", "ABOVE", "ABUSE", "ACTOR", "ACUTE", "ADMIT", "ADOPT", "ADULT",
            "AFTER", "AGAIN", "AGENT", "AGREE", "AHEAD", "ALARM", "ALBUM", "ALERT",
            "ALIKE", "ALIVE", "ALLOW", "ALONE", "ALONG", "ALTER", "ANGER", "APPLE",
            "APPLY", "ARENA", "AVOID", "BASIC", "BEACH", "BEGAN", "BEING", "BLACK",
            "BLANK", "BRAIN", "BRAVE", "BREAD", "BREAK", "BRING", "BUILD", "CHAIR",
            "CHARM", "CHASE", "CHEAP", "CHECK", "CHEST", "CHIEF", "CHILD", "CLAIM",
            "CLASS", "CLEAN", "CLEAR", "CLIMB", "CLOCK", "CLOSE", "COACH", "COULD",
            "COUNT", "COVER", "CREAM", "CRIME", "DANCE", "DEATH", "DELAY", "DREAM",
            "DRESS", "DRINK", "DRIVE", "EARTH", "EIGHT", "EMPTY", "ENJOY", "ENTER",
            "EQUAL", "ERROR", "EVENT", "EXACT", "FAITH", "FALSE", "FIELD", "FIGHT",
            "FINAL", "FIRST", "FLASH", "FOCUS", "FORCE", "FOUND", "FRAME", "FRESH",
            "FRUIT", "GIVEN", "GLASS", "GOING", "GRACE", "GRADE", "GRAND", "GRANT",
            "GRASS", "GREAT", "GREEN", "GROUP", "GUARD", "GUESS", "GUEST", "GUIDE",
            "HAPPY", "HEART", "HEAVY", "HORSE", "HOTEL", "HOUSE", "HUMAN", "IMAGE",
            "JAPAN", "JUDGE", "KNOWN", "LARGE", "LASER", "LATER", "LAUGH", "LEARN",
            "LEAST", "LEAVE", "LEGAL", "LEVEL", "LIGHT", "LIMIT", "LINKS", "LIVED",
            "LOCAL", "LOGIC", "LOWER", "LUCKY", "MAGIC", "MAJOR", "MARCH", "MATCH",
            "MAYBE", "MAYOR", "MEANT", "MEDIA", "METAL", "MIGHT", "MINOR", "MIXED",
            "MODEL", "MONEY", "MONTH", "MORAL", "MOTOR", "MOUNT", "MOVED", "MOVIE",
            "MUSIC", "NEVER", "NEWLY", "NIGHT", "NOISE", "NORTH", "NOTED", "NOVEL",
            "NURSE", "OCCUR", "OCEAN", "OFFER", "OFTEN", "ORDER", "OTHER", "OUGHT",
            "OWNED", "OWNER", "PAINT", "PANEL", "PAPER", "PARTY", "PEACE", "PHASE",
            "PHONE", "PHOTO", "PIECE", "PILOT", "PLACE", "PLAIN", "PLANE", "PLANT",
            "PLATE", "POINT", "POUND", "POWER", "PRESS", "PRICE", "PRIDE", "PRIME",
            "PRINT", "PRIOR", "PROOF", "PROUD", "PROVE", "QUEEN", "QUICK", "QUIET",
            "QUITE", "RADIO", "RAISE", "RANGE", "RAPID", "REACH", "READY", "RIGHT",
            "RIVER", "ROUGH", "ROUND", "ROUTE", "ROYAL", "RURAL", "SCALE", "SCENE",
            "SCOPE", "SCORE", "SENSE", "SERVE", "SEVEN", "SHALL", "SHAPE", "SHARE",
            "SHARP", "SHEET", "SHIFT", "SHINE", "SHIRT", "SHOOT", "SHORT", "SHOWN",
            "SIGHT", "SINCE", "SIXTH", "SIZED", "SKILL", "SLEEP", "SLIDE", "SMALL",
            "SMART", "SMILE", "SMOKE", "SOLID", "SOLVE", "SORRY", "SOUND", "SOUTH",
            "SPACE", "SPARE", "SPEAK", "SPEED", "SPEND", "SPENT", "SPLIT", "SPORT",
            "STAFF", "STAGE", "STAND", "START", "STATE", "STEAM", "STEEL", "STILL",
            "STOCK", "STONE", "STORE", "STORM", "STORY", "STUCK", "STUDY", "STUFF",
            "STYLE", "SUGAR", "SWEET", "TABLE", "TAKEN", "TEACH", "TERMS", "TEXAS",
            "THANK", "THEIR", "THEME", "THERE", "THESE", "THICK", "THING", "THINK",
            "THIRD", "THOSE", "THREE", "THROW", "TIGHT", "TIMES", "TIRED", "TITLE",
            "TODAY", "TOPIC", "TOTAL", "TOUCH", "TOUGH", "TOWER", "TRACK", "TRADE",
            "TRAIN", "TREAT", "TRIAL", "TRIED", "TRUCK", "TRULY", "TRUST", "TRUTH",
            "TWICE", "UNCLE", "UNDER", "UNION", "UNITY", "UNTIL", "UPPER", "URBAN",
            "USUAL", "VALID", "VALUE", "VIDEO", "VISIT", "VITAL", "VOICE", "WASTE",
            "WATCH", "WATER", "WHEEL", "WHERE", "WHICH", "WHILE", "WHITE", "WHOLE",
            "WOMAN", "WORLD", "WORRY", "WORSE", "WORST", "WORTH", "WOULD", "WRITE",
            "WRONG", "YIELD", "YOUNG", "YOUTH"
        ]


def get_random_word(words=None):
    """Get a random word from the word list."""
    if words is None:
        words = load_words()
    return random.choice(words)


def get_word_hints(target_word, guess):
    """
    Get hints for a Wordle-style game.
    Returns a list of hints: 'correct', 'present', or 'absent'.
    """
    if len(guess) != len(target_word):
        return None
    
    hints = []
    target_chars = list(target_word)
    
    # First pass: mark correct positions
    for i, char in enumerate(guess):
        if char == target_word[i]:
            hints.append('correct')
            target_chars[i] = None  # Mark as used
        else:
            hints.append(None)  # Placeholder
    
    # Second pass: mark present letters
    for i, char in enumerate(guess):
        if hints[i] is None:  # Not already marked as correct
            if char in target_chars:
                hints[i] = 'present'
                target_chars[target_chars.index(char)] = None  # Mark as used
            else:
                hints[i] = 'absent'
    
    return hints


def format_guess_with_hints(guess, hints):
    """Format a guess with color hints for display."""
    from game.ui import Colors
    
    output = ""
    for char, hint in zip(guess, hints):
        if hint == 'correct':
            output += f"{Colors.BRIGHT_GREEN}{char}{Colors.RESET}"
        elif hint == 'present':
            output += f"{Colors.BRIGHT_YELLOW}{char}{Colors.RESET}"
        else:  # absent
            output += f"{Colors.BRIGHT_BLACK}{char}{Colors.RESET}"
    return output
