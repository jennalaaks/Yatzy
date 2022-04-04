from dice import Dice

class Roll:
    def __init__(self):
        self.__current_dice_list = []
        self.__current_kept_dice = []

    def roll_five_times(self):
        self.__current_dice_list.clear()
        self.__current_kept_dice.clear()
        for i in range(5):
            dice = Dice()
            dice.roll_dice(6)
            value = dice.get_value()
            self.__current_dice_list.append(value)
        print(f'You rolled: {self.__current_dice_list}')

    def keep_dice(self):
        keep = input('Which dice you want to keep? (separated by comma): ')
        split = keep.split(',')

        if keep == '':
            return self.__current_dice_list

        split_int = [int(item) for item in split]

        for dice in split_int:
            self.__current_kept_dice.append(dice)

        for value in split_int:
            if value in self.__current_dice_list:
                self.__current_dice_list.remove(value)

        return self.__current_dice_list

    def reroll_dice(self, dice_list):
        rerolled = []
        for count in range(len(dice_list)):
            dice = Dice()
            dice.roll_dice(6)
            value = dice.get_value()
            rerolled.append(value)
        self.__current_dice_list = rerolled
        print(f'You rolled: {self.__current_dice_list}')

        return self.__current_dice_list

    def get_dice_list(self):
        return self.__current_dice_list

    def get_kept_list(self):
        return self.__current_kept_dice
    
    def forced_keep(self, dice_list):
        for dice in dice_list:
            self.__current_kept_dice.append(dice)


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
        pass

    def check_two_pairs(self, dice_list):
        pass

    def check_three_kind(self, dice_list):
        pass

    def check_four_kind(self, dice_list):
        pass

    def check_low_straight(self, dice_list):
        pass

    def check_high_straight(self, dice_list):
        pass

    def check_full_house(self,dice_list):
        pass

    def add_chance(self, dice_list):
        pass

    def check_yatzy(self, dice_list):
        if len(set(dice_list)) == 1:
            return True
        return False
