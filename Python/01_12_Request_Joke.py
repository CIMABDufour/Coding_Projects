# Beginner Project
# Get a joke from API
# Build a simple program that fetches jokes.

import requests


def save_joke_to_file(joke):
    try:
        filepath = input('Save file to ? : ')
        name = input('name of the text file ? : ') + '.txt'
        full_path = f'{filepath}\\{name}'
        new_file = open(full_path, 'w')
        new_file.write(joke)
        return 'file successfully saved'
    except Exception as err:
        error_message = err.args
        return error_message


def get_a_joke():
    try:
        type_list = ['general', 'knock-knock', 'programming', 'dad']
        user_type_input = input('general,knock-knock,programming,dad type of joke ? : ')
        if user_type_input not in type_list:
            error_input = "this type of joke isn't valid"
            return error_input
        else:
            new_url = f'https://official-joke-api.appspot.com/jokes/{user_type_input}/random'
            new_request = requests.get(new_url)
            joke_json = new_request.json()
            setup = joke_json[0]['setup']
            punchline = joke_json[0]['punchline']
            full_joke = f'{setup}\n{punchline}'
            return full_joke

    except Exception as err:
        error_message = err.args
        return error_message


get_a_new_joke = get_a_joke()

print(get_a_new_joke)

save_to_file_input = input('Do you want to save this joke for later ? : ')

if save_to_file_input == 'yes':
    print(save_joke_to_file(get_a_new_joke))
else:
    print('have a nice day!')
