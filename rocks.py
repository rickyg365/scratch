import os
import sys

import pyautogui

import time
import random

import datetime


class Rock:
    def __init__(self, rock_name="", rock_type=""):
        self.name = rock_name
        self.type = rock_type
        self.id = 0

    def __str__(self):
        text = f"#{self.id}\tRock Name: {self.name}\t \t[{self.type}]"
        return text


class RockCollection:
    def __init__(self, collection_name):
        self.name = collection_name
        self.items = []
        self.size = 0

    def __str__(self):
        text = f"{self.name.title()}'s Collection:"

        for item in self.items:
            text += f"\n{item}"

        text += "\n ."

        return text

    def add_rock(self, rock_name="", rock_type="", rock_object=None):
        # Add a check to make sure its a rock object
        if rock_object:
            self.items.append(rock_object)
            self.size += 1
            return True
        else:
            new_rock = Rock(rock_name, rock_type)
            self.items.append(new_rock)
            self.size += 1
            return True


if __name__ == "__main__":
    my_bag = RockCollection("RG")

    rock1 = Rock("Granite", "Igneous")
    rock2 = Rock("Slate", "Metamorphic")
    rock3 = Rock("Sandstone", "Sedimentary")

    my_bag.add_rock("Granite", "Igneous")
    my_bag.add_rock("Sandstone", "Sedimentary")
    my_bag.add_rock(rock_object=rock2)

    print(my_bag)


















