import os

import requests
from bs4 import BeautifulSoup

from anytree import Node, RenderTree

"""
Program: League Build Scraper/Manager
Author: Rickyg3
Date: 05/22/2021
"""


class Ability:
    def __init__(self):
        self.name = ""
        self.description = ""
        self.damage = ""
        self.cool_down = ""
        self.mana_cost = ""

    def __str__(self):
        text = f""
        return text


class Champion:

    base_url = "https://app.mobalytics.gg/lol/champions/"

    special_champ_urls = {
        'wukong': 'monkeyking',
    }

    current_patch = 0

    def __init__(self, champion_name):
        self.build_url = self.base_url + champion_name + "/build"
        self.aram_url = self.base_url + champion_name + "/aram-builds"

        if champion_name in self.special_champ_urls.keys():
            self.build_url = self.base_url + self.special_champ_urls.get(champion_name) + "/build"
            self.aram_url = self.base_url + self.special_champ_urls.get(champion_name) + "/aram-builds"

        self.last_patch = 0
        self.current_build = ""

        self.name = champion_name

        self.abilities = {
            'Q': {'name': "", 'description': "", 'mana_cost': "", 'stats': ""},
            'W': {'name': "", 'description': "", 'mana_cost': "", 'stats': ""},
            'E': {'name': "", 'description': "", 'mana_cost': "", 'stats': ""},
            'R': {'name': "", 'description': "", 'mana_cost': "", 'stats': ""}
        }
        self.runes = {
            'primary': [],
            'secondary': []
        }
        self.aram_runes = {
            'primary': [],
            'secondary': []
        }
        self.build = {
            'starter': [],
            'core': [],
            'full': []
        }
        self.aram_build = {
            'starter': [],
            'core': [],
            'full': []
        }
        self.summoners = []
        self.skill_order = ""

    def __str__(self):
        text = f""
        return text

    def check_current_patch(self):
        # Return True if on the latest patch
        self.current_patch = None  # webscrape the patch

        if self.last_patch == self.current_patch:
            return True
        return False

    def get_build(self, build_version='aram'):
        current_url = self.build_url
        self.current_build = 'norm'
        if build_version == 'aram':
            current_url = self.aram_url
            self.current_build = 'aram'

        my_scraper = LolScraper(current_url)

        self.summoners = my_scraper.get_sums()
        self.skill_order = my_scraper.get_skill_order()

        if self.current_build == 'aram':
            self.aram_runes = my_scraper.get_runes()
            self.aram_build = my_scraper.get_items()
        else:
            self.build = my_scraper.get_items()
            self.runes = my_scraper.get_runes()


