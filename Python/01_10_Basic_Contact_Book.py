# Beginner Project
# Basic Contact Book.
# Add, Search, Delete or view all contact available

book_contact = [] # Big ... Avoid Global Variables big 
# Instead of a global book_contact, encapsulate it inside a class or pass it as an argument to functions.


class Contact:
    def __init__(self, fname, lname, number):
        self.fname = fname
        self.lname = lname
        self.number = number

    def add_new_contact(self):
        new_contact = {'Full_Name': f'{self.fname} {self.lname}', 'Phone_Number': f'{self.number}'}
        book_contact.append(new_contact)
        return new_contact


def main_function():
    print('Welcome to your contact book')
    while True:
        try:
            user_input = input('add, search, all, delete contact ? (tap exit to quit the contact book) : ').lower()
            if user_input == 'add':
                fname_input = input('First name : ')
                lname_input = input('Last name : ')
                pnum_input = input('Phone Number : ')
                new_contact = Contact(fname_input, lname_input, pnum_input).add_new_contact()
                print(f'New contact added to book : {new_contact}')

            elif user_input == 'search':
                name_input = input('Add a name to the search : ')
                for n in book_contact:
                    if name_input in n['Full_Name']:
                        print(n['Phone_Number'])
                    else:
                        print('Couldnt found this name in the book')

            elif user_input == 'all':
                if len(book_contact) == 0:
                    print('No contact added to the book, please add a new contact')
                else:
                    for i in book_contact:
                        print(i)

            elif user_input == 'delete':
                delete_input = input('Add a name to the search : ')
                for n in book_contact:
                    if delete_input in n['Full_Name']:
                        security_input = input('Are you sure you want to delete this contact ? (y/n): ')
                        if security_input == 'y':
                            book_contact.remove(n)
                            print('The contact was successfully removed')
                        else:
                            print('the contact wasnt removed')
                    else:
                        print('Couldnt found this name in the book')

            elif user_input == 'exit':
                print('have a nice day')
                break

            else:
                print('the action send isnt available, please select a valid action')
        except Exception as error:
            error_message = error.args
            return error_message


main_function()
