# Medium Difficulty Project
# Simple Expense Tracking
# Tracking of expenses from a person buying stuff.

def new_expense_file(file_path, file_name) :
    try :
        full_path = file_path + file_name+'.txt'
        new_file = open(full_path, 'w')
        return new_file
    except Exception as e :
        e_message = e.args
        return e_message


def add_expense_to_file(file_path, file_name, categ, cost_) :
    try :
        full_path = file_path + file_name
        get_file = open(full_path, 'a')
        new_expense = expense(categ, cost_)
        get_file.writelines(f'{new_expense.expense_category},{new_expense.expense_total} \n')
        return new_expense

    except Exception as e :
        e_message = e.args
        return e_message


def get_total_expense(file_path, file_name) :
    try :
        total = 0
        new_text = []
        full_path = file_path + file_name
        get_file = open(full_path, 'r')
        lines = get_file.readlines()
        for line in lines :
            get_cost = line.removeprefix(line[0] + ',')
            new_text.append(float(get_cost))
            total = sum(new_text)
        return total
    except Exception as e :
        e_message = e.args
        return e_message


def get_most_cat_expense(file_path, file_name) :
    try :
        cat_one = 0
        cat_two = 0
        cat_three = 0
        full_path = file_path + file_name
        get_file = open(full_path, 'r')
        lines = get_file.readlines()
        for line in lines :
            if line.startswith('1') :
                cat_one += 1
            if line.startswith('2') :
                cat_two += 1
            if line.startswith('3') :
                cat_three += 1

        if cat_one > cat_two and cat_one > cat_three :
            return ['Insurance', cat_one]
        if cat_two > cat_one and cat_two > cat_three :
            return ['Rent', cat_two]
        if cat_three > cat_one and cat_three > cat_two :
            return ['Business fees', cat_three]

    except Exception as e :
        e_message = e.args
        return e_message


class expense :
    def __init__(self, expense_category, expense_total) :
        self.expense_category = expense_category
        self.expense_total = expense_total


category_type = {'Insurance' : 1, 'Rent' : 2, 'Business fees' : 3}

user_input = input('what do you want to do ? : ')

if user_input == 'create file' :
    try :
        path = 'C:\\Users\\BenBi\\OneDrive\\Desktop\\'
        name = input('file name ? : ')
        expense_file = new_expense_file(path, name)
        print('New file created successfully')
    except Exception as error :
        error_message = error.args
        print(error_message)

elif user_input == 'add new expense' :
    try :
        path = 'C:\\Users\\BenBi\\OneDrive\\Desktop\\'
        name = input('file name ? : ')
        cat = input(f'cat value ? : ')
        cost = input('total of expense ? : ')
        add_expense = add_expense_to_file(path, name, cat, cost)
        print('New expenses successfully added')

    except Exception as error :
        error_message = error.args
        print(error_message)

elif user_input == 'get cat most expense' :
    try :
        path = 'C:\\Users\\BenBi\\OneDrive\\Desktop\\'
        name = input('file name ? : ')
        cat_expense = get_most_cat_expense(path, name)
        print(f'the category having the most expenses is : {cat_expense[0]} with a total of {cat_expense[1]} expenses')
    except Exception as error :
        error_message = error.args
        print(error_message)

elif user_input == 'get total expenses' :
    try :
        path = 'C:\\Users\\BenBi\\OneDrive\\Desktop\\'
        name = input('file name ? : ')
        total_expenses = get_total_expense(path, name)
        print(f'the total expenses is : {total_expenses}')
    except Exception as error :
        error_message = error.args
        print(error_message)

else :
    print("this action isn't valid")
