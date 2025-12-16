"""
Player state management for the School Days game.
Tracks player stats, inventory, relationships, and progress.
"""


class Player:
    """Represents the player character."""
    
    def __init__(self, name):
        """Initialize a new player."""
        self.name = name
        
        # Academic stats
        self.grades = {
            'english': 75,
            'math': 75,
            'science': 75,
            'history': 75,
            'pe': 75
        }
        
        # Social stats
        self.popularity = 50
        self.relationships = {}  # NPC name -> relationship level (0-100)
        
        # Game state
        self.inventory = []
        self.visited_locations = set()
        self.completed_minigames = set()
        self.achievements = []
        
        # Time and schedule
        self.current_period = 1
        self.energy = 100
        self.stress = 0
        
        # Story flags
        self.story_flags = {}
        self.choices_made = []
        
    def add_grade_points(self, subject, points):
        """Add points to a subject grade."""
        if subject in self.grades:
            self.grades[subject] = min(100, self.grades[subject] + points)
            
    def subtract_grade_points(self, subject, points):
        """Subtract points from a subject grade."""
        if subject in self.grades:
            self.grades[subject] = max(0, self.grades[subject] - points)
    
    def get_gpa(self):
        """Calculate the player's GPA."""
        total = sum(self.grades.values())
        average = total / len(self.grades)
        # Convert to 4.0 scale
        return round((average / 100) * 4.0, 2)
    
    def add_item(self, item):
        """Add an item to inventory."""
        self.inventory.append(item)
        
    def remove_item(self, item):
        """Remove an item from inventory."""
        if item in self.inventory:
            self.inventory.remove(item)
            return True
        return False
    
    def has_item(self, item):
        """Check if player has an item."""
        return item in self.inventory
    
    def change_popularity(self, amount):
        """Change popularity by the given amount."""
        self.popularity = max(0, min(100, self.popularity + amount))
        
    def set_relationship(self, npc_name, level):
        """Set relationship level with an NPC."""
        self.relationships[npc_name] = max(0, min(100, level))
        
    def change_relationship(self, npc_name, amount):
        """Change relationship level with an NPC."""
        current = self.relationships.get(npc_name, 50)
        self.relationships[npc_name] = max(0, min(100, current + amount))
        
    def get_relationship(self, npc_name):
        """Get relationship level with an NPC."""
        return self.relationships.get(npc_name, 50)
    
    def visit_location(self, location):
        """Mark a location as visited."""
        self.visited_locations.add(location)
        
    def has_visited(self, location):
        """Check if player has visited a location."""
        return location in self.visited_locations
    
    def complete_minigame(self, game_name):
        """Mark a minigame as completed."""
        self.completed_minigames.add(game_name)
        
    def has_completed_minigame(self, game_name):
        """Check if player has completed a minigame."""
        return game_name in self.completed_minigames
    
    def add_achievement(self, achievement):
        """Add an achievement."""
        if achievement not in self.achievements:
            self.achievements.append(achievement)
            
    def set_flag(self, flag_name, value=True):
        """Set a story flag."""
        self.story_flags[flag_name] = value
        
    def get_flag(self, flag_name, default=False):
        """Get a story flag value."""
        return self.story_flags.get(flag_name, default)
    
    def has_flag(self, flag_name):
        """Check if a story flag is set."""
        return flag_name in self.story_flags and self.story_flags[flag_name]
    
    def add_choice(self, choice_description):
        """Record a choice made by the player."""
        self.choices_made.append(choice_description)
        
    def change_energy(self, amount):
        """Change energy level."""
        self.energy = max(0, min(100, self.energy + amount))
        
    def change_stress(self, amount):
        """Change stress level."""
        self.stress = max(0, min(100, self.stress + amount))
        
    def advance_period(self):
        """Advance to the next class period."""
        self.current_period += 1
        
    def get_stats_summary(self):
        """Get a summary of player stats."""
        return {
            'name': self.name,
            'gpa': self.get_gpa(),
            'popularity': self.popularity,
            'energy': self.energy,
            'stress': self.stress,
            'achievements': len(self.achievements),
            'inventory_items': len(self.inventory)
        }
    
    def __repr__(self):
        """String representation of the player."""
        return f"Player({self.name}, GPA: {self.get_gpa()}, Popularity: {self.popularity})"
