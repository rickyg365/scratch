import os

"""
Program: League Champion Handler
Author: Rickyg3
Date: 08/24/21
"""


# Variables


# Functions
def func():
    return


# Classes
class ClassName:
    def __init__(self):
        self.var = ""

    def __str__(self):
        text = ""
        return text


class Champion:
    def __init__(self, champion_name):
        self.name = champion_name
        self.tier = ""

        # Abilities
        self.abilities = [
            {
                "id": "p",
                "name": "",
                "priority": 0
             },
            {
                "id": "q",
                "name": "",
                "priority": 0
            },
            {
                "id": "w",
                "name": "",
                "priority": 0
            },
            {
                "id": "e",
                "name": "",
                "priority": 0
            },
            {
                "id": "r",
                "name": "",
                "priority": 0
            }
        ]

        # Runes and Items
        self.runes = []
        self.aram_runes = []

        self.items = []
        self.aram_items = []

        # Might not need
        self.skill_order = []

    def __str__(self):
        text = f"{self.name.title()} [{self.tier}]: "
        text += f"\n Runes: "
        for rune in self.runes:
            text += f"\n\t{rune}"
        text += f"\n Abilities: "
        text += f"\n Items: "
        return text

    def set_ability(self, ability_id, ability_name, ability_priority):
        # This is for when you don't have info, but we do so lets make a cheat dictionary
        # save_index = 0
        # for i, ability in enumerate(self.abilities):
        #     if ability['id'] == ability_id:
        #         save_index = i

        ability_index_map = {
            "p": 0,
            "q": 1,
            "w": 2,
            "e": 3,
            "r": 4
        }

        ability_index = ability_index_map[ability_id]

        self.abilities[ability_index]['name'] = ability_name
        self.abilities[ability_index]['priority'] = ability_priority


class ChampionHandler:
    def __init__(self):
        # list of champion in database
        self.champions = []

        self.scraper = ""

    def __str__(self):
        text = f"{list(champion for champion in self.champions)}"
        return text

    def load_json(self):
        return

    def load_csv(self):
        return

    def load_txt(self):
        return

    def save_json(self):
        return

    def save_csv(self):
        return

    def save_txt(self):
        return


if __name__ == "__main__":

    vayne = Champion('vayne')


