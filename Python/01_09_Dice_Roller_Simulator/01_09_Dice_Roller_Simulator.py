# Beginner Project
# Dice Roller Simulator
# Roll one or multiple dice.

import random
import time


class Dice:
    def __init__(self, side, rolled):
        self.side = side
        self.rolled = rolled

    def roll_dice(self):
        print('the dice got yeeted')
        count = 3
        while count > 0:
            print(count)
            time.sleep(1)
            count -= 1
        num_list = range(1, self.side + 1)
        get_num = random.choice(num_list)
        self.rolled = True
        return get_num

    def is_dice_rolled(self):
        return self.rolled

    def how_many_side(self):
        return self.side


new_dice = Dice(6, False)
print(f'the dice landed on a : {new_dice.roll_dice()}')
