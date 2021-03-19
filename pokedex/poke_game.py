import os
import sys

import time
import random

from pokedex2 import *


""" 
Program:
Author:
Date: 03/18/2021
"""


# Functions
def clear_screen():
    os.system('cls')


def check_save(file):
    try:
        with open(file, 'r') as load_f:
            load_data = json.loads(load_f.read())
        return True
    except JSONDecodeError:
        return False

def load_game(file):
    '''
    load json,
    should be a list of trainers with their own pokedex
    nay a dictionary with the trainer name (Trainer id?) as a key and all attributes as a dict
    '''

def intro():
    # Start a new game
    print("Welcome young trainer!")
    name = input("\nWhat is your name?: ")

    print("")
    print(f"Ah, I see, so your name is {name}.")
    print("\n")
    print(f"Get ready {name}, your very own adventure is about to begin!")
    print("\n")

    pokedex = Pokedex(name)

    starters = [
        ["Bulbasaur", "grass type"],
        ["Squirtle", "water type"],
        ["Charmander", "fire type"]
    ]

    not_chosen = True

    while not_chosen:
        starter = input("Choose: \nGrass, Water, or Fire?: ")
        if starter.lower() == 'grass':
            confirm = input(f"\nThe {starters[0][1]} pokemon {starters[0][0]}, are you sure?: ")
            if confirm.lower() == 'y':
                pokedex.add_pokemon(starters[0][0])
                not_chosen = False
        elif starter.lower() == 'water':
            confirm = input(f"\nThe {starters[1][1]} pokemon {starters[1][0]}, are you sure?: ")
            if confirm.lower() == 'y':
                pokedex.add_pokemon(starters[1][0])
                not_chosen = False
        elif starter.lower() == 'fire':
            confirm = input(f"\nThe {starters[2][1]} pokemon {starters[2][0]}, are you sure?: ")
            if confirm.lower() == 'y':
                pokedex.add_pokemon(starters[2][0])
                not_chosen = False
        else:
            print("\nInvalid input")

    print(pokedex)

    return pokedex

# Classes
class Game():
    def __init__(self, file_name):
        self.file_name = file_name
        self.running = True

    def run(self):
        while self.running:
            print("Hi")


class Item:
    def __init__(self, item_id, item_reference):
        self.id = item_id

        self.name = ""
        self.quantity = 0
        self.description = ""

        # itemref = [ {item_id1:{name: "", quantity:"", ...}}, ...]
        self.item_reference = item_reference
        self.get_item(item_id)

    def __str__(self):
        text = f"\n{self.name}| {self.quantity}|\n{self.description}\n"
        return text

    def get_item(self, item_id):
        for tem_id, attr in self.item_reference.items():
            if item_id == tem_id:
                self.name = attr['name']
                self.quantity = attr['quantity']
                self.description = attr['description']


class Trainer:
    def __init__(self, trainer_name):
        self.name = trainer_name
        self.pokedex = None
        self.badges = []
        self.party = []
        self.bag = []


    def __str__(self):
        text = f"\n| {self.name} |\n"
        return text


if __name__ == "__main__":
    # Check if data is present
    if check_save:
        # save data is present
        # current_game = Load_game()
        # user_pokedex = current_game.get_pokedex(user_name)
    else:
        user_pokedex = intro()

    # try:
    #     with open("poke_data.json", 'r') as load_f:
    #         load_data = json.loads(load_f.read())
    #
    #     # Because we can only save one pokedex I didn't save who it belongs too so I can make a random
    #     # pokedex and just load it
    #     # Make it so if its has a name that already exists it loads data if its a new name it doesnt load any data
    #     p = Pokedex("random")
    #     p.load()
    #     print(p)

    # except JSONDecodeError:
