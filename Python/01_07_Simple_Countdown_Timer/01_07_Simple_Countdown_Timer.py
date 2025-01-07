# Beginner Project
# Simple Countdown Timer
# Add seconds to countdown in terminal

import time

def countdown() :
    try :

        user_input = input('How many seconds do you want ? : ')
        seconds = int(user_input)
        while seconds > 0 :
            print(seconds)
            time.sleep(1)
            seconds -= 1
        print("Time's up!")
    except Exception as error :
        error_message = error.args
        return error_message


new_countdown = countdown()
