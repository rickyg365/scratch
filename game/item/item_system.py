import os
import sys

import time

""" 
Program: Item Class
Author: rickyg3
Date: 03/23/2021 
"""


class Database:
    def __init__(self, filename):
        self.filename = filename

    def load(self):
        # with open(self.filename, 'r') as in_file:
            # Load file
        print(f"Loaded {self.filename} file")


class ItemDatabase(Database):
    def __init__(self, item_filename='base_item.csv'):
        super().__init__(item_filename)


def load(database: list) -> dict:
    """
    Format = choose_attribute_as_key: {attribute1: val1, attribute2: val2, attribute3: val3, attribute4: val4}

    Result =
        item_db = {
            "#001": {"id": "#001", "name": "sword", "value": 10, "description": "A dull sword"},
            "#002": {"id": "#002", "name": "shield", "value": 10, "description": "A busted down shield"},
            "#003": {"id": "#003", "name": "helmet", "value": 12, "description": "A reliable old helmet"}
        }
    """
    # dict to hold our new database
    temp_db = {}
    # iterate through all the rows in the database
    for item_row in database:
        # Set ID attribute as key
        key = item_row['id']
        # add item row with the chosen attribute as the key
        temp_db[key] = item_row

    return temp_db


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
    # SAMPLE ITEM DATABASE * Not gonna be in final version
    item_db = [
        {"id": "#001", "name": "sword", "value": 10, "description": "A dull sword"},
        {"id": "#002", "name": "shield", "value": 10, "description": "A busted down shield"},
        {"id": "#003", "name": "helmet", "value": 12, "description": "A reliable old helmet"}
    ]

    # Load item database, for now its loading from an object but can change to load from a csv file
    # For now use this
    item_database = load(item_db)
    # # Actual Database loading
    # item_database = ItemDatabase()
    # item_database.load()

    # Create item instances, using id# and database reference (so we wont have to reload the database for each item)
    sword = Item('#001', item_database)
    shield = Item('#002', item_database)
    helmet = Item('#003', item_database)

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
