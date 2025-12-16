"""
Story content and branching logic for the School Days game.
Contains all story nodes, choices, and narrative branches.
"""

from game.ui import (
    clear_screen, print_title, print_colored, Colors, type_text,
    print_choices, get_choice, pause, print_box, print_separator
)
from minigames import typing_test, sentence_fix, word_puzzle, math_quiz, science_quiz
from utils.hallway import SimpleHallway


class StoryNode:
    """Represents a node in the story tree."""
    
    def __init__(self, node_id, text, choices=None, action=None, end_game=False):
        """Initialize a story node."""
        self.node_id = node_id
        self.text = text
        self.choices = choices or []
        self.action = action  # Function to execute (e.g., mini-game)
        self.end_game = end_game


class Story:
    """Manages the game story and narrative flow."""
    
    def __init__(self, player, time_system):
        """Initialize the story with player and time system."""
        self.player = player
        self.time_system = time_system
        self.current_node = "start"
        self.story_nodes = self._create_story_nodes()
    
    # Helper functions for node actions
    @staticmethod
    def _reduce_stress_increase_popularity(p, ts):
        """Reduce stress and increase popularity."""
        p.change_stress(-15)
        p.change_popularity(5)
    
    @staticmethod
    def _new_friend_jordan(p, ts):
        """Make friends with Jordan."""
        p.set_relationship("Jordan", 60)
        p.change_popularity(10)
        p.add_achievement("Made a new friend")
    
    @staticmethod
    def _lunch_alone_recovery(p, ts):
        """Recover stress and energy from alone time."""
        p.change_stress(-20)
        p.change_energy(15)
    
    @staticmethod
    def _afternoon_classes_complete(p, ts):
        """Complete afternoon classes."""
        p.add_grade_points('history', 10)
        p.add_grade_points('pe', 10)
        p.change_energy(-20)
        
    def _create_story_nodes(self):
        """Create all story nodes and choices."""
        nodes = {}
        
        # START: Game opening
        nodes["start"] = StoryNode(
            "start",
            f"""
🌅 *BEEP BEEP BEEP* 

Your alarm clock screams at you. It's 7:00 AM on a Monday morning.

You groggily open your eyes and realize - it's your first day at Jefferson High School!
Wait, no... you've been going here for months. But today feels different.

Today is the day of the BIG TEST that everyone's been talking about.
Your performance today could determine your entire future... or at least your grade.

You drag yourself out of bed and get ready for school.
            """,
            [
                ("Rush to school immediately (you might be late!)", "arrival_rushed"),
                ("Take your time and have breakfast (start the day right)", "arrival_calm"),
                ("Check your phone for messages first", "check_phone")
            ]
        )
        
        # Check phone path
        nodes["check_phone"] = StoryNode(
            "check_phone",
            """
You grab your phone and see several messages:

📱 Your best friend Alex: "Dude, did you study for the test??"
📱 Your mom: "Don't forget your lunch! ❤️"
📱 Random group chat: "Who even invented Monday mornings?"

You chuckle at the group chat. At least you're not alone in this struggle.

You glance at the clock - 7:15 AM. School starts at 8:00 AM.
            """,
            [
                ("Reply to Alex and head to school", "arrival_calm"),
                ("Ignore everything and rush to school", "arrival_rushed")
            ]
        )
        
        # Rushed arrival
        nodes["arrival_rushed"] = StoryNode(
            "arrival_rushed",
            """
You sprint out the door, forgetting half your stuff.

*20 minutes later*

You burst through the school doors, panting heavily. The hallways are already full
of students. You made it! But you're flustered and unprepared.

Your teacher, Ms. Rodriguez, gives you a disapproving look as you slide into your seat.

"Cutting it close again, I see," she says with a slight smile. "I hope you're ready
for today's challenges."
            """,
            [
                ("Apologize and focus on the day ahead", "first_period"),
                ("Make a joke to lighten the mood", "joke_response")
            ]
        )
        
        # Calm arrival
        nodes["arrival_calm"] = StoryNode(
            "arrival_calm",
            """
You have a nice breakfast, pack your bag properly, and head to school with time to spare.

*25 minutes later*

You arrive at Jefferson High with 10 minutes before the first bell. Perfect timing!

You see your friends hanging out by the lockers. Alex waves you over.

"Hey! Ready for the gauntlet?" Alex asks, referring to today's series of tests.
"I heard Ms. Rodriguez is making English class extra challenging today."

You nod confidently. You've got this.
            """,
            [
                ("Chat with friends before class", "chat_friends"),
                ("Head directly to class and review notes", "first_period")
            ]
        )
        
        # Chat with friends
        nodes["chat_friends"] = StoryNode(
            "chat_friends",
            """
You spend a few minutes catching up with Alex and your other friends.

"Did you hear about the new transfer student?" whispers Jamie. "Apparently they're
some kind of genius. Already aced the placement tests!"

"Great, more competition," Alex groans. "As if today wasn't stressful enough!"

You all laugh nervously. The bell rings.

"Well, here we go!" you say, heading to your first class.
            """,
            [
                ("Time for First Period - English Class!", "first_period")
            ],
            action=lambda p, ts: ts.advance_period()
        )
        
        # Joke response
        nodes["joke_response"] = StoryNode(
            "joke_response",
            """
You grin and say, "Hey, at least I didn't show up tomorrow instead!"

The class chuckles, and even Ms. Rodriguez cracks a smile.

"Well, let's hope your wit extends to your writing," she says. "Because you're going
to need it today."

The tension in the room eases a bit. Good save!
            """,
            [
                ("Focus on the lesson", "first_period")
            ]
        )
        
        # First period - English class
        nodes["first_period"] = StoryNode(
            "first_period",
            f"""
📚 FIRST PERIOD - ENGLISH CLASS with Ms. Rodriguez

Ms. Rodriguez stands at the front of the classroom, her presence commanding attention.

"Good morning, class! Today we're going to test your language skills in multiple ways.
We'll start with a vocabulary challenge, then move on to grammar, and finally,
typing proficiency."

She smiles mysteriously. "And yes, this all counts toward your grade."

The room fills with nervous energy. You take a deep breath.

"First up," Ms. Rodriguez announces, "our Word Master challenge! Think of it as...
well, a game you might have played before. You have 6 chances to guess a 5-letter word."

Current Time: {self.time_system.get_current_time()}
Current Grade: {self.player.grades['english']}%
            """,
            [
                ("Take the Word Master challenge!", "word_game"),
                ("Ask for a different test", "alternate_english")
            ]
        )
        
        # Word game mini-game
        nodes["word_game"] = StoryNode(
            "word_game",
            "",
            [
                ("Continue to Grammar Challenge", "grammar_challenge")
            ],
            action=lambda p, ts: word_puzzle.play_word_puzzle(p)
        )
        
        # Grammar challenge
        nodes["grammar_challenge"] = StoryNode(
            "grammar_challenge",
            """
"Excellent!" Ms. Rodriguez says. "Now let's test your grammar skills.
I've prepared some sentences that need correction. Show me what you know!"

She projects several sentences on the board, each with grammatical errors.
            """,
            [
                ("Take the Grammar Challenge!", "grammar_game")
            ]
        )
        
        # Grammar game mini-game
        nodes["grammar_game"] = StoryNode(
            "grammar_game",
            "",
            [
                ("Continue to Typing Test", "typing_challenge")
            ],
            action=lambda p, ts: sentence_fix.play_sentence_fix(p)
        )
        
        # Typing challenge
        nodes["typing_challenge"] = StoryNode(
            "typing_challenge",
            """
"One more challenge," Ms. Rodriguez announces. "In the modern world, typing speed
and accuracy matter. Let's see how fast and accurate you are!"

She displays a sentence on the board.

"Type this exactly as you see it, as quickly as you can. Ready?"
            """,
            [
                ("Take the Typing Test!", "typing_game")
            ]
        )
        
        # Typing game mini-game
        nodes["typing_game"] = StoryNode(
            "typing_game",
            "",
            [
                ("English class complete! Time for break", "morning_break")
            ],
            action=lambda p, ts: typing_test.play_typing_test(p)
        )
        
        # Alternate English (skip mini-games)
        nodes["alternate_english"] = StoryNode(
            "alternate_english",
            """
Ms. Rodriguez raises an eyebrow. "Not feeling confident? That's okay, you can take
a traditional written test instead."

She hands you a paper test. You work through it, but you can't help wondering if
the mini-games would have been more fun...

You finish with an average performance.
            """,
            [
                ("Move on to the next period", "morning_break")
            ],
            action=lambda p, ts: p.add_grade_points('english', 8)
        )
        
        # Morning break
        nodes["morning_break"] = StoryNode(
            "morning_break",
            f"""
🕐 BREAK TIME - 9:00 AM

You have a 10-minute break before your next class. Students pour into the hallway.

Your friend Alex catches up with you. "How'd it go? English was intense, right?"

You compare notes and discuss how you did. 

"Next up is Math," Alex groans. "I heard Mr. Thompson is going full-on quiz mode today."

You have some time. What do you want to do?

Current English Grade: {self.player.grades['english']}%
            """,
            [
                ("Review math notes", "math_prep"),
                ("Get a snack from the vending machine", "snack_break"),
                ("Navigate the hallway to the math classroom", "hallway_nav")
            ]
        )
        
        # Math prep
        nodes["math_prep"] = StoryNode(
            "math_prep",
            """
You find a quiet corner and review your math notes. Quadratic equations, word problems,
basic algebra... you go through the key concepts.

*Time well spent!*

You feel more prepared for what's coming.
            """,
            [
                ("Head to Math Class", "second_period")
            ],
            action=lambda p, ts: p.change_stress(-10)
        )
        
        # Snack break
        nodes["snack_break"] = StoryNode(
            "snack_break",
            """
You grab a granola bar from the vending machine. It's a bit stale, but hey,
it's fuel for your brain!

As you munch, you overhear some students talking about how difficult the math
test is going to be. Great.

*Energy restored!*
            """,
            [
                ("Head to Math Class", "second_period")
            ],
            action=lambda p, ts: p.change_energy(10)
        )
        
        # Hallway navigation
        nodes["hallway_nav"] = StoryNode(
            "hallway_nav",
            """
You decide to take the scenic route through the school hallways.

The hallways of Jefferson High are like a maze. You navigate past various classrooms,
the cafeteria, and the gym.
            """,
            [
                ("Navigate to Math Class", "hallway_minigame")
            ]
        )
        
        # Hallway mini-game (simplified version)
        nodes["hallway_minigame"] = StoryNode(
            "hallway_minigame",
            """
You successfully navigate through the hallways, arriving at the Math classroom!
            """,
            [
                ("Enter Math Class", "second_period")
            ],
            action=lambda p, ts: p.visit_location("Math Classroom")
        )
        
        # Second period - Math class
        nodes["second_period"] = StoryNode(
            "second_period",
            f"""
🔢 SECOND PERIOD - MATH CLASS with Mr. Thompson

Mr. Thompson is already writing problems on the board when you enter.

"Take your seats quickly!" he says cheerfully. "Today we're having a rapid-fire
math challenge. I'll give you a variety of problems - arithmetic, algebra, and
some word problems. Speed and accuracy both matter!"

He turns around with a big grin. "Who's ready to exercise their brain?"

Despite his enthusiasm, you can see several students looking nervous.

Current Time: {self.time_system.get_current_time()}
Current Math Grade: {self.player.grades['math']}%
            """,
            [
                ("Take the Math Quiz!", "math_game"),
                ("Request extra time to prepare", "math_delay")
            ]
        )
        
        # Math game mini-game
        nodes["math_game"] = StoryNode(
            "math_game",
            "",
            [
                ("Continue to next class", "third_period")
            ],
            action=lambda p, ts: math_quiz.play_math_quiz(p)
        )
        
        # Math delay
        nodes["math_delay"] = StoryNode(
            "math_delay",
            """
Mr. Thompson nods understandingly. "Sure, take a minute to collect your thoughts."

You use the time to calm your nerves and review the basics mentally.
            """,
            [
                ("Take the Math Quiz now", "math_game")
            ],
            action=lambda p, ts: p.change_stress(-5)
        )
        
        # Third period - Science class
        nodes["third_period"] = StoryNode(
            "third_period",
            f"""
🔬 THIRD PERIOD - SCIENCE CLASS with Dr. Chen

You enter the science lab, where Dr. Chen is setting up some equipment.

"Welcome, scientists!" she says enthusiastically. "Today we're testing your knowledge
across multiple scientific disciplines - biology, chemistry, and physics!"

She pulls out a stack of question cards.

"This will be a quiz-style assessment. Answer the questions to the best of your ability.
Remember, science is all around us!"

Current Time: {self.time_system.get_current_time()}
Current Science Grade: {self.player.grades['science']}%
            """,
            [
                ("Take the Science Quiz!", "science_game"),
                ("Ask about extra credit", "science_extra")
            ]
        )
        
        # Science game mini-game
        nodes["science_game"] = StoryNode(
            "science_game",
            "",
            [
                ("Head to lunch!", "lunch_time")
            ],
            action=lambda p, ts: science_quiz.play_science_quiz(p)
        )
        
        # Science extra credit
        nodes["science_extra"] = StoryNode(
            "science_extra",
            """
Dr. Chen smiles. "I appreciate your initiative! The quiz itself has bonus questions
that can earn you extra points. Do well and you'll be rewarded!"

You nod, feeling motivated.
            """,
            [
                ("Take the Science Quiz!", "science_game")
            ]
        )
        
        # Lunch time
        nodes["lunch_time"] = StoryNode(
            "lunch_time",
            f"""
🍕 LUNCH TIME - 10:45 AM

Finally, lunch! You're exhausted from all the tests but relieved to have a break.

The cafeteria is packed with students. You grab a tray and look around.

Your friend Alex waves you over to a table where several of your friends are sitting.

At another table, you see the new transfer student eating alone. They look a bit lonely.

There's also an empty quiet corner where you could eat and relax by yourself.

Current Energy: {self.player.energy}%
Current Stress: {self.player.stress}%
            """,
            [
                ("Sit with your friends", "lunch_friends"),
                ("Invite the transfer student to join you", "lunch_transfer"),
                ("Eat alone and decompress", "lunch_alone")
            ]
        )
        
        # Lunch with friends
        nodes["lunch_friends"] = StoryNode(
            "lunch_friends",
            """
You join your friends at their table. Everyone is discussing how the tests went.

"That math quiz was brutal!" Jamie exclaims.
"Science wasn't much better," adds Alex.

You all share stories, laugh about mistakes, and support each other.
It's nice to have friends who understand what you're going through.

*Stress reduced, popularity increased!*
            """,
            [
                ("Finish lunch and prepare for afternoon classes", "afternoon_prep")
            ],
            action=Story._reduce_stress_increase_popularity
        )
        
        # Lunch with transfer student
        nodes["lunch_transfer"] = StoryNode(
            "lunch_transfer",
            """
You walk over to the transfer student. "Hey, mind if I join you?"

They look up, surprised and grateful. "Sure! I'm Jordan. I just started here last week."

You introduce yourself and start chatting. Jordan is actually really cool and shares
your interest in video games and science.

"Thanks for sitting with me," Jordan says. "Being new is tough."

You made a new friend today!

*New relationship established! Popularity increased!*
            """,
            [
                ("Finish lunch and prepare for afternoon classes", "afternoon_prep")
            ],
            action=Story._new_friend_jordan
        )
        
        # Lunch alone
        nodes["lunch_alone"] = StoryNode(
            "lunch_alone",
            """
You find a quiet corner and eat your lunch in peace.

It's nice to have some alone time after the intense morning. You mentally review
how you've done so far and psyche yourself up for the afternoon.

*Stress greatly reduced! Energy restored!*
            """,
            [
                ("Finish lunch and prepare for afternoon classes", "afternoon_prep")
            ],
            action=Story._lunch_alone_recovery
        )
        
        # Afternoon prep
        nodes["afternoon_prep"] = StoryNode(
            "afternoon_prep",
            """
The lunch period is ending. You have a few more classes to get through, but you're
feeling more confident now.

You check your schedule:
- History class (light discussion today)
- PE class (physical activity)
- Study hall (free time)

The hardest tests are over. You can relax a bit now.
            """,
            [
                ("Continue through the afternoon", "afternoon_classes")
            ],
            action=lambda p, ts: ts.advance_period()
        )
        
        # Afternoon classes (simplified)
        nodes["afternoon_classes"] = StoryNode(
            "afternoon_classes",
            """
📚 The afternoon flies by...

History class is interesting but low-pressure. You discuss ancient civilizations
and get into a fun debate about historical what-ifs.

PE class gets your blood pumping with a game of dodgeball. It's exhausting but fun!

Study hall gives you time to decompress and chat with friends.

Before you know it, the final bell rings.
            """,
            [
                ("School's over! Time to head home", "end_of_day")
            ],
            action=Story._afternoon_classes_complete
        )
        
        # End of day
        nodes["end_of_day"] = StoryNode(
            "end_of_day",
            f"""
🌆 END OF SCHOOL DAY - 2:00 PM

You made it through the day! 

As you walk out of Jefferson High, you reflect on everything that happened:
- Survived multiple challenging tests
- Made it through mini-games and quizzes
- Connected with friends (and maybe made new ones)
- Learned a lot

Tomorrow will bring new challenges, but today you proved you can handle whatever
comes your way.

════════════════════════════════════════
              FINAL STATS
════════════════════════════════════════

Student Name: {self.player.name}
GPA: {self.player.get_gpa()}/4.0

GRADES:
  English:  {self.player.grades['english']}%
  Math:     {self.player.grades['math']}%
  Science:  {self.player.grades['science']}%
  History:  {self.player.grades['history']}%
  PE:       {self.player.grades['pe']}%

STATS:
  Popularity: {self.player.popularity}/100
  Energy:     {self.player.energy}/100
  Stress:     {self.player.stress}/100

ACHIEVEMENTS: {len(self.player.achievements)}
  {', '.join(self.player.achievements) if self.player.achievements else 'None'}

Mini-games completed: {len(self.player.completed_minigames)}

════════════════════════════════════════
            """,
            [],
            end_game=True
        )
        
        return nodes
    
    def play_node(self, node_id):
        """Play a story node."""
        if node_id not in self.story_nodes:
            print_colored(f"Error: Story node '{node_id}' not found!", Colors.RED)
            return None
        
        node = self.story_nodes[node_id]
        
        # Display story text
        if node.text.strip():
            clear_screen()
            print_colored(node.text, Colors.WHITE)
        
        # Execute action if present
        if node.action:
            pause()
            result = node.action(self.player, self.time_system)
            pause()
        
        # Check if game ends
        if node.end_game:
            return None
        
        # Show choices and get next node
        if not node.choices:
            return None
        
        if len(node.choices) == 1:
            # Only one choice, auto-continue
            pause()
            return node.choices[0][1]
        
        # Multiple choices
        print_separator()
        choice_texts = [choice[0] for choice in node.choices]
        print_choices(choice_texts)
        
        choice_num = get_choice("What do you do? ", len(node.choices))
        
        # Record choice
        self.player.add_choice(node.choices[choice_num - 1][0])
        
        return node.choices[choice_num - 1][1]
    
    def play(self):
        """Play through the story."""
        current_node_id = self.current_node
        
        while current_node_id:
            current_node_id = self.play_node(current_node_id)
        
        # Game ended
        print_title("GAME OVER")
        print_colored("Thanks for playing School Days!", Colors.BRIGHT_CYAN)
        print_colored(f"\nYour final GPA: {self.player.get_gpa()}/4.0", Colors.BRIGHT_YELLOW)
        
        if self.player.get_gpa() >= 3.5:
            print_colored("\n🌟 Outstanding performance! You're on the honor roll!", Colors.BRIGHT_GREEN)
        elif self.player.get_gpa() >= 3.0:
            print_colored("\n✨ Great work! You're doing well!", Colors.GREEN)
        elif self.player.get_gpa() >= 2.5:
            print_colored("\n👍 Good effort! Keep it up!", Colors.YELLOW)
        else:
            print_colored("\n📚 Keep studying! You'll improve!", Colors.CYAN)
