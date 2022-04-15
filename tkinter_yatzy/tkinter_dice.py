import random

class Dice:
    def __init__(self):
        self.__sideup = 1

    def roll_dice(self):
        self.__sideup = random.randint(1, 6)
        
    def get_dice_sideup(self):
        return self.__sideup