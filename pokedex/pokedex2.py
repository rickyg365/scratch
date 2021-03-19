import os
import sys

import random
import time

import csv
import json
from json.decoder import JSONDecodeError

""" 
Program: Pokedex and Digidex
Author: rickyg3
Date: 03/18/2021
"""
""" 
TO DO:
- implement saving more than one pokedex, do this in a separate file so we dont ruin this working version
- add something to do for the main program if theres already data lol
- That should lowkey go in a separate file that imports the pokedex function from this one and
- the intro and stuff like that should be its own class
"""


class Dex:
    def __init__(self, owner, data, title="Collection"):
        self.data = data
        self.complete_data = {}
        self.ot = owner
        self.title = title

    def __str__(self):
        text = f"\n{self.ot}'s {self.title}: \n \n"
        for data in self.data:
            text += f"  {data}\n"
        return text

    def add_mon(self, mon_obj):
        self.data.append(mon_obj)


class Pokedex(Dex):
    # How do we save multiple pokedexes?
    saved_pokedexes = {}

    def __init__(self, ot, data=None):
        if data is None:
            data = []
        super().__init__(ot, data,  title="Pokedex")
        self.save_file = 'poke_data2.json'
        self.database_file = 'Pokemon.csv'

        # # Load instance
        # self.load()

        # Load database
        self.load_complete(self.database_file)

    def add_pokemon(self, pokemon_name):
        if pokemon_name[0].islower():
            poke_name = pokemon_name.capitalize()
        else:
            poke_name = pokemon_name
        poke_data = self.complete_data[poke_name]

        poke_name_list = map(lambda data: data.name, self.data)
        if poke_name not in poke_name_list:
            self.data.append(Pokemon(poke_name, poke_data))
            print(f"\n[{poke_name}] added to {self.ot}'s pokedex")
        # print(poke_data)
        self.save()

    def add_id(self, pokemon_id):
        for name, data in self.complete_data.items():
            if data['#'] == str(pokemon_id):
                self.add_pokemon(name)

    def save(self):
        save_data = {}
        for data in self.data:
            save_data[f"{data.name}"] = data.attr

        json_obj = json.dumps(save_data, indent=3)

        with open(self.save_file, 'w') as out:
            out.write(json_obj)

    def load(self):
        try:
            with open(self.save_file, 'r') as load_file:
                load_data = json.loads(load_file.read())

            for pokemon_name, attribute_dict in load_data.items():
                processed_data = Pokemon(pokemon_name, attr=attribute_dict)
                self.data.append(processed_data)
        except JSONDecodeError:
            print("No Data")

    def load_complete(self, csv_file):
        self.complete_data = {}

        with open(csv_file, encoding='utf-8') as csvf:
            csvreader = csv.DictReader(csvf)

            for rows in csvreader:
                key = rows['Name']
                self.complete_data[key] = rows


class Monster:
    def __init__(self, monster_name, attr=None):
        self.name = monster_name
        if attr is None:
            attr = {}
        self.attr = attr

    def __str__(self):
        number = f"{self.attr['#']}"
        if len(number) < 3:
            diff = 3 - len(number)
            number = f"{diff*'0'}{number}"
        spacing = 15 - len(self.name)
        if spacing < 0:
            spacing = 1
        text = f"#{number} {self.name}{spacing*' '}[Type: {self.attr['Type 1']}] [Gen {self.attr['Generation']}]"

        return text


class Pokemon(Monster):
    def __init__(self, pokemon_name, attr=None):
        super().__init__(pokemon_name, attr)
        # self.type = attr['type']
        # Instance of poke is a specific pokemon not the general pokemon
        # self.moves = attr['moves']


if __name__ == "__main__":
    username = input("Please input your name: ")

    user_dex = Pokedex(username)

    run = True

    while run:
        r = random.randint(0, 720)

        user_dex.add_id(r)
        
        query = input("\nWould you like to add another random pokemon?: ")
        if query.upper() == 'N':
            run = False

    print(user_dex)
