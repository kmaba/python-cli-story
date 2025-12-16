"""
Time tracking system for the School Days game.
Manages in-game time, class schedule, and time-based events.
"""


class TimeSystem:
    """Manages in-game time and schedule."""
    
    # School schedule
    SCHEDULE = {
        1: {"name": "Homeroom", "time": "8:00 AM", "duration": 15},
        2: {"name": "First Period", "time": "8:15 AM", "duration": 50},
        3: {"name": "Second Period", "time": "9:05 AM", "duration": 50},
        4: {"name": "Third Period", "time": "9:55 AM", "duration": 50},
        5: {"name": "Lunch", "time": "10:45 AM", "duration": 30},
        6: {"name": "Fourth Period", "time": "11:15 AM", "duration": 50},
        7: {"name": "Fifth Period", "time": "12:05 PM", "duration": 50},
        8: {"name": "Sixth Period", "time": "12:55 PM", "duration": 50},
        9: {"name": "After School", "time": "1:45 PM", "duration": None}
    }
    
    def __init__(self):
        """Initialize the time system."""
        self.current_period = 1
        self.minutes_elapsed = 0
        self.is_late = False
        
    def get_current_time(self):
        """Get the current in-game time as a string."""
        period_info = self.SCHEDULE.get(self.current_period, self.SCHEDULE[1])
        return period_info["time"]
    
    def get_current_period_name(self):
        """Get the name of the current period."""
        period_info = self.SCHEDULE.get(self.current_period, self.SCHEDULE[1])
        return period_info["name"]
    
    def advance_period(self):
        """Move to the next period."""
        if self.current_period < 9:
            self.current_period += 1
            self.is_late = False
            return True
        return False
    
    def add_minutes(self, minutes):
        """Add minutes to the elapsed time."""
        self.minutes_elapsed += minutes
        
    def mark_late(self):
        """Mark the player as late to class."""
        self.is_late = True
        
    def is_lunch_time(self):
        """Check if it's lunch time."""
        return self.current_period == 5
    
    def is_after_school(self):
        """Check if school is over."""
        return self.current_period >= 9
    
    def get_time_until_next_period(self):
        """Get minutes until the next period."""
        if self.current_period >= 9:
            return 0
        current = self.SCHEDULE[self.current_period]
        return current["duration"] - (self.minutes_elapsed % current["duration"])
    
    def get_schedule_display(self):
        """Get a formatted schedule display."""
        lines = []
        lines.append("\n📅 Today's Schedule:")
        lines.append("─" * 40)
        for period, info in self.SCHEDULE.items():
            if period == 9:
                continue
            marker = "→" if period == self.current_period else " "
            lines.append(f"{marker} Period {period}: {info['name']:15} ({info['time']})")
        lines.append("─" * 40)
        return "\n".join(lines)
    
    def __repr__(self):
        """String representation of the time system."""
        return f"TimeSystem(Period {self.current_period}: {self.get_current_period_name()})"
