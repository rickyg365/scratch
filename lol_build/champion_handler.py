import os

from lol_build_scraper2 import *

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


class ChampionBuild:
    def __init__(self, initial_champion_data=None):
        # self.name = ""
        # self.tier = ""
        # self.rank = ""
        # self.patch = 0
        # self.mode = ""
        #
        # self.skill_priority = []
        # self.runes = {}
        # self.items = {}
        self.name = ""
        self.tier = ""
        self.rank = ""

        # current patch when data was extracted
        self.patch = ""
        self.mode = ""

        # Abilities
        self.skill_priority = []

        # Runes and Items
        self.runes = {}

        self.items = {}

        self.builds = {}

        if initial_champion_data is not None:
            self.update_data(initial_champion_data)

    def __str__(self):
        # text = f"{self.name.title()} [{self.tier}]: "
        text = f"Patch: {self.patch}\n{self.name.title():^30} | {self.rank:^10} [{self.tier:^3}]"
        text += f"\n Runes: "
        for rune_branch, runes in self.runes.items():
            text += f"\n\t{rune_branch}{runes}"
        text += f"\n Abilities: {self.skill_priority}"
        text += f"\n Items: "
        for item_set, items in self.items.items():
            text += f"\n\t{item_set}{items}"
        return text

    def add_build(self, champion_data):
        game = champion_data['mode']
        if game != 'aram':
            game = 'norm'

        key = f"{champion_data['name']}_{champion_data['patch']}_{game}"

        if key in self.builds.keys():
            return False
        print(key)
        print(champion_data)
        self.builds[key] = champion_data

        print(self.builds)
        return True

    def update_data(self, champion_data):
        self.name = champion_data['name']
        self.tier = champion_data['tier']
        self.rank = champion_data['rank']

        # current patch when data was extracted
        self.patch = champion_data['patch']
        self.mode = champion_data['mode']

        # Abilities
        self.skill_priority = champion_data['skill_priority']

        # Runes and Items
        self.runes = {
            f"{champion_data['runes']['primary_name']}": champion_data['runes']['primary'],
            f"{champion_data['runes']['secondary_name']}": champion_data['runes']['secondary'],
            'other': champion_data['runes']['other']
        }

        self.items = {
            'Starting Items': champion_data['items']['starter'],
            'Core Items': champion_data['items']['core'],
            'Full Build': champion_data['items']['full']
        }

        self.add_build(champion_data)

    def print_data(self, champion_data):
        name = champion_data['name']
        tier = champion_data['tier']
        rank = champion_data['rank']

        # current patch when data was extracted
        patch = champion_data['patch']
        mode = champion_data['mode']

        # Abilities
        skill_priority = champion_data['skill_priority']

        # Runes and Items
        runes = {
            f"{champion_data['runes']['primary_name']}": champion_data['runes']['primary'],
            f"{champion_data['runes']['secondary_name']}": champion_data['runes']['secondary'],
            'other': champion_data['runes']['other']
        }

        items = {
            'Starting Items': champion_data['items']['starter'],
            'Core Items': champion_data['items']['core'],
            'Full Build': champion_data['items']['full']
        }

        text = f"Patch: {patch}\n{name.title():^30} | {rank:^10} [{tier:^3}]"
        text += f"\n Runes: "
        for rune_branch, rune_list in runes.items():
            text += f"\n\t{rune_branch}{rune_list}"
        text += f"\n Abilities: {skill_priority}"
        text += f"\n Items: "
        for item_set, item_list in items.items():
            text += f"\n\t{item_set}{item_list}"

        return text

    def print_all_data(self):
        new_entry = ""
        for t, build in self.builds.items():
            title = t
            print(title, self.name)
            new_entry += self.print_data(build)

        print(new_entry)


class ChampionHandler:
    def __init__(self):
        # list of champion in database
        self.champions = []

        self.scraper = BuildScraper()

    def __str__(self):
        text = f"{list(champion for champion in self.champions)}"
        return text

    def add_champion(self, champion_name, mode):

        self.scraper.run_scraper(champion_name, mode)

        return

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
    new_scrape = BuildScraper()
    champions = []

    while True:

        champ = input("Champion: ")
        if champ.lower() == 'quit':
            break

        champ_build_data = new_scrape.run_scraper(champ, '')

        new_champ = ChampionBuild(champ_build_data)

        # Cant scrape too fast
        time.sleep(1)
        new_data = new_scrape.run_scraper(champ, 'aram')
        new_champ.update_data(new_data)

        champions.append(new_champ)

    print(champions)

    for champ_builds in champions:
        print(f"\n{champ_builds.name.upper()} Build: ")
        print(champ_builds)
        champ_builds.print_all_data()
