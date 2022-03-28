# Filename      dice.py
# Authors:      Jenna Laaksovirta, Karolina Mäkinen ja Sanna Salmi
# Description:  Dice

import random

class Dice:
    def __init__(self):
        self.__sideup = 1

    def roll_the_dice(self):
        self.__sideup = random.randint(1, 6)
        
    def get_dice_sideup(self):
        return self.__sideup