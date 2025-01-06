# Beginner Project
# Guess number game
# The user guess a number between a range define by the user

import random


def convert_number(i) :
    try :
        converted_number = int(i)
        return converted_number
    except Exception as err_ :
        err_message_ = err_.args
        return err_message_


try :
    user_range = input('Welcome to the num guessing game, choose the max number in range : ')
    user_input = input(f'choose a number between 1 and {user_range} : ')
    range_int = convert_number(user_range)
    num_guess = convert_number(user_input)
    rand_num = random.randint(1, range_int)
    if num_guess == rand_num :
        print(f'User : {user_input}, Computer : {rand_num} You win !')
    else :
        print(f'User : {user_input}, Computer : {rand_num} You lose, try again !')
except Exception as err :
    err_message = err.args
    print(err_message)
