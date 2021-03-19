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
            print(f"[{poke_name}] added to {self.belongs}'s pokedex")
        print(poke_data)
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
        text = f"{self.name}\t["
        # Restrict to one line for now
        for attrib_name, attrib_val in self.attr.items():
            if len(text) > 41:
                break
            text += f" {attrib_name}: {attrib_val} "

        text += ']'
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
    # Pokedex
    p = Pokedex("RG")
    p.add_pokemon('Squirtle')
    p.add_pokemon('Bulbasaur')
    p.add_pokemon('Charmander')

    print(p)

    # Digidex
    # d = Digidex("RG")
    # d.load()
    #
    # d.save()
    # print(d)
