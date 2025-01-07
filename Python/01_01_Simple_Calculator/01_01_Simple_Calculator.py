# Beginner Project
# Simple Calculator Program
# Let the user calculate from the terminal with different operation +,-,*,/

def convert_number(i) :
    try :
        converted_number = int(i)
        return converted_number
    except Exception as err_ :
        err_message_ = err_.args
        return err_message_


def operation_choosen(num_one, num_two, ope) :
    try :
        if ope == '+' :
            return num_one + num_two
        elif ope == '-' :
            return num_one - num_two
        elif ope == '*' :
            return num_one * num_two
        elif ope == '/' :
            return num_one / num_two
        else :
            err_message__ = 'the operator isnt valid'
            return err_message__
    except Exception as err__ :
        err_message__ = err__.args
        return err_message__


try :
    first_number = input('add your first number : ')
    operator = input('choose your operation +, -, *, / : ')
    second_number = input('add your second number : ')

    int_first = convert_number(first_number)
    int_second = convert_number(second_number)
    result = operation_choosen(int_first, int_second, operator)
    print(f'The result is : {result}')

except Exception as err :

    err_message = err.args
    print(err_message)
