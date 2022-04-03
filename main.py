# Filename      dice.py
# Authors:      Jenna Laaksovirta, Karolina Mäkinen ja Sanna Salmi
# Description:  

# Import classes
from dice import Dice # Dice
from roll import Roll # Roll
from player import Player # Player


def main():

    # Defining what we work with on the top part of the game.
    game_list_top = ['aces' , 'twos' , 'threes' , 'fours' , 'fives' , 'sixes']
    game_list_top_values = [1,2,3,4,5,6]

    dice1 = Roll()
    
    player1 = Player('Sanna', 15, 'sannas861', 1)

    # first roll:
    dice1.roll_dice()
    keep1 = dice1.keep_dice()
    
main()