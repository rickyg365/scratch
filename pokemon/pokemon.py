import os
import random
import pandas as pd


"""
Data Key
{mega}{legend}{gen}{dex #}
"""


def get_name(dataframe, dex_num):
    return dataframe['Name'][dex_num]


def get_num(dataframe, dex_num):
    return dataframe['#'][dex_num]


def get_type1(dataframe, dex_num):
    return dataframe['Type 1'][dex_num]


def get_type2(dataframe, dex_num):
    return dataframe['Type 2'][dex_num]


def get_gen(dataframe, dex_num):
    return dataframe['Generation'][dex_num]


def get_legendary(dataframe, dex_num):
    return dataframe['Legendary'][dex_num]


def load_pokemon(dataframe):
    return


def load_data(filepath):
    pokemon_dataframe = pd.read_csv(filepath)

    # column_names = []
    #
    # for index, item in enumerate(pokemon_dataframe):
    #     column_names.append(item)
    #
    # print(column_names)

    # load data into a dict with unique keys and into a pokemon obj
    pokemon_data = {}

    for i in range(len(pokemon_dataframe)):
        # parse data
        dex_number = pokemon_dataframe["#"][i]
        name = pokemon_dataframe["Name"][i]
        gen = pokemon_dataframe["Generation"][i]
        legend = pokemon_dataframe["Legendary"][i]

        type1 = pokemon_dataframe["Type 1"][i]
        type2 = pokemon_dataframe["Type 2"][i]

        # check mega status
        mega_status = "Mega" in name
        if mega_status:
            length_slice = len(pokemon_dataframe["Name"][i-1])
            name = name[length_slice:]

        # check type 2
        if type(type2) is float:
            type2 = ""

        # Create KEY  | (legend)(generation)(mega)(dex no.)
        my_key = f"{1 if legend else 0}{gen}{1 if mega_status else 0}{dex_number:03.0f}"

        # add parsed data into dict using the newly generated key
        pokemon_data[my_key] = Pokemon(
            name=name,
            dex=int(dex_number),
            types=[type1, type2],
            legendary_status=legend,
            generation=gen
        )

        # check data
        # print(f"{i}: ", my_key, name)

    return pokemon_data


class Pokemon:
    def __init__(self, name="", dex=0, types=None, moves=None, legendary_status=False, generation=0):
        if types is None:
            types = ["", ""]
        if moves is None:
            moves = []

        self.name = name
        self.dex = dex
        self.generation = generation
        self.legendary = legendary_status
        self.type = types
        self.moves = moves

    def __str__(self):
        text = f"[{self.dex:03.0f}] {self.name} [{self.type[0]}]{f'[{self.type[1]}]' if (self.type[1] != '') else ''}"
        # text += f"\nMoves:\n {self.moves}"
        return text

    def use_move(self):
        ...

    def learn_move(self):
        ...

    def evolve(self):
        ...


if __name__ == "__main__":
    # sample_pokemon = {
    #     "name": "corviknight",
    #     "dex": 73,
    #     "types": ["dark", "flying"],
    #     "moves": ["fly", "peck", "steel wing", "pursuit"]
    # }
    #
    # corviknight = Pokemon(**sample_pokemon)
    #
    # print(corviknight)

    current_data = load_data("poke_data/Pokemon.csv")

    for value in current_data.values():
        print(value)
