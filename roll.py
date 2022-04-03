from dice import Dice

class Roll:
    def __init__(self):
        self.__current_dice_list = []
        self.__current_kept_dice = []

    # Roll dice.
    def roll_dice(self):
        self.__current_kept_dice.clear()

        dice = Dice()
        
        for dice in range(5):
            dice.roll()
            self.__current_dice_list.append(dice.get_dice_sideup())

        print (f'you rolled {self.__current_dice_list}! \n')
        return self.__current_dice_list








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

        from dice import Dice