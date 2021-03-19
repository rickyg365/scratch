import os
import sys

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
        self.belongs = owner
        self.title = title

    def __str__(self):
        text = f"\n{self.belongs}'s {self.title}: \n \n"
        for data in self.data:
            text += f"  {data}\n"
        return text

    def add_mon(self, mon_obj):
        self.data.append(mon_obj)


class Pokedex(Dex):
    # How do we save multiple pokedexes?
    # saved_pokedexes = {"ot": "save_data"}

    def __init__(self, ot, data=None):
        if data is None:
            data = []
        super().__init__(ot, data,  title="Pokedex")
        self.save_file = 'poke_data.json'
        self.database_file = 'Pokemon.csv'

        # # Load instance
        # self.load()

        # Load database
        self.load_complete(self.database_file)

    def add_pokemon(self, pokemon_name):
        poke_name = pokemon_name.capitalize()
        poke_data = self.complete_data[poke_name]

        poke_name_list = map(lambda data: data.name, self.data)
        if poke_name not in poke_name_list:
            print(f"\n[{poke_name}] added to {self.belongs}'s pokedex")
        # print(poke_data)
        self.data.append(Pokemon(poke_name, poke_data))
        self.save()

    def save(self):
        save_data = {}
        for data in self.data:
            save_data[f"{data.name}"] = data.attr

        json_obj = json.dumps(save_data, indent=3)

        with open("poke_data.json", 'w') as out:
            out.write(json_obj)

    def load(self):
        try:
            with open("poke_data.json", 'r') as load_file:
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


class Digidex(Dex):
    def __init__(self, ot, data=None):
        if data is None:
            data = []
        super().__init__(ot, data, title="Digidex")
        self.save_data = {}

    def save(self):
        for data in self.data:
            self.save_data[f"{data.name}"] = {"Attribute": "Value"}

        json_obj = json.dumps(self.save_data, indent=3)

        with open("digi_data.json", 'w') as out:
            out.write(json_obj)

    def load(self):
        with open("digi_data.json", 'r') as load_file:
            load_data = json.loads(load_file.read())

        for digimon_name, attribute_dict in load_data.items():
            processed_data = Digimon(digimon_name, attr=attribute_dict)
            self.data.append(processed_data)


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
        text = f"#{number} {self.name}\t[Type: {self.attr['Type 1']}] [Gen {self.attr['Generation']}]"
        # Restrict to one line for now
        # for attrib_name, attrib_val in self.attr.items():
        #     if len(text) > 41:
        #         break
        #     text += f" {attrib_name}: {attrib_val} "

        # text += ']'
        return text


class Pokemon(Monster):
    def __init__(self, pokemon_name, attr=None):
        super().__init__(pokemon_name, attr)
        # self.type = attr['type']
        # Instance of poke is a specific pokemon not the general pokemon
        # self.moves = attr['moves']


class Digimon(Monster):
    def __init__(self, digimon_id, attr=None):
        super().__init__(digimon_id, attr)


if __name__ == "__main__":
    # Check if data is present
    try:
        with open("poke_data.json", 'r') as load_f:
            load_data = json.loads(load_f.read())

        # Because we can only save one pokedex I didn't save who it belongs too so I can make a random
        # pokedex and just load it
        # Make it so if its has a name that already exists it loads data if its a new name it doesnt load any data
        p = Pokedex("random")
        p.load()
        print(p)

    except JSONDecodeError:
        # Else start a new game
        print("Welcome young trainer!")
        username = input("\nWhat is your name?: ")

        print("")
        print(f"Ah, I see, so your name is {username}.")
        print("\n")
        print(f"Get ready {username}, your very own adventure is about to begin!")
        print("\n")

        user_pokedex = Pokedex(username)

        starters = [
            ["Bulbasaur", "grass type"],
            ["Squirtle", "water type"],
            ["Charmander", "fire type"]
        ]

        not_chosen = True

        while not_chosen:
            starter = input("Choose: \nGrass, Water, or Fire?: ")
            if starter.lower() == 'grass':
                confirm = input(f"\nThe {starters[0][1]} pokemon {starters[0][0]}, \n\tare you sure?: ")
                if confirm.lower() == 'y':
                    user_pokedex.add_pokemon(starters[0][0])
                    not_chosen = False
            elif starter.lower() == 'water':
                confirm = input(f"\nThe {starters[1][1]} pokemon {starters[1][0]}, \n\tare you sure?: ")
                if confirm.lower() == 'y':
                    user_pokedex.add_pokemon(starters[1][0])
                    not_chosen = False
            elif starter.lower() == 'fire':
                confirm = input(f"\nThe {starters[2][1]} pokemon {starters[2][0]}, \n\tare you sure?: ")
                if confirm.lower() == 'y':
                    user_pokedex.add_pokemon(starters[2][0])
                    not_chosen = False
            else:
                print("\nInvalid input")

        print(user_pokedex)

    # Digidex
    # d = Digidex("RG")
    # d.load()
    #
    # d.save()
    # print(d)
