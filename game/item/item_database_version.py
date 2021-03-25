import os
import sys

import time
import csv

""" 
Program: Item Class
Author: rickyg3
Date: 03/23/2021 
"""
''' 
REFERENCE:
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
'''


class Database:
    def __init__(self, filename):
        self.filename = filename
        self.data = {}

    def load(self):
        # had to change from utf-8 to utf-8-sig
        with open(self.filename, encoding='utf-8-sig') as in_csv:
            item_db = csv.DictReader(in_csv)

            for rows in item_db:
                key = rows['id']
                self.data[key] = rows

        print(f"Loaded {self.filename} file")


class ItemDatabase(Database):
    def __init__(self, item_filename='base_item.csv'):
        super().__init__(item_filename)


class Item:
    def __init__(self, item_id, ref_database):
        """
        # Is it better to input a reference database that's already loaded everything or
        # is it better to just take in an item id and have a class function to load the database
        """
        # Attributes
        self.id = item_id
        self.name = ref_database[item_id]['name']
        self.value = ref_database[item_id]['value']
        self.description = ref_database[item_id]['description']

        # Reference dict of attributes in case I need to iterate through the attributes
        self.attributes = ref_database[item_id]

    def __str__(self):
        text = f""
        for attribute_name, attribute in self.attributes.items():
            text += f"{attribute_name.capitalize()}: {attribute}\n"
        # text += '\n'

        return text

    def print_item(self,  display_info=True, box=False, hide_gold=False):
        """
        Display item flags
        - display info: show or hide description
        - box: possible feature, that makes it into a text box
        """
        if hide_gold:
            gold_value = '???'
        else:
            gold_value = f"{self.value}g"
        if box:
            text_box_size = len(self.name) + len(f"{gold_value}") + 5
            text = f".{text_box_size * '-'}.\n"
            text += f"| {self.name.capitalize()} [{gold_value}] |\n"
            text += f"'{text_box_size * '-'}'\n"
            print(text)
        elif display_info:
            print(f"{self.name.capitalize()} [{gold_value}]: '{self.description}'")

        else:
            print(f"{self.name.capitalize()} [{gold_value}]")


class TreasureChest:
    def __init__(self):
        """
        Select random items and save a list of them
        should we save the actual item instances or save a list with the item id's and only load the items
        """
        pass

    def __str__(self):
        pass


class Inventory:
    def __init__(self):
        """
        Holds user items
        """
        pass

    def __str__(self):
        text = ""
        return text


class Shop:
    """
    Each shop object has its own line up
    maybe use the box style for shop?
    """
    def __init__(self):
        pass

    def __str__(self):
        text = ""
        return text


if __name__ == '__main__':
    # Database loading
    item_database = ItemDatabase()
    item_database.load()
    item_data = item_database.data

    # Create item instances, using id# and database reference (so we wont have to reload the database for each item)
    sword = Item('#001', item_data)
    shield = Item('#002', item_data)
    helmet = Item('#003', item_data)

    # Create a list of the item instances
    items = [
        sword,
        shield,
        helmet
    ]

    # Print all item attributes, item by item
    for item in items:
        print(item)

    # Print item for display (Using various styles/settings)
    for item in items:
        # No Description
        item.print_item(display_info=False)
        # Item + Description
        item.print_item()
        # Text box (no description)
        item.print_item(box=True)

        # Hide Gold Value, replaces w/ ???

        # Hide Gold + No Description
        item.print_item(display_info=False, hide_gold=True)
        # Hide Gold + Item + Description
        item.print_item(hide_gold=True)
        # Hide Gold + Text box (no description)
        item.print_item(box=True, hide_gold=True)
