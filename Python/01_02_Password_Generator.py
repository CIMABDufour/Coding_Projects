# Beginner Project
# A random password generator
# Create a random password for a user

import random


def generate_password(pass_len) :
    try :
        char_str = '1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*_-+'
        new_pass = ''
        for i in range(int(pass_len)) :
            char_len = len(char_str)
            rand_num = random.randint(0, char_len-1)
            get_char = char_str[rand_num]
            new_pass += get_char
        return new_pass

    except Exception as err_ :
        err_message_ = err_.args
        return err_message_


try:
    password_length = input('Enter password length : ')
    print(generate_password(password_length))
except Exception as err :
    err_message = err.args
    print(err_message)
