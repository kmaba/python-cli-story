"""
ASCII hallway navigation system for the School Days game.
Allows player to move through the school in a 2D grid.
"""

import sys
import os


class Hallway:
    """Manages the ASCII hallway navigation."""
    
    # Map layout: '#' = wall, ' ' = walkable, letters = rooms
    SCHOOL_MAP = [
        "####################",
        "#   A     B     C  #",
        "#                  #",
        "#   D     E     F  #",
        "#                  #",
        "# G      H        I#",
        "#                  #",
        "#   J     K     L  #",
        "####################"
    ]
    
    # Room labels
    ROOMS = {
        'A': "English Classroom",
        'B': "Math Classroom",
        'C': "Science Lab",
        'D': "History Classroom",
        'E': "Principal's Office",
        'F': "Art Room",
        'G': "Cafeteria",
        'H': "Gymnasium",
        'I': "Music Room",
        'J': "Library",
        'K': "Computer Lab",
        'L': "Nurse's Office"
    }
    
    def __init__(self):
        """Initialize the hallway system."""
        # Starting position (middle of hallway)
        self.player_x = 9
        self.player_y = 4
        self.map_data = [list(row) for row in self.SCHOOL_MAP]
        
    def can_move(self, x, y):
        """Check if the player can move to the given position."""
        if 0 <= y < len(self.map_data) and 0 <= x < len(self.map_data[0]):
            cell = self.map_data[y][x]
            return cell != '#'
        return False
    
    def move(self, direction):
        """Move the player in the given direction."""
        new_x, new_y = self.player_x, self.player_y
        
        if direction in ['w', 'W', 'up']:
            new_y -= 1
        elif direction in ['s', 'S', 'down']:
            new_y += 1
        elif direction in ['a', 'A', 'left']:
            new_x -= 1
        elif direction in ['d', 'D', 'right']:
            new_x += 1
        else:
            return False
        
        if self.can_move(new_x, new_y):
            self.player_x = new_x
            self.player_y = new_y
            return True
        return False
    
    def get_current_room(self):
        """Get the current room name if player is standing on a room location."""
        cell = self.map_data[self.player_y][self.player_x]
        if cell in self.ROOMS:
            return self.ROOMS[cell]
        return None
    
    def render(self):
        """Render the hallway with the player position."""
        lines = []
        lines.append("\n🏫 School Hallway")
        lines.append("=" * 40)
        
        for y, row in enumerate(self.map_data):
            line = ""
            for x, cell in enumerate(row):
                if x == self.player_x and y == self.player_y:
                    line += "*"  # Player marker
                else:
                    line += cell
            lines.append(line)
        
        lines.append("=" * 40)
        
        # Show controls
        lines.append("Controls: W/↑=Up, S/↓=Down, A/←=Left, D/→=Right, Q=Quit")
        
        # Show current location
        current_room = self.get_current_room()
        if current_room:
            lines.append(f"\n📍 You are at: {current_room}")
        else:
            lines.append("\n📍 You are in the hallway")
        
        # Show legend
        lines.append("\nLegend: * = You, # = Wall, Letters = Rooms")
        
        return "\n".join(lines)
    
    def get_room_list(self):
        """Get a formatted list of all rooms."""
        lines = ["\n🗺️  School Map:"]
        lines.append("─" * 40)
        for letter, room_name in sorted(self.ROOMS.items()):
            lines.append(f"  {letter} - {room_name}")
        lines.append("─" * 40)
        return "\n".join(lines)
    
    def navigate(self):
        """Run the navigation mini-game."""
        from game.ui import clear_screen, print_colored, Colors
        
        print(self.get_room_list())
        print("\nNavigate to your destination using WASD or arrow keys.")
        print("Press Q to exit navigation mode.\n")
        input("Press Enter to start...")
        
        while True:
            clear_screen()
            print(self.render())
            
            # Get input
            if os.name == 'nt':  # Windows
                import msvcrt
                key = msvcrt.getch().decode('utf-8').lower()
            else:  # Unix/Linux/Mac
                import tty
                import termios
                fd = sys.stdin.fileno()
                old_settings = termios.tcgetattr(fd)
                try:
                    tty.setraw(fd)
                    key = sys.stdin.read(1).lower()
                finally:
                    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            
            if key == 'q':
                break
            elif key in ['w', 's', 'a', 'd']:
                moved = self.move(key)
                if not moved:
                    print_colored("\n⚠ Can't move there!", Colors.RED)
                else:
                    current_room = self.get_current_room()
                    if current_room:
                        print_colored(f"\n✓ Arrived at {current_room}!", Colors.GREEN)
                        input("\nPress Enter to continue...")
                        break
        
        return self.get_current_room()


class SimpleHallway:
    """Simplified hallway navigation for better compatibility."""
    
    def __init__(self):
        """Initialize simple hallway."""
        self.locations = [
            "Hallway Entrance",
            "English Classroom",
            "Math Classroom", 
            "Science Lab",
            "Cafeteria",
            "Library",
            "Gymnasium"
        ]
        self.current_index = 0
        
    def show_options(self):
        """Show available movement options."""
        print("\n🏫 Current Location:", self.locations[self.current_index])
        print("\nWhere would you like to go?")
        
        options = []
        if self.current_index > 0:
            options.append(f"1. Go to {self.locations[self.current_index - 1]}")
        if self.current_index < len(self.locations) - 1:
            options.append(f"{len(options) + 1}. Go to {self.locations[self.current_index + 1]}")
        options.append(f"{len(options) + 1}. Stay here")
        
        for opt in options:
            print(opt)
        
        return len(options)
    
    def move(self, choice, num_options):
        """Move based on user choice."""
        if self.current_index > 0 and choice == 1:
            self.current_index -= 1
            return True
        elif self.current_index < len(self.locations) - 1 and choice == (2 if self.current_index > 0 else 1):
            self.current_index += 1
            return True
        return False
    
    def get_current_location(self):
        """Get current location name."""
        return self.locations[self.current_index]
