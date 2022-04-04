from person import Person #Roll
from roll import Roll

class Player(Person):
    def __init__(self, name, age, username, id):
        Person.__init__(self, name, age)
        self.__id = id
        self.__username = username
        
        # Scoreboard
        self.__scoreboard = {
            "Ones": '' ,
            "Twos": '',
            "Threes": '',
            "Fours": '',
            "Fives": '',
            "Sixes": '',
            "Top score": 0,
            "Top bonus": '' 
        }
        
        # Scores
        self.__top_score = 0
        self.__top_bonus = 0
        self.__bottom_score = 0
        self.__bonus_bottom = 0
        self.__total_score = 0

    def set_id(self, id):
        self.__id = id
    
    def set_username(self, username):
        self.__username =username

    # Method adding scores to the player scoreboard
    def add_rolled(self, rolled_type , value):
        self.__scoreboard[rolled_type] = value

    # Method adding a rolled score to the top part score.
    def add_top_score(self, value):
        self.__scoreboard["Top score"] += value
        self.__top_score += value

    # Print player scoreborad.
    def print_scoreboard(self):
        print()
        print(f"{self.get_name()}'s SCOREBOARD")
        print("-" *20)
        for key, value in self.__scoreboard.items():
            print (f'{key}: {value}')

    # Check if player get bonus points from upstair.
    def add_top_bonus(self):
        needed_score_to_bonus = 63

        if self.get_top_score() >= needed_score_to_bonus:
            self.__scoreboard["Top bonus"] = 50

        else:
            self.__scoreboard["Top bonus"] = 0

        self.__top_bonus = self.__scoreboard["Top bonus"]

    def get_top_score(self):
        return self.__top_score

    def get_top_bonus(self):
        return self.__top_bonus

    def get_id(self):
        return self.__id

    def get_username(self):
        return self.__username

    def __str__(self):
        return Person.__str__(self) + f', ID: {self.__id}, Username: {self.__username}'