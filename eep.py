import os
import sys

import time

""" 
Program: 
Author: rickyg3
Date: 03/20/2021
"""


class Entry:
    def __init__(self, entry_name):
        # This class is necessary because it assigns the attributes tot he entry object without it we would have to
        # manually do it, This will make base objects and then in our table we can update local versions of the objects
        # attributes

        self.name = entry_name
        self.attributes = {}

    def __str__(self):
        text = f"[{self.name}]"
        return text

    # Can also update
    def add_attribute(self, new_key, value):
        self.attributes[new_key] = value


class Table:
    def __init__(self, width=4):
        '''
        Example Layout:
        .--------------------.
        |entry1              |
        |entry2 entry3       |
        |entry4 entry5 entry6|
        '____________________'

        [entry1]
        [entry2, entry3]
        ...

        '''
        self.layout = []

        self.width = width

        self.data = {}

    def __str__(self):
        text = ""
        count = 0
        for entry_name, entry_data in self.data.items():
            if count > (self.width - 2):
                count = 0
                text += f"{self.data[entry_name]}\n"
            else:
                text += f"{self.data[entry_name]} "
                count += 1

        return text

    def add_entry(self, entry_name):
        entry = Entry(entry_name)
        self.data[entry_name] = entry

    def update_entry(self, entry_name, new_data):
        # set current entry
        current_entry = self.data[entry_name]
        # Iterate through new data and add it to entry object
        for name, value in new_data.items():
            current_entry.add_attribute(name, value)


if __name__ == '__main__':
    t = Table(width=3)
    t.add_entry("#1")
    t.add_entry("#2")
    t.add_entry("#3")
    t.add_entry("#4")

    t.add_entry("#5")
    t.add_entry("#6")
    t.add_entry("#7")
    t.add_entry("#8")

    new_dat = {"name": "random name", "HP": "100", "random_attr": "random value"}
    t.update_entry('#4', new_dat)

    print(t)
