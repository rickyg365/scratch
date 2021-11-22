import time
import json

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


# Classes
class BuildScraper:
    def __init__(self):
        self.url = ""
        self.soup = None

        self.data = {
            'patch': 0,
            'name': '',
            'mode': '',
            'tier': '',
            'rank': '',
            'spells': [],
            'skill_priority': [],
            'runes': {
                'primary_name': '',
                'secondary_name': '',
                'primary': [],
                'secondary': [],
                'other': []
            },
            'items': {
                'starter': [],
                'core': [],
                'full': []
            }
        }

    def __str__(self):
        text = f"Patch: {self.data['patch']}\n{self.data['name'].title():^20} | {self.data['rank']:^10} [{self.data['tier']:^3}]"
        return text

    def steps_div_class(self, steps, starting_soup=None):
        current_soup = starting_soup
        if starting_soup is None:
            current_soup = self.get_soup() if self.soup is None else self.soup
            print(starting_soup)
        # current_soup = starting_soup
        print(current_soup, "done")
        for step in steps:
            print(f"{step} \n{current_soup}")
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
        if self.data['mode'].lower() in valid_aram:
            self.data['mode'] = 'aram'

    def validate_champ(self):

        special_cases = {
            'wukong': 'monkeyking'
        }

        if self.data['name'] in special_cases:
            self.data['name'] = special_cases[self.data['name']]

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

        base_url = f"https://app.mobalytics.gg/lol/champions/{self.data['name']}"

        # Normal   -> vayne/build
        # Aram     -> vayne/aram-builds
        # Counters -> vayne/counters
        # Guide    -> vayne/guide
        if self.data['mode'] == 'aram':
            return base_url + f"/aram-builds"

        if self.data['mode'] in valid_requests:
            return base_url + f"/{self.data['mode']}"

        # Else return default
        return base_url + f"/build"

    def get_soup(self):
        self.url = self.build_url()
        page = requests.get(self.url)

        condition = str(page.status_code)[0] == '2'

        if condition:
            return BeautifulSoup(page.content, "html.parser")

        # else
        print(page.status_code)
        return None

    @staticmethod
    def get_champ_tier_rank(starting_point):
        header_list = starting_point.find_all('div', 'm-1scqgey')

        tier = header_list[1].find('img')['alt']
        rank = header_list[0].find('p').get_text(strip=True)

        return tier, rank

    @staticmethod
    def get_skill_priority(starting_point):
        """
        Returns in order list of skill priority
        """

        skill_priority_element_list = starting_point.find_all('p')

        skill_priority_list = []
        for p_element in skill_priority_element_list:
            skill_priority_list.append(p_element.get_text())
        # print(skill_priority_list)

        return skill_priority_list

    def get_runes(self, starting_point):

        branches = starting_point.find_all('div', class_='m-1953d5c')
        base_primary, secondary_plus = branches

        # Find Branch
        branch_map = {
            'Precision': 'm-ysur5m',
            'Domination': 'm-x6atmv',
            'Sorcery': 'm-1gvu32d',
            'Inspiration': 'm-ynny72',
            'Resolve': 'm-atmt6i',
        }

        branch_names = []
        for branch in branches:
            branch_steps = [
                'm-16mmcnu',
                'm-1c9b3nz',
                'm-1izw5ay'
            ]
            name_element = self.steps_div_class(branch_steps, branch)
            branch_names.append(name_element.get_text(strip=True))

        # print(branch_names)
        primary_name, secondary_name = branch_names

        self.data['runes']['primary_name'] = primary_name
        self.data['runes']['secondary_name'] = secondary_name

        # Primary Runes
        primary_steps = [
            'm-16mmcnu',
            f"{branch_map[primary_name]}",
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
        # print('Primary: ', primary_runes)

    # Secondary plus

        # Secondary
        secondary_steps = [
            'm-16mmcnu',
            branch_map.get(secondary_name)
        ]
        secondary_rows = self.steps_div_class(secondary_steps, secondary_plus)
        active_rows = secondary_rows.find_all('div', class_="m-1hok3la")

        secondary_runes = []

        for row in active_rows:
            active_element = row.find('div', class_="m-17xx7ne")
            new_secondary_rune = active_element.find('img')['alt']
            secondary_runes.append(new_secondary_rune)

        # print('Secondary: ', secondary_runes)

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

        # print('Other: ', other_runes)

        return primary_runes, secondary_runes, other_runes

    @staticmethod
    def get_sum_spells(starting_point):
        spell_elements = starting_point.find_all('div', class_='m-1thjkq')

        spells = []
        for element in spell_elements:
            spell = element.find('img')['src'][-10:-4]
            spells.append(spell)

        # parse spell url for spell name
        # print(spells)
        return spells

    def get_items(self, starting_point):
        item_branches = starting_point.find_all('div', class_='m-14bp6ot')

        refine_steps = [
            'm-1d3w5wq',
            'm-yhe5ws',
            'm-1uz370t'
        ]

        starter_items = []
        core_items = []
        full_build = []

        starter_flag = False
        core_flag = False
        full_flag = False

        for _, item_branch in enumerate(item_branches):
            refined_branch = self.steps_div_class(refine_steps, item_branch)
            raw_items = refined_branch.select("div > div > img[alt]")

            # starter, core, full = raw_items
            if _ == 0:
                starter_flag = True
                core_flag = False
                full_flag = False
            if _ == 1:
                starter_flag = False
                core_flag = True
                full_flag = False
            if _ == 2:
                starter_flag = False
                core_flag = False
                full_flag = True

            for item in raw_items:
                item_name = item['alt']
                if starter_flag:
                    starter_items.append(item_name)
                if core_flag:
                    core_items.append(item_name)
                if full_flag:
                    full_build.append(item_name)
                # print(item_name)

        # print("Starter Items: ", starter_items)
        # print("Core Items: ", core_items)
        # print("Full Build: ", full_build)
        return starter_items, core_items, full_build

    def run_scraper(self, champion_name, gamemode):
        """
        Build out the skeleton and then when you get to branch points call individual functions that take in start_point
        """
        # SAVE CHAMP NAME AND MODE
        self.data['name'] = champion_name
        self.data['mode'] = gamemode

        # VALIDATE CHAMP AND GAMEMODE
        self.validate_champ()
        self.validate_gamemode()

        # BUILD URL
        self.build_url()

        # GET/REFRESH SOUP
        self.soup = self.get_soup()

        # FIND ROOT
        base = self.soup.find('main', class_='m-36y2kb')
        steps = [
            'm-1dw2zw',
            "m-cmscw5"
        ]

        root = self.steps_div_class(steps, base)

        # FIND MAIN BRANCH ROOTS aka branch out

        # HEADER
        header_steps = [
            'm-19c8912',
            'm-5t4kgk'
        ]
        header = self.steps_div_class(header_steps, root)

        # BODY CONTENT
        body_content = root.find('div', class_="m-cmscw5")

        # GET PATCH
        patch_steps = [
            'm-2kr0ld',
            'm-e0nk88',
            'm-2x9yv2',
            'm-18pdjar'
        ]
        patch_element = self.steps_div_class(patch_steps, body_content)

        patch = patch_element.find('span').get_text(strip=True)
        self.data['patch'] = patch

        # CHAMP INFO LIST
        champ_info_steps = [
            'm-18nur1e',
            'm-2ps0tg',
        ]
        champ_info = self.steps_div_class(champ_info_steps, body_content)

        champ_info_list = champ_info.find_all('div', 'm-1evdfmk')

        # GET RANK AND TIER
        tier, rank = self.get_champ_tier_rank(header)
        self.data['tier'], self.data['rank'] = tier, rank

        # GET SKILLS
        skill_priority_steps = [
            'm-1o7o6pr',
            'm-h82iku',
            'm-3jew8v',
            'm-7s2yt4',
            'm-s5xdrg'
        ]
        skill_priorities = self.steps_div_class(skill_priority_steps, champ_info_list[1])

        skills = self.get_skill_priority(skill_priorities)
        self.data['skill_priority'] = skills

        # GET RUNES, SPELLS, AND ITEMS
        base_list = champ_info_list[0].find_all('div', class_='m-1o7o6pr')

        base_runes = base_list[0]
        base_spells_items = base_list[1]

        # GET RUNES
        rune_steps = [
            'm-h82iku',
            'm-ea8wdb'
        ]
        runes = self.steps_div_class(rune_steps, base_runes)

        primary_list, secondary_list, other_list = self.get_runes(runes)
        self.data['runes']['primary'] = primary_list
        self.data['runes']['secondary'] = secondary_list
        self.data['runes']['other'] = other_list

        # SUM SPELL ITEM SPLIT
        base_spells, base_items = base_spells_items.find_all('div', class_='m-h82iku')

        # SUMS SPELLS
        spell_container = base_spells.find('div', class_='m-oeh2q5')

        spells = self.get_sum_spells(spell_container)
        self.data['spells'] = spells

        # GET ITEMS

        item_root = base_items.find('div', class_='m-1y0hiws')

        start, cor, ful = self.get_items(item_root)

        self.data['items']['starter'] = start
        self.data['items']['core'] = cor
        self.data['items']['full'] = ful

        return self.data

    def save_json(self):
        """
        TBI
        """
        return

    def save_csv(self):
        """
        TBI
        """
        return

    def save_txt(self):
        """
        TBI
        """
        return


if __name__ == "__main__":

    start_time = time.time()

    # Main Program
    my_scraper = BuildScraper()

    running = True

    while running:

        champ_name = input("Champion Name?: ")
        if champ_name.lower() == 'quit':
            running = False
            continue

        game_mode = input("Mode?: ")

        my_scraper.run_scraper(champ_name, game_mode)

        print(my_scraper)
        print(my_scraper.data)

    # Program Finish

    end_time = time.time()

    print(f"\nProcess took {end_time - start_time}s")
