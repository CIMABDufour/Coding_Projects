# Project Difficulty : Medium
# Personal Finance Manager
# This file contain the core functions of the tool

import json


class User :
    def __init__(self, first_name, last_name, password) :
        self.first_name = first_name
        self.last_name = last_name
        self.password = password


class Expenses :
    def __init__(self, category_name, cost) :
        self.category_name = category_name
        self.cost = cost
