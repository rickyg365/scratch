import os
import time

import requests
from bs4 import BeautifulSoup

from anytree import Node, RenderTree


class Ability:
    def __init__(self):
        self.name = ""
        self.description = ""
        self.stats = {
            'damage': [],
            'cool_down': [],
            'mana_cost': []
        }

    def __str__(self):
        text = f""
        return text


class Champion:
    base_url = ""
    def __init__(self, champion_name):
        self.name = champion_name
        self.abilities = {
            'Q': None,
            'W': None,
            'E': None,
            'R': None
        }
        self.runes = {
            'primary': [],
            'secondary': []
        }
        self.build = []
        self.skill_order = []


    def __str__(self):
        text = f""
        return text


class LeagueScraper:
    base_url = "https://app.mobalytics.gg/lol/champions/"

    special_champ_urls = {
        'wukong': 'monkeyking',
    }

    def __init__(self, champion_name):
        champion_name = champion_name.lower()

        self.build_url = self.base_url + champion_name + "/build"
        self.aram_url = self.base_url + champion_name + "/aram-builds"

        if champion_name in self.special_champ_urls.keys():
            self.build_url = self.base_url + self.special_champ_urls.get(champion_name) + "/build"
            self.aram_url = self.base_url + self.special_champ_urls.get(champion_name) + "/aram-builds"

        self.soup = None

    def get_page(self, url_version):
        if url_version == 'aram':
            ARAM = requests.get(self.aram_url)

            self.soup = BeautifulSoup(ARAM.content, 'html.parser')
        else:
            regular = requests.get(self.build_url)

            self.soup = BeautifulSoup(regular.content, 'html.parser')

    def extract_data(self):
        rune_data = {
            'primary': {'name': "", 'keystone': "", '1': "", '2': "", '3': ""},
            'secondary': {'name': "", "1": "", "2": ""},
            'stats': {'1': "", '2': "", "3": ""},
            'skills': [],
            'sums': [],
            'items': {'starter': [], 'core': [], 'full': []}
        }

        starting_point = self.soup.select_one("div.css-k0869a")
# Build Base Container
        build_info = starting_point.select_one("div.css-1a8oi0m")

        build = build_info.select_one("div.css-1qedivl")

        skills = build.select("div.css-1evdfmk")

# Skill Order
        skill_order = skills[1]

        skill_order = skill_order.select_one("div.css-70qvj9")

        skill_order = skill_order.findAll('p')

        rune_data['skills'] = [skill.get_text() for skill in skill_order]

# Runes

        raw_info = build.select("div.css-1o7o6pr")

        raw_runes = raw_info[0]

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
        stats = stats.select("div.css-1jf5ej7")
        for index, stat in enumerate(stats):
            image_tag = stat.find('img')
            stat_name = image_tag['alt']
            stat_choice = int(image_tag['src'][-8:-4])

            stat_map = {
                5001: 'Health',
                5002: 'Armor',
                5003: 'Magic Resist',
                5005: 'Atk. Speed',
                5007: 'Cooldown Reduction',
                5008: 'Damage',
            }
            rune_data['stats'][f"{index+1}"] = f"{stat_name}: {stat_map.get(stat_choice)}"
            # print(f"{index + 1}: {stat_name}: {stat_map.get(stat_choice)}")
# Summoner Spells and Items
        sums_items = raw_info[1]

        sums_items = sums_items.select("div.css-h82iku")

        sums = sums_items[0]
        sums = sums.select("div.css-1iu2z76")
        for s in sums:
            data = s.find('img')
            sum_name = data['src'].split('-')[-1][15:-4]
            rune_data['sums'].append(sum_name)
            # print(sum_name)
        # print(sums)

        items = sums_items[1]

        item_sets = items.select("div.css-19xu9kw")

        for index, item_set in enumerate(item_sets):
            item_list = item_set.findAll('img')
            new_list = []
            for item in item_list:
                name = item['alt']
                new_list.append(name)
            item_sets[index] = new_list

        rune_data['items']['starter'] = item_sets[0]

        rune_data['items']['core'] = item_sets[1]

        rune_data['items']['full'] = item_sets[2]

        return rune_data

