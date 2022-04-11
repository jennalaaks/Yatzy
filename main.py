# Filename      main.py
# Authors:      Jenna Laaksovirta, Karolina Mäkinen ja Sanna Salminen
# Description:  Instruction, playing the game, player choose where to put dices and defining the winner.

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

def game(player_list):
    print()
    print("Players:")
    for player in player_list:
        print(player)

    dice = Roll()
    
    for i in range(15):
        for player in player_list:
            
            print()
            print(f'{player.get_name()}, your turn')
            player.print_scoreboard() 
            print()

            # first roll
            print(f"{player.get_name()} rolled:", dice.roll_five_times())
            keep1 = dice.keep_dice()
    
            # second roll
            print(f"Second roll:", dice.reroll_dice(keep1))
            keep2 = dice.keep_dice()

            # third roll
            roll3 = dice.reroll_dice(keep2)
            print(f"Third roll:", roll3)
            dice.forced_keep(roll3)

            print(f'Your final dices: {dice.get_kept_list()}')
            print()
            while True:
                try:
                    print("Where do you want to use your dices?")
                    user = int(input("Ones = 1, Twos = 2, Threes = 3, Fours = 4, Fives = 5, Sixes = 6\n"
                    "One pair = 7, Two pairs = 8, Three of a kind = 9, Four of a kind = 10, Full house = 11\n"
                    "Low straight = 12, High straight = 13, Chance = 14, Yatzy = 15: "))

                    if user == 1: 
                        if player.get_scoreboard()['Ones']: # Check is scoreboard ones empty, if it is then scores add to scoreboard.
                            ones = dice.check_ones(dice.get_kept_list())
                            player.add_rolled("Ones", ones)
                            player.add_top_score(ones)
                            break

                        else: # If user have already ones, then scores will be not added.
                            print('You already have ones.')

                    elif user == 2: 
                        twos = dice.check_twos(dice.get_kept_list())
                        player.add_rolled("Twos", twos)
                        player.add_top_score(twos)
                        break

                    elif user == 3: 
                        threes = dice.check_threes(dice.get_kept_list())
                        player.add_rolled("Threes", threes)
                        player.add_top_score(threes)
                        break

                    elif user == 4: 
                        fours = dice.check_fours(dice.get_kept_list())
                        player.add_rolled("Fours", fours)
                        player.add_top_score(fours)
                        break

                    elif user == 5: 
                        fives = dice.check_fives(dice.get_kept_list())
                        player.add_rolled("Fives", fives)
                        player.add_top_score(fives)
                        break

                    elif user == 6: 
                        sixes = dice.check_sixes(dice.get_kept_list())
                        player.add_rolled("Sixes", sixes)
                        player.add_top_score(sixes)
                        break

                    elif user == 7: 
                        one_pair = dice.check_one_pair(dice.get_kept_list())
                        player.add_rolled("One pair", one_pair)
                        player.add_bottom_score(one_pair)
                        break

                    elif user == 8: 
                        two_pairs = dice.check_two_pairs(dice.get_kept_list())
                        player.add_rolled("Two pairs", two_pairs)
                        player.add_bottom_score(two_pairs)
                        break

                    elif user == 9:
                        three_kind = dice.check_three_kind(dice.get_kept_list())
                        player.add_rolled("Three of a kind", three_kind)
                        player.add_bottom_score(three_kind)
                        break

                    elif user == 10:
                        four_kind = dice.check_four_kind(dice.get_kept_list())
                        player.add_rolled("Four of a kind", four_kind)
                        player.add_bottom_score(four_kind)
                        break

                    elif user == 11: 
                        full_house = dice.check_full_house(dice.get_kept_list())
                        player.add_rolled("Full house", full_house)
                        player.add_bottom_score(full_house)
                        break

                    elif user == 12:
                        low_straight = dice.check_low_straight(dice.get_kept_list())
                        player.add_rolled("Low straight", low_straight)
                        player.add_bottom_score(low_straight)
                        break

                    elif user == 13:
                        high_straight = dice.check_high_straight(dice.get_kept_list())
                        player.add_rolled("High straight", high_straight)
                        player.add_bottom_score(high_straight)
                        break

                    elif user == 14:
                        chance = dice.check_chance(dice.get_kept_list())
                        player.add_rolled("Chance", chance)
                        player.add_bottom_score(chance)
                        break
                
                    elif user == 15:
                        yatzy = dice.check_yatzy(dice.get_kept_list())
                        player.add_rolled("Yatzy", yatzy)
                        player.add_bottom_score(yatzy)
                        break

                    else:
                        print("Integers between 1 to 15")
                   
                except ValueError:
                    print("Integers only. Please answer 1 - 15.")

    player.add_top_bonus()
    player.set_total_score()

    print()
    for player in player_list:
        player.print_scoreboard()

def winner(player_list):
    total_points = 0
    winner = ''
    for player in player_list:
        if player.get_total_score() > total_points:
            total_points = player.get_total_score()
            winner = player.get_name()
        print(f"{player.get_name()}'s total score:",total_points)

    print('Winner is',winner)


def main():

    print("Let's play Yatzy!")
        
    if choice() == 1:
        try: 
            file = open("instructions.txt", "r", encoding="utf8")
            print()
            print(file.read())
        except FileNotFoundError:
            print("File not found.")

    player_list = [ Player('Sanna', 38, 'sannas861', 1) ]

    game(player_list)

    winner(player_list)

    
main()