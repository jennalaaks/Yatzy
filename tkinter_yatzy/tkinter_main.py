# Filename      dice.py
# Authors:      Jenna Laaksovirta, Karolina Mäkinen ja Sanna Salminen
# Description:  

# Import classes

from tkinter_roll import Roll # Roll
from tkinter_player import Player # Player
from tkinter import *
import random



def game(player_list):

    dice = Roll()

    # creating tkinter window
    root = Tk()
    root.title('Yatzy')
    root.geometry('900x600')

    root.counter = 0

    # creating the player names to scoreboard
    i = 0
    for player in player_list:
        i += 1
        name = Label(root, text=player.get_name(), width=10)
        name.grid(row=0, column=i)

    # creating the cells
    for r in range(1, 20):
      for c in range(1, 6):
        cell = Label(root, bg='white', width=10, borderwidth=1, relief='raised')
        cell.grid(row=r, column=c)

    # creating player info
    l = Label(root, text= 'Players')
    l.grid(row=0, column=10, columnspan=5)
    i = 0
    for player in player_list:
        i += 1
        t1 = Label(root, text = player,width=45, borderwidth=2, relief='groove')
        t1.grid(row=i, column=10, columnspan= 5, sticky= 'e')

    # function to open the rules file to new window
    def open_new_window():
        new = Toplevel(root)
        new.title("Yatzy Rules")
        new.geometry("600x600")
        my_text = Text(new, width=550, height=550, font=("Helvetica", 10))
        my_text.pack(pady=10)

        file = open("instructions.txt", "r", encoding="utf8")
        stuff = file.read()
        my_text.insert(END, stuff)
        file.close()

        new.mainloop()

    # button for rules
    btn = Button(root, text="Click for rules",width= 20, height = 2, bg='lightyellow', command = open_new_window)
    btn.grid(row= 21,rowspan=2, column=2, columnspan=2)


    t2 = Label(root, text = '', height= 4, width= 45, borderwidth=2, relief='groove')
    t2.grid(row=7, rowspan=4, column=10, columnspan=5, sticky='e')


    for i in range(15):

        for player in player_list:

            btn.configure(state='normal')
            t2.configure(text=player.get_name() +", your turn")

            def place_ones():
                ones = dice.check_ones(dice_numbers)
                cell1 = Label(root, text= ones, bg='white', width=10, borderwidth=1, relief='raised')
                cell1.grid(row=1, column=i+1)
                player.add_top_score(ones)
                btn.configure(state='normal')
                t2.configure(text=player.get_name() +", your turn")
                for die in dice_list:
                    die.configure(bg='lightgrey')
                root.counter = 0
                

            # creating scoreboard buttons and labels
            Button(root, text='Ones', command= place_ones).grid(row=1, column=0, sticky='ew')
            Button(root, text='Twos').grid(row=2, column=0, sticky='ew')
            Button(root, text='Threes').grid(row=3, column=0, sticky='ew')
            Button(root, text='Fours').grid(row=4, column=0, sticky='ew')
            Button(root, text='Fives').grid(row=5, column=0, sticky='ew')
            Button(root, text='Sixes').grid(row=6, column=0, sticky='ew')
            Label(root, text='TOP SCORE', borderwidth=1, relief='raised').grid(row=7, column=0, pady=5, sticky='ew')
            Label(root, text='TOP BONUS', borderwidth=1, relief='raised').grid(row=8, column=0, pady=5, sticky='ew')
            Button(root, text='One pair').grid(row=9, column=0, sticky='ew')
            Button(root, text='Two pairs').grid(row=10, column=0, sticky='ew')
            Button(root, text='Three of a kind').grid(row=11, column=0, sticky='ew')
            Button(root, text='Four of a kind').grid(row=12, column=0, sticky='ew')
            Button(root, text='Full house').grid(row=13, column=0, sticky='ew')
            Button(root, text='Low straight').grid(row=14, column=0, sticky='ew')
            Button(root, text='High straight').grid(row=15, column=0, sticky='ew')
            Button(root, text='Chance').grid(row=16, column=0, sticky='ew')
            Button(root, text='Yatzy').grid(row=17, column=0, sticky='ew')
            Label(root, text='BOTTOM SCORE', borderwidth=1, relief='raised').grid(row=18, column=0, pady=5,  sticky='ew')
            Label(root, text='TOTAL SCORE', borderwidth=1, relief='raised').grid(row=19, column=0, pady=5, sticky='ew')


            # dice labels
            dice1 = Label(root, text="",font=("times", 50))
            dice2 = Label(root, text="",font=("times", 50))
            dice3 = Label(root, text="",font=("times", 50))
            dice4 = Label(root, text="",font=("times", 50))
            dice5 = Label(root, text="",font=("times", 50))
        
            dice_list = [dice1, dice2, dice3, dice4, dice5]

            dice_numbers = []
            
            def hold_dice1():
                if dice1['bg'] == 'pink':
                    dice1.configure(bg='white')
                dice1.configure(bg='pink')
            
            def hold_dice2():
                if dice2['bg'] == 'pink':
                    dice2.configure(bg='white')
                dice2.configure(bg='pink')
    
            def hold_dice3():
                if dice3['bg'] == 'pink':
                    dice3.configure(bg='white')
                dice3.configure(bg="pink")

            def hold_dice4():
                if dice4['bg'] == 'pink':
                    dice4.configure(bg='white')
                dice4.configure(bg="pink")
                
            def hold_dice5():
                if dice5['bg'] == 'pink':
                    dice5.configure(bg='white')
                dice5.configure(bg="pink")
                
            #dice number buttons
            d1_button = Button(root, text="", command= hold_dice1)
            d2_button = Button(root, text="", command= hold_dice2)
            d3_button = Button(root, text="", command= hold_dice3)
            d4_button = Button(root, text="", command= hold_dice4)
            d5_button = Button(root, text="", command= hold_dice5)

            button_list = [d1_button, d2_button, d3_button, d4_button, d5_button]

            def roll():

                root.counter += 1

                #define list of dice unicodes
                dice_codes = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']

                # define dict with key as unicodes and value as number
                numbers = {'\u2680':1,'\u2681':2,
                           '\u2682':3,'\u2683':4,
                           '\u2684':5,'\u2685':6}

                for dice in dice_list:

                    if dice == dice1:
                        if dice['bg'] != 'pink':
                            # roll dice randomly
                            d1 = random.choice(dice_codes)
                            # configure dice labels
                            dice1.configure(text=d1)
                            if d1 in numbers.keys():
                                #return rolled dice number
                                d1_number = numbers[d1]
                             # configure dice number buttons
                            d1_button.configure(text=d1_number)

                    if dice == dice2:
                        if dice['bg'] != 'pink':
                            d2 = random.choice(dice_codes)
                            dice2.configure(text=d2)
                            if d2 in numbers.keys():
                                d2_number = numbers[d2]
                            d2_button.configure(text=d2_number)

                    if dice == dice3:
                        if dice['bg'] != 'pink':
                            d3 = random.choice(dice_codes)
                            dice3.configure(text=d3)
                            if d3 in numbers.keys():
                                d3_number = numbers[d3]
                            d3_button.configure(text=d3_number)

                    if dice == dice4:
                        if dice['bg'] != 'pink':
                            d4 = random.choice(dice_codes)
                            dice4.configure(text=d4)
                            if d4 in numbers.keys():
                                d4_number = numbers[d4]
                            d4_button.configure(text=d4_number)

                    if dice == dice5:
                        if dice['bg'] != 'pink':
                            d5 = random.choice(dice_codes)
                            dice5.configure(text=d5)
                            if d5 in numbers.keys():
                                d5_number = numbers[d5]
                            d5_button.configure(text=d5_number)

                    # after third roll the numbers are added to the dice_numbers list
                    if root.counter == 3:
                        btn.configure(state='disabled')
                        dice_numbers.append(numbers[dice['text']])
                        t2.configure(text=player.get_name() +" where do you want to use your dices?\nChoose from the scoreboard.")

                    dice1.grid(row=13, rowspan=3, column=10)
                    dice2.grid(row=13, rowspan=3, column=11)
                    dice3.grid(row=13, rowspan=3, column=12)
                    dice4.grid(row=13, rowspan=3, column=13)
                    dice5.grid(row=13, rowspan=3, column=14)

                    d1_button.grid(row=16, column=10)
                    d2_button.grid(row=16, column=11)
                    d3_button.grid(row=16, column=12)
                    d4_button.grid(row=16, column=13)
                    d5_button.grid(row=16, column=14)

                
            btn = Button(root, width=20, height=2, bg='lightyellow', text="Roll Dice", command= roll)
            btn.grid(row= 10, rowspan=3, column=10, columnspan=5)

        
            root.mainloop()

            print('dice numbers: ', dice_numbers)

            print(root.counter)
            """
            while True:
                try:
                    print("Where do you want to use your dices?")
                    user = int(input("Ones = 1, Twos = 2, Threes = 3, Fours = 4, Fives = 5, Sixes = 6\n"
                    "One pair = 7, Two pairs = 8, Three of a kind = 9, Four of a kind = 10, Full house = 11\n"
                    "Low straight = 12, High straight = 13, Chance = 14, Yatzy = 15: "))

                    if user == 1: 
                        ones = dice.check_ones(dice.get_kept_list())
                        player.add_rolled("Ones", ones)
                        player.add_top_score(ones)
                        num = Label(root, text=ones)
                        num.grid(row=1, column=player_list.index(player))
                        
                        
                        break

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
                """
            
            

    """
    player.add_top_bonus()
    player.set_total_score()

    print()
    for player in player_list:
        player.print_scoreboard()
    """
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

    print("Welcome to play Yatzy!")

    while True:
        try:
            player_amount = int(input("How many players you want to have? (min = 2, max = 5): "))
            if player_amount >= 2 and player_amount <= 5:
                break
            else:
                print('You need to enter 2 - 5')

        except ValueError:
            print("Only integers between 2 to 5.")

    player_list = []

    for i in range(player_amount):
        print()
        name = input(f'Player {i+1} name: ')
        age = int(input(f'Player {i+1} age: '))
        username = input(f'Player {i+1} user name: ')
        pl_id = int(input(f'Player {i+1} id: '))

        player_list.append(Player(name, age, username, pl_id))

    game(player_list)

    #winner(player_list)

    
main()