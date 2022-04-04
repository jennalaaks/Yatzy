# Filename      dice.py
# Authors:      Jenna Laaksovirta, Karolina Mäkinen ja Sanna Salminen
# Description:  

# Import classes
from dice import Dice # Dice
from roll import Roll # Roll
from player import Player # Player

def choice():
    while True:
        try:
            choice = int(input("Do you want to read the instructions before we start? yes = 1, no = 2: "))
            if choice == 1:
                return choice
            elif choice == 2:
                return choice
            else:
                print("Please answer 1 or 2.")
        except ValueError:
            print("Integers only. Please answer 1 or 2.")
   

def main():

    print("Let's play Yatzy!")
        
    if choice() == 1:
        try: 
            file = open("instructions.txt", "r", encoding="utf8")
            print(file.read())
        except FileNotFoundError:
            print("File not found.")

    player1 = Player('Sanna', 15, 'sannas861', 1)
    player2 = Player('Jenna', 23, 'jenna123', 2)

    print("First player: ")
    print(player1)
    print()
    print("Second player:")
    print(player2)

    dice1 = Roll()
    dice2 = Roll()


    for i in range (6):
        # first roll:
        print()
        print(f'{player1.get_name()}, your turn')
        player1.print_scoreboard() 
        print()

        dice1.roll_five_times()
        keep1 = dice1.keep_dice()
    
        # second roll
        dice1.reroll_dice(keep1)
        keep2 = dice1.keep_dice()

        # third roll
        roll3 = dice1.reroll_dice(keep2)
        dice1.forced_keep(roll3)

        print(f'Your final dices: {dice1.get_kept_list()}')
        print()

        print("Where do you want to use your dices?")
        user = int(input("Ones = 1, Twos = 2, Threes = 3, Fours = 4, Fives = 5, Sixes = 6: "))
        #"1 pair = 7, 2 pairs = 8, 3 of a kind = 9, 4 of a kind = 10, Full House = 11\n"
        #"Low Straight = 12, High Straight = 13, Yatzy = 14, Chance = 15: "))
        if user == 1: 
            player1.add_rolled("Ones", dice1.check_ones(dice1.get_kept_list()))
            player1.add_top_score(dice1.check_ones(dice1.get_kept_list()))
        elif user == 2: 
            player1.add_rolled("Twos", dice1.check_twos(dice1.get_kept_list()))
            player1.add_top_score(dice1.check_twos(dice1.get_kept_list()))
        elif user == 3: 
            player1.add_rolled("Threes", dice1.check_threes(dice1.get_kept_list()))
            player1.add_top_score(dice1.check_threes(dice1.get_kept_list()))
        elif user == 4: 
            player1.add_rolled("Fours", dice1.check_fours(dice1.get_kept_list()))
            player1.add_top_score(dice1.check_fours(dice1.get_kept_list()))
        elif user == 5: 
            player1.add_rolled("Fives", dice1.check_fives(dice1.get_kept_list()))
            player1.add_top_score(dice1.check_fives(dice1.get_kept_list()))
        elif user == 6: 
            player1.add_rolled("Sixes", dice1.check_sixes(dice1.get_kept_list()))
            player1.add_top_score(dice1.check_sixes(dice1.get_kept_list()))

        # first roll:
        print()
        print(f'{player2.get_name()}, your turn')
        player2.print_scoreboard() 
        print()

        dice2.roll_five_times()
        keep1 = dice2.keep_dice()
    
        # second roll
        dice2.reroll_dice(keep1)
        keep2 = dice2.keep_dice()

        # third roll
        roll3 = dice2.reroll_dice(keep2)
        dice2.forced_keep(roll3)

        print(f'Your final dices: {dice2.get_kept_list()}')
        print()

        print("Where do you want to use your dices?")
        user = int(input("Ones = 1, Twos = 2, Threes = 3, Fours = 4, Fives = 5, Sixes = 6: "))
        #"1 pair = 7, 2 pairs = 8, 3 of a kind = 9, 4 of a kind = 10, Full House = 11\n"
        #"Low Straight = 12, High Straight = 13, Yatzy = 14, Chance = 15: "))
        if user == 1: 
            player2.add_rolled("Ones", dice2.check_ones(dice2.get_kept_list()))
            player2.add_top_score(dice2.check_ones(dice2.get_kept_list()))
        elif user == 2: 
            player2.add_rolled("Twos", dice2.check_twos(dice2.get_kept_list()))
            player2.add_top_score(dice2.check_twos(dice2.get_kept_list()))
        elif user == 3: 
            player2.add_rolled("Threes", dice2.check_threes(dice2.get_kept_list()))
            player2.add_top_score(dice2.check_threes(dice2.get_kept_list()))
        elif user == 4: 
            player2.add_rolled("Fours", dice2.check_fours(dice2.get_kept_list()))
            player1.add_top_score(dice2.check_fours(dice2.get_kept_list()))
        elif user == 5: 
            player2.add_rolled("Fives", dice2.check_fives(dice2.get_kept_list()))
            player2.add_top_score(dice2.check_fives(dice2.get_kept_list()))
        elif user == 6: 
            player2.add_rolled("Sixes", dice2.check_sixes(dice2.get_kept_list()))
            player2.add_top_score(dice2.check_sixes(dice2.get_kept_list()))
        

    player1.add_top_bonus()
    player2.add_top_bonus()
    print()
    print("After the top bonus checking:")
    print()
    player1.print_scoreboard()
    print()
    player2.print_scoreboard()

    
    
main()