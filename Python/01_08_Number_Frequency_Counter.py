# Beginner Project
# Count instance of number in list
# Add numbers in list and print the number of instances of each

import random


def lst_num_generator() :
    lst_num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    new_lst_num = []
    count = 0
    while count < 10 :
        new_num_to_lst = random.choice(lst_num)
        new_lst_num.append(new_num_to_lst)
        count += 1
    return new_lst_num


def lst_num_count(num_list) :
    num_dict = {i : num_list.count(i) for i in num_list}
    return num_dict


print(lst_num_count(lst_num_generator()))
