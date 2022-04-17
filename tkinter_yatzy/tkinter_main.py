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
                    dice1.configure(bg='lightgrey')
                else:
                    dice1.configure(bg='pink')
            
            def hold_dice2():
                if dice2['bg'] == 'pink':
                    dice2.configure(bg='lightgrey')
                else:
                    dice2.configure(bg='pink')
    
            def hold_dice3():
                if dice3['bg'] == 'pink':
                    dice3.configure(bg='lightgrey')
                else:
                    dice3.configure(bg="pink")

            def hold_dice4():
                if dice4['bg'] == 'pink':
                    dice4.configure(bg='lightgrey')
                else:
                    dice4.configure(bg="pink")
                
            def hold_dice5():
                if dice5['bg'] == 'pink':
                    dice5.configure(bg='lightgrey')
                else:
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

    player_list = [Player('Jespa', 3, 'jenspeliini12', 1), Player('Teppo', 56, 'teppo23', 2)]

    '''while True:
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

        player_list.append(Player(name, age, username, pl_id))'''

    game(player_list)

    #winner(player_list)

    
main()