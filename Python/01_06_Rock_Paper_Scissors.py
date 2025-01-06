# Beginner Project
# Rock Paper Scissors game with the computer
# Choose between the option of rock paper and scissors

import random


def win_comb(user_choice, comp_choice) :
    winning_combinations = [
        ('rock', 'scissors'),
        ('paper', 'rock'),
        ('scissors', 'paper')
    ]
    if user_choice == comp_choice :
        return f"User Input: {user_choice}, Computer Input: {comp_choice}. It's a draw!"
    elif (user_choice, comp_choice) in winning_combinations :
        return f"User Input: {user_choice}, Computer Input: {comp_choice}. You win!"
    else :
        return f"User Input: {user_choice}, Computer Input: {comp_choice}. Computer wins!"


def gameplay() :
    try :
        choices = ['rock', 'paper', 'scissors']
        while True :
            user_input = input("Choose between Rock, Paper, and Scissors (or type 'exit' to quit): ").strip().lower()
            if user_input == 'exit' :
                print("Thanks for playing! Goodbye!")
                break
            elif user_input not in choices :
                print("Invalid choice. Please select Rock, Paper, or Scissors.")
                continue

            comp_choice = random.choice(choices)
            result = win_comb(user_input, comp_choice)
            print(result)

    except Exception as error :
        error_message = error.args
        return error_message


new_game = gameplay()
