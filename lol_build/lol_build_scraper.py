import os

import time

import requests
from bs4 import BeautifulSoup

"""
Program: League of Legends, build scraper
Author: Rickyg3
Date: 08/23/21
"""
"""
BS4 
- find method => find('html_tag', class_='', id='')
- select method => select("css_selector")
"""


# Functions


# Classes
class ClassName:
    def __init__(self):
        self.var = ""

    def __str__(self):
        text = ""
        return text


class BuildScraper:
    def __init__(self, champion_name, game_mode=""):
        self.champion_name = champion_name

        self.game_mode = game_mode
        self.validate_gamemode()

        self.url = self.build_url()
        self.soup = self.get_soup()

        # Get Root
        base = self.soup.find('main', class_='m-36y2kb')
        steps = [
            'm-1dw2zw',
            'm-1hq4tsy'
        ]

        self.root = self.steps_div_class(steps, base)

        # Branches
        self.header = None
        self.body_content = None
        self.champ_info_list = None

        self.patch = 0

        self.branch_out()

    def __str__(self):
        self.get_skill_priority()
        self.get_runes_items()
        tier, rank = self.get_champ_tier_rank()
        text = f"Patch: {self.patch}\n{self.champion_name.title():^20} | {rank:^10} [{tier:^3}]"
        return text

    def refresh_soup(self):
        self.soup = self.get_soup()

    def branch_out(self):
        # HEADER
        header_steps = [
            'm-19c8912',
            'm-5t4kgk'
        ]
        self.header = self.steps_div_class(header_steps, self.root)

        # BODY CONTENT
        self.body_content = self.root.find('div', class_="m-cmscw5")

        # PATCH
        patch_steps = [
            'm-2kr0ld',
            'm-e0nk88',
            'm-2x9yv2',
            'm-18pdjar'
        ]
        patch_element = self.steps_div_class(patch_steps, self.body_content)

        self.patch = patch_element.find('span').get_text()

        # CHAMP INFO LIST
        champ_info_steps = [
            'm-18nur1e',
            'm-2ps0tg',
        ]
        champ_info = self.steps_div_class(champ_info_steps, self.body_content)

        self.champ_info_list = champ_info.find_all('div', 'm-1evdfmk')

    def steps_div_class(self, steps, starting_soup=None):
        if starting_soup is None:
            starting_soup = self.root
        current_soup = starting_soup
        for step in steps:
            # do a section find
            new_soup = current_soup.find('div', class_=f"{step}")
            current_soup = new_soup

        return current_soup

    def validate_gamemode(self):
        # Base output is raw input
        # Valid spellings and abbreviations
        # valid_sums = [
        #     "sum",
        #     "summoners",
        #     "summoner",
        #     "summoners rift",
        #     "sum rift",
        #     "sums rift"
        # ]
        valid_aram = [
            "aram",
            "a",
            "howling",
            "howling abyss"
        ]

        # correct to proper output
        # if raw_game_mode.lower() in valid_sums:
        #     game_mode = 'summoners'
        if self.game_mode.lower() in valid_aram:
            self.game_mode = 'aram'

    def validate_champ(self):
        return

    def build_url(self):
        # Champion Name Validation
        special_cases = {
            'wukong': "monkeyking",


        }
        # NO SPECIAL CASES YET!!!

        # Game_mode url selection

        valid_requests = [
            'counters',
            'guide'
        ]

        base_url = f"https://app.mobalytics.gg/lol/champions/{self.champion_name}"

        # Normal   -> vayne/build
        # Aram     -> vayne/aram-builds
        # Counters -> vayne/counters
        # Guide    -> vayne/guide
        if self.game_mode == 'aram':
            return base_url + f"/aram-builds"

        if self.game_mode in valid_requests:
            return base_url + f"/{self.game_mode}"

        # Else return default
        return base_url + f"/build"

    def get_soup(self):
        page = requests.get(self.url)

        condition = str(page.status_code)[0] == '2'

        if condition:
            return BeautifulSoup(page.content, "html.parser")

        # else
        print(page.status_code)
        return None

    def get_champ_tier_rank(self):
        header_list = self.header.find_all('div', 'm-1scqgey')

        tier = header_list[1].find('img')['alt']
        rank = header_list[0].find('p').get_text(strip=True)

        return tier, rank

    def get_skill_priority(self):

        skill_priority_steps = [
            'm-1o7o6pr',
            'm-h82iku',
            'm-3jew8v',
            'm-7s2yt4',
            'm-s5xdrg'
        ]
        skill_priorities = self.steps_div_class(skill_priority_steps, self.champ_info_list[1])

        skill_priority_element_list = skill_priorities.find_all('p')

        skill_priority_list = []
        for p_element in skill_priority_element_list:
            skill_priority_list.append(p_element.get_text())

        print(skill_priority_list)

        return skill_priority_list

    def get_runes_items(self):
        base_list = self.champ_info_list[0].find_all('div', class_='m-1o7o6pr')

        base_runes = base_list[0]
        rune_steps = [
            'm-h82iku',
            'm-ea8wdb'
        ]
        runes = self.steps_div_class(rune_steps, base_runes)

        base_primary, secondary_plus = runes.find_all('div', class_='m-1953d5c')

        primary_steps = [
            'm-16mmcnu',
            'm-ysur5m',
        ]

        primary = self.steps_div_class(primary_steps, base_primary)

        primary_rows = primary.find_all('div', class_="m-1hok3la")

        top_row = primary_rows[0]

        primary_runes = []

        keystone = top_row.find('img')['alt']
        primary_runes.append(keystone)

        for row in primary_rows[1:]:
            new_primary_rune = row.find('div', class_="m-17xx7ne").find('img')['alt']
            primary_runes.append(new_primary_rune)
        print('Primary: ', primary_runes)
    # Secondary plus

        # Secondary
        secondary_steps = [
            'm-16mmcnu',
            'm-x6atmv',
        ]
        secondary_rows = self.steps_div_class(secondary_steps, secondary_plus)
        active_rows = secondary_rows.find_all('div', class_="m-1hok3la")

        secondary_runes = []

        for row in active_rows:
            active_element = row.find('div', class_="m-17xx7ne")
            new_secondary_rune = active_element.find('img')['alt']
            secondary_runes.append(new_secondary_rune)

        print('Secondary: ', secondary_runes)

        # Plus
        rune_map = {
            '5001': 'Health',
            '5002': 'Armor',
            '5003': 'MR',
            '5005': 'Atk Spd',
            '5007': 'CDR',
            '5008': 'Force',
            '5000': 'Error',
        }
        plus_runes = secondary_plus.find('div', class_='m-bbc0pq e1xh10yy2')

        plus_rows = plus_runes.find_all('div', class_='m-1do3yya e1xh10yy1')

        other_runes = []

        for row in plus_rows:
            active_element = row.find('div', class_='e1xh10yy0 m-1uu0ijn')

            new_active_rune_key = active_element.find('img')['src'][-8:-4]
            other_runes.append(rune_map[new_active_rune_key])

        print('Other: ', other_runes)






        return

    def get_sum_spells(self):
        return


if __name__ == "__main__":
    # Variables
    # data = {
    #     'name': 'vayne',
    #     'gamemode': 'aram',
    #     'tier': '',
    #     'q': 0,
    #     'w': 0,
    #     'e': 0,
    #     'r': 0,
    #     'items': [],
    #     'runes': []
    # }
    start_time = time.time()

    champ_name = 'vayne'   # data['name']
    game_mode = 'aram'  # data['gamemode']

    my_scraper = BuildScraper(champ_name, game_mode)
    print(my_scraper)

    # for key, value in data.items():
    #     print(f"{key}: {value}")

    end_time = time.time()

    print(f"\nProcess took {end_time - start_time}s")