#
# champion = "ashe"
#
# base_url = "https://app.mobalytics.gg/lol/champions/"
#
# build_url = base_url + champion + "/build"
#
# aram_url = base_url + champion + "/aram-builds"
#
#
# # Download Page
# ARAM = requests.get(aram_url)
#
# # Parse ARAM Page
# aram_soup = BeautifulSoup(ARAM.content, 'html.parser')
#
# # print(aram_soup.prettify())
#
# starting_point = aram_soup.select_one("div.css-k0869a")
#
# # print(starting_point)
#
# build_info = starting_point.select_one("div.css-1a8oi0m")
#
# # print(build_info)
#
# build = build_info.select_one("div.css-1qedivl")
#
# # print(build)
#
# raw_runes = build.select_one("div.css-1o7o6pr")
#
# # print(runes)
#
# runes = raw_runes.select("div.css-1h50o8o")
#
# primary = runes[0]
#
# secondary = runes[1]
#
# # print(primary)
# # print()
# # print(secondary)
#
# primary_name = primary.select_one("div.css-6g060g").get_text()
#
# # print(primary_name)
#
# primary_data = primary.select("div.css-1hok3la")
#
# # print(primary_data)
#
# keystone = primary_data[0]
# keystone = keystone.find('img', class_="css-1bdyqpk")
# keystone = keystone['alt']
# # print(keystone)
#
# pone = primary_data[1]
# pone = pone.select_one("div.css-1gh2v5y")
# pone = pone.find('img')['alt']
# # print(pone)
#
# ptwo = primary_data[2]
# ptwo = ptwo.select_one("div.css-1gh2v5y")
# ptwo = ptwo.find('img')['alt']
# # print(ptwo)
#
# pthree = primary_data[3]
# pthree = pthree.select_one("div.css-1gh2v5y")
# pthree = pthree.find('img')['alt']
# # print(pthree)
#
#
# secondary_name = secondary.select_one("div.css-6g060g").get_text()
#
# # print(secondary_name)
#
#
# secondary_rows = secondary.select("div.css-1hok3la")
#
# sone = secondary_rows[0]
# sone = sone.select_one("div.css-1gh2v5y")
# sone = sone.find('img')['alt']
# # print(sone)
#
# stwo = secondary_rows[1]
# stwo = stwo.select_one("div.css-1gh2v5y")
# stwo = stwo.find('img')['alt']
# # print(stwo)
#
#
# stats = secondary.select_one("div.css-1qudlbs")
# stats = stats.select("div.css-1jf5ej7")
# for index, stat in enumerate(stats):
#     image_tag = stat.find('img')
#     stat_name = image_tag['alt']
#     stat_choice = int(image_tag['src'][-8:-4])
#
#     stat_map = {
#         5001: 'Health',
#         5002: 'Armor',
#         5003: 'Magic Resist',
#         5005: 'Atk. Speed',
#         5007: 'Cooldown Reduction',
#         5008: 'Damage',
#     }
#
#     print(f"{index+1}: {stat_name}: {stat_map.get(stat_choice)}")
# # print(stats)


if __name__ == "__main__":
    champ = input('Choose a champ: ')
    print("")
    my_scraper = LeagueScraper(champ)
    my_scraper.get_page('aram')
    my_runes = my_scraper.extract_data()

    # print(my_runes)
    champion = Node(champ.title())

# Skills
    skills = Node('Skills', parent=champion)

    skill_max = ""
    for size_t, skill in enumerate(my_runes['skills']):
        if size_t == 2:
            skill_max += f"{skill}"
        else:
            skill_max += f"{skill} > "
    skill = Node(skill_max, parent=skills)

    # for size_t, skil in enumerate(my_runes['skills']):
    #     new_skill = Node(f"{size_t+1}: {my_runes['skills'][size_t]}", parent=skills)

    # skill1 = Node(my_runes['skills'][0], parent=skills)
    # skill2 = Node(my_runes['skills'][1], parent=skills)
    # skill3 = Node(my_runes['skills'][2], parent=skills)

    # Summoner Spells
    sums = Node('Summoner Spells', parent=champion)

    sumd = Node(f"D: {my_runes['sums'][0]}", parent=sums)
    sumf = Node(f"F: {my_runes['sums'][1]}", parent=sums)

    # Runes
    runes = Node("Runes", parent=champion)

    primary = Node(my_runes['primary']['name'], parent=runes)

    keystone = Node(my_runes['primary']['keystone'], parent=primary)
    pone = Node(my_runes['primary']['1'], parent=primary)
    ptwo = Node(my_runes['primary']['2'], parent=primary)
    pthree = Node(my_runes['primary']['3'], parent=primary)

    secondary = Node(my_runes['secondary']['name'], parent=runes)
    sone = Node(my_runes['secondary']['1'], parent=secondary)
    stwo = Node(my_runes['secondary']['2'], parent=secondary)

    stat1 = Node(my_runes['stats']['1'], parent=runes)
    stat2 = Node(my_runes['stats']['2'], parent=runes)
    stat3 = Node(my_runes['stats']['3'], parent=runes)

    # Items
    items = Node('Items', parent=champion)

    starter = Node('Starter', parent=items)
    for s_item in my_runes['items']['starter']:
        new_s_item = Node(s_item, parent=starter)

    core = Node('Core', parent=items)
    for c_item in my_runes['items']['core']:
        new_c_item = Node(c_item, parent=core)

    full = Node('Full', parent=items)
    for f_item in my_runes['items']['full']:
        new_f_item = Node(f_item, parent=full)

    for pre, fill, node in RenderTree(champion):
        print("%s%s" % (pre, node.name))

    #
    # print(
    #     f"\n{my_runes['primary']['name']}"
    #     f"\n\tKeystone: {my_runes['primary']['keystone']}"
    #     f"\n\t1: {my_runes['primary']['1']}"
    #     f"\n\t2: {my_runes['primary']['2']}"
    #     f"\n\t3: {my_runes['primary']['3']}"
    #     f"\n"
    #     f"\n{my_runes['secondary']['name']}"
    #     f"\n\t1: {my_runes['secondary']['1']}"
    #     f"\n\t2: {my_runes['secondary']['2']}"
    #     f"\n"
    #     f"\n{my_runes['stats']['1']}"
    #     f"\n{my_runes['stats']['2']}"
    #     f"\n{my_runes['stats']['3']}"
    #     f"\n"
    # )
    print()