class LolScraper:

    def __init__(self, url):
        self.url = url
        self.soup = None
        self.build = None
        self.raw_info = None

        self.get_starting_points()

    def get_soup(self):
        page = requests.get(self.url)

        self.soup = BeautifulSoup(page.content, 'html.parser')

    def get_starting_points(self):
        self.get_soup()
        starting_point = self.soup.select_one("div.css-k0869a")
        # Build Base Container
        build_info = starting_point.select_one("div.css-1a8oi0m")

        self.build = build_info.select_one("div.css-1qedivl")

        self.raw_info = self.build.select("div.css-1o7o6pr")

    def get_sums(self):
        sum_spells = []

        # Summoner Spells
        sums_items = self.raw_info[1]

        sums_items = sums_items.select("div.css-h82iku")

        sums = sums_items[0]
        sums = sums.select("div.css-1iu2z76")
        for s in sums:
            data = s.find('img')
            sum_name = data['src'].split('-')[-1][15:-4]
            sum_spells.append(sum_name)

        return sum_spells

    def get_items(self):

        build = {'starter': [], 'core': [], 'full': []}

        # Summoner Spells and Items
        sums_items = self.raw_info[1]

        sums_items = sums_items.select("div.css-h82iku")

        items = sums_items[1]

        item_sets = items.select("div.css-19xu9kw")

        for index, item_set in enumerate(item_sets):
            item_list = item_set.findAll('img')
            new_list = []
            for item in item_list:
                name = item['alt']
                new_list.append(name)
            item_sets[index] = new_list

        build['starter'] = item_sets[0]

        build['core'] = item_sets[1]

        build['full'] = item_sets[2]

        return build

    def get_runes(self):
        rune_data = {
            'primary': {'name': "", 'keystone': "", '1': "", '2': "", '3': ""},
            'secondary': {'name': "", "1": "", "2": ""},
            'stats': {'1': "", '2': "", "3": ""}
        }

        # Runes

        raw_runes = self.raw_info[0]

        runes = raw_runes.select("div.css-1h50o8o")

        primary = runes[0]

        secondary = runes[1]

        primary_name = primary.select_one("div.css-6g060g").get_text()
        rune_data['primary']['name'] = primary_name

        primary_data = primary.select("div.css-1hok3la")

        keystone = primary_data[0]
        keystone = keystone.find('img', class_="css-1bdyqpk")
        keystone = keystone['alt']
        rune_data['primary']['keystone'] = keystone

        pone = primary_data[1]
        pone = pone.select_one("div.css-1gh2v5y")
        pone = pone.find('img')['alt']
        rune_data['primary']['1'] = pone

        ptwo = primary_data[2]
        ptwo = ptwo.select_one("div.css-1gh2v5y")
        ptwo = ptwo.find('img')['alt']
        rune_data['primary']['2'] = ptwo

        pthree = primary_data[3]
        pthree = pthree.select_one("div.css-1gh2v5y")
        pthree = pthree.find('img')['alt']
        rune_data['primary']['3'] = pthree

        secondary_name = secondary.select_one("div.css-6g060g").get_text()
        rune_data['secondary']['name'] = secondary_name

        secondary_rows = secondary.select("div.css-1hok3la")

        sone = secondary_rows[0]
        sone = sone.select_one("div.css-1gh2v5y")
        sone = sone.find('img')['alt']
        rune_data['secondary']['1'] = sone

        stwo = secondary_rows[1]
        stwo = stwo.select_one("div.css-1gh2v5y")
        stwo = stwo.find('img')['alt']
        rune_data['secondary']['2'] = stwo

        stats = secondary.select_one("div.css-1qudlbs")
        stat_list = stats.select("div.css-1jf5ej7")

        stat_map = {
            5001: 'Health',
            5002: 'Armor',
            5003: 'Magic Resist',
            5005: 'Atk. Speed',
            5007: 'Cooldown Reduction',
            5008: 'Damage',
        }

        for index, stat in enumerate(stat_list):
            image_tag = stat.find('img')
            stat_name = image_tag['alt']
            stat_choice = int(image_tag['src'][-8:-4])
            print(stat_choice)

            rune_data['stats'][f"{index + 1}"] = f"{stat_name}: {stat_map.get(stat_choice)}"
            print(f"{index + 1}: {stat_name}: {stat_map.get(stat_choice)}")

        return rune_data

    def get_skill_order(self):
        sk_list = []

        skills = self.build.select("div.css-1evdfmk")

        # Skill Order
        skill_order = skills[1]

        skill_order = skill_order.select_one("div.css-70qvj9")

        skill_order = skill_order.findAll('p')

        sk_list = [skill.get_text() for skill in skill_order]

        return sk_list


if __name__ == "__main__":
    champ = input("Choose a champ!: ")
    champion = Champion(champ)

    champ_url = "https://app.mobalytics.gg/lol/champions/soraka/aram-builds"  # champion.aram_url

    scraper = LolScraper(champ_url)

    summoners = scraper.get_sums()
    skill_order = scraper.get_skill_order()

    build_extract = scraper.get_items()
    rune_extract = scraper.get_runes()

    print(
        f"\nsums: {summoners}"
        f"\nskills: {skill_order}"
        f"\nbuild: {build_extract}"
        f"\nrunes: {rune_extract}"
    )
