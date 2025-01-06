# Beginner Project
# Dice Roller Simulator
# Roll one or multiple dice.

import random
import time


class Dice :
    def __init__(self, side, rolled) :
        self.side = side
        self.rolled = rolled

    def roll_dice(self) :
        self.rolled = True
        return self

    def dice_side(self) :
        user_input = input('how many side does your dice have ? : ')
        self.side = int(user_input)
        return self

    def is_dice_rolled(self) :
        return self.rolled

    def how_many_side(self) :
        return self.side


new_dice = Dice(6, False)
new_dice.roll_dice()
print(new_dice.how_many_side())
