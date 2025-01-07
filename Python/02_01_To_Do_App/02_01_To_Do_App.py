# Medium Difficulty Project
# To do list app
# Manage simple to-do list where users can add, remove, and view tasks. The tasks are saved into a text file.

def new_todo_file(path, file_name) :
    try :
        file_path = path + file_name
        new_file = open(file_path, 'w')
        return new_file
    except Exception as e :
        e_message = e.args
        return e_message


def new_task_to_file(path, file_name) :
    try :
        file_path = path + file_name
        f_write = open(file_path, 'a')

        task_name = input('enter task name : ')
        task_priority = input('enter task priority level (1 to 3) : ')
        task_status = input('enter task status (New, WIP, Ended) : ')

        new_task = task(task_name, task_priority, task_status)

        f_write.write(
            f'name : {new_task.get_task_name()} , '
            f'priority : {new_task.get_task_priority()} , '
            f'status : {new_task.get_task_status()} \n'
        )

        return new_task

    except Exception as er :
        er_message = er.args
        return er_message


def get_task_name_line(path, file_name, task_name) :
    try :
        task_name_line = 0
        file_path = path + file_name
        f_read = open(file_path, 'r')
        for line in f_read :
            task_name_line += 1
            if task_name in line :
                return task_name_line
    except Exception as error :
        error_message = error
        return error_message


def delete_task_line(path, file_name, task_line) :
    try :
        file_path = path + file_name
        with open(file_path, 'r') as file:
            lines = file.readlines()
        if int(task_line) <= len(lines):
            del lines[int(task_line)-1]

            with open(file_path, 'w') as file:
                for line in lines:
                    file.write(line)
        return task_line
    except Exception as error_ :
        error_message_ = error_
        return error_message_


class task :
    def __init__(self, task_name, task_priority, task_status) :
        self.task_name = task_name
        self.task_priority = task_priority
        self.task_status = task_status

    def get_task_name(self) :
        return self.task_name

    def get_task_priority(self) :
        return self.task_priority

    def get_task_status(self) :
        return self.task_status


try :

    user_choice = input('Do you want to create a new file, create new task, delete task or search task by name ? : ')

    if user_choice == 'new file' :
        new_path = input('Add a path for the file here : ') + '\\'
        new_file_name = input('What is the name of the new file ? : ') + '.txt'
        print(new_todo_file(new_path, new_file_name))
    elif user_choice == 'new task' :
        new_path = input('Add a path for the file here : ') + '\\'
        new_file_name = input('What is the name of the new file ? : ') + '.txt'
        print(f'new task added : {new_task_to_file(new_path, new_file_name).task_name} successfully')
    elif user_choice == 'search task by name' :
        new_path = input('Add a path for the file here : ') + '\\'
        new_file_name = input('What is the name of the new file ? : ') + '.txt'
        search_task_name = "name : " + input("Name of the task you're looking for ? : ") + " ,"
        print(f'the task is on line : {get_task_name_line(new_path, new_file_name, search_task_name)}')
    elif user_choice == 'delete task' :
        new_path = input('Add a path for the file here : ') + '\\'
        new_file_name = input('What is the name of the new file ? : ') + '.txt'
        delete_task_at = input("The line that you want to delete ? : ")
        line_deleted = delete_task_line(new_path, new_file_name, int(delete_task_at))
        print(f'the line {delete_task_at} was successfully removed')
    else :
        print("this action isn't valid")

except Exception as err :
    err_message = err.args
    print(err_message)
