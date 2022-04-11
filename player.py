# Filename      player.py
# Authors:      Jenna Laaksovirta, Karolina Mäkinen ja Sanna Salminen
# Description:  Players infromtion, scoreboard, checks if player gets bonus points and counts total score

from person import Person # Person
from roll import Roll # Roll

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
            "TOP SCORE": 0,
            "TOP BONUS": '',
            "One pair": '',
            "Two pairs": '',
            "Three of a kind": '',
            "Four of a kind": '',
            "Full house": '',
            "Low straight": '',
            "High straight": '',
            "Chance": '',
            "Yatzy": '',
            "BOTTOM SCORE": 0,
            "TOTAL SCORE": ''
        }

        # Scores
        self.__top_score = 0
        self.__top_bonus = 0
        self.__bottom_score = 0
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
        self.__scoreboard["TOP SCORE"] += value
        self.__top_score += value

    # Print player scoreborad.
    def print_scoreboard(self):
        print()
        print(f"{self.get_name()}'s SCOREBOARD")
        print("-" *20)
        for key, value in self.__scoreboard.items():
            print (f'{key}: {value}')
        print("-" *20)

    # Get player scoreboard.
    def get_scoreboard(self):
        return self.__scoreboard

    # Check if player gets bonus points from upper section
    def add_top_bonus(self):
        if self.get_top_score() >= 63:
            self.__scoreboard["TOP BONUS"] = 50
        else:
            self.__scoreboard["TOP BONUS"] = 0

        self.__top_bonus = self.__scoreboard["TOP BONUS"]

    # Method adding a rolled score to the bottom part score.
    def add_bottom_score(self, value):
        self.__scoreboard["BOTTOM SCORE"] += value
        self.__bottom_score += value

    # Calculates all scores toghether
    def set_total_score(self):
        total_points = self.__top_bonus + self.__top_score + self.__bottom_score
        self.__total_score = total_points
        self.__scoreboard["TOTAL SCORE"] = total_points

    def get_top_score(self):
        return self.__top_score

    def get_top_bonus(self):
        return self.__top_bonus

    def get_bottom_score(self):
        return self.__bottom_score

    def get_total_score(self):
        return self.__total_score
    
    def get_id(self):
        return self.__id

    def get_username(self):
        return self.__username

    def __str__(self):
        return Person.__str__(self) + f', ID: {self.__id}, Username: {self.__username}'