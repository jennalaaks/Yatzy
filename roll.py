# Filename      roll.py
# Authors:      Jenna Laaksovirta, Karolina Mäkinen ja Sanna Salminen
# Description:  Rolls the dices, which dices are going to be kept and which rolled again. Counts points and checks ...

from dice import Dice

class Roll:
    def __init__(self):
        self.__current_dice_list = []
        self.__current_kept_dice = []

    # Rolls the five dices at once
    def roll_five_times(self):
        self.__current_dice_list.clear()
        self.__current_kept_dice.clear()
        for i in range(5):
            dice = Dice()
            dice.roll_dice()
            value = dice.get_dice_sideup()
            self.__current_dice_list.append(value)
        return self.__current_dice_list

    # User chooses if she/he wants to keep dice or dices
    def keep_dice(self):
        while True: 
            try:
                keep = input('Which dice you want to keep? (separated by comma): ')
                split = keep.split(',')
                if keep == '':
                    return self.__current_dice_list
            
                split_int = [int(item) for item in split]
                for i in split_int:
                    if i == int:
                        split_int.append(int(i))
                break        
            except ValueError:
                print("Please enter only integers separated by comma")
            
        kept_list = [] 
        
        # Kept dices added to a list
        for dice in split_int:
            kept_list.append(dice)

        for dice in kept_list:
            kept_dice = kept_list.count(dice) #Counts kept dices
            dices = self.__current_dice_list.count(dice) #Counts current dices
            if kept_dice > dices: #If kept dices are bigger current dices
                for i in range(kept_dice - dices): #Removes kept dices from current dices?
                    kept_list.remove(dice) #Removes dices in kept_list so the list is empty for next round
            
        self.__current_kept_dice += kept_list # Adds current dices to kept_list

        for value in split_int:
            if value in self.__current_dice_list:
                self.__current_dice_list.remove(value)

        return self.__current_dice_list

    # Rolls all or the dices that are not kept again
    def reroll_dice(self, dice_list):
        rerolled = []
        for count in range(len(dice_list)):
            dice = Dice()
            dice.roll_dice()
            value = dice.get_dice_sideup()
            rerolled.append(value)
        self.__current_dice_list = rerolled
        return self.__current_dice_list

    def get_dice_list(self):
        return self.__current_dice_list

    def get_kept_list(self):
        return self.__current_kept_dice
    
    # If player has not chosen to keep any dices before the last roll
    def forced_keep(self, dice_list):
        for dice in dice_list:
            self.__current_kept_dice.append(dice)

    # HERE ARE ALL METHODS THAT CHECKS ALL DIFFERENT COMBINATIONS

    def check_ones(self, dice_list):
        ones = 0
        for dice in dice_list:
            if dice == 1:
                ones += 1
        return ones

    def check_twos(self, dice_list):
        twos = 0
        for dice in dice_list:
            if dice == 2:
                twos += 2
        return twos

    def check_threes(self, dice_list):
        threes = 0
        for dice in dice_list:
            if dice == 3:
                threes += 3
        return threes

    def check_fours(self, dice_list):
        fours = 0
        for dice in dice_list:
            if dice == 4:
                fours += 4
        return fours
    
    def check_fives(self, dice_list):
        fives = 0
        for dice in dice_list:
            if dice == 5:
                fives += 5
        return fives
    
    def check_sixes(self, dice_list):
        sixes = 0
        for dice in dice_list:
            if dice == 6:
                sixes += 6
        return sixes
    
    def check_one_pair(self, dice_list):
        dice_list.sort()
        sum = 0
        for dice in dice_list:
            if dice_list.count(dice) >= 2:
                sum = dice * 2
        return sum

    def check_two_pairs(self, dice_list):
        dice_list.sort()
        if (dice_list[0] == dice_list[1] and dice_list[2] == dice_list[3]):
            return dice_list[0] + dice_list[1] + dice_list[2] + dice_list[3]
        if (dice_list[0] == dice_list[1] and dice_list[3] == dice_list[4]):
            return dice_list[0] + dice_list[1] +  dice_list[3] + dice_list[4]
        if (dice_list[1] == dice_list[2] and dice_list[3] == dice_list[4]):
            return dice_list[1] + dice_list[2] + dice_list[3] + dice_list[4]

    def check_three_kind(self, dice_list):
        dice_list.sort()
        dice = dice_list[2]
        if dice_list[0] == dice_list[2] or dice_list[1] == dice_list[3] or dice_list[2] == dice_list[4]:
            return dice * 3
        else:
            print("It was not Three of a kind")
            return 0

    def check_four_kind(self, dice_list):
        dice_list.sort()
        dice = dice_list[2]
        if dice_list[0] == dice_list[3] or dice_list[1] == dice_list[4]:
            return dice * 4
        else:
            print("It was not Full House")
            return 0
            
    def check_full_house(self,dice_list):
        dice_list.sort()
        fullhouse = 0
        if (len(set(dice_list))) != 2:
            print('It was not Full House')
            return 0

        elif (dice_list[0] != dice_list[3]) or (dice_list[1] != dice_list[4]):
            for dice in dice_list:
                fullhouse += dice
            return fullhouse
            
    def check_low_straight(self, dice_list):
        dice_list.sort()
        if len(set(dice_list)) == 5 and dice_list[0] == 1 and dice_list[4] == 5:
            return 15
        else:
            print("It was not Low straight")
            return 0

    def check_high_straight(self, dice_list):
        dice_list.sort()
        if len(set(dice_list)) == 5 and dice_list[0] == 2 and dice_list[4] == 6:
            return 20
        else:
            print("It was not High straight")
            return 0
        
    def check_chance(self, dice_list):
        sum = 0
        for dice in dice_list:
            sum += dice
        return sum

    def check_yatzy(self, dice_list):
        yatzy = all(element == dice_list[0] for element in dice_list)
        if (yatzy):
            return 50
        else: 
            print('It was not Yatzy')
            return 0