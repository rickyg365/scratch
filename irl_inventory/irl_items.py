import os
import sys

import csv
import time

"""
Program: Custom Item Object
Author: Rickyg3
Date: 04/09/2021
"""
''' 
Add something to display only 5 entries at a time and then you can go to the next couple of 
entries by inputting something or by pressing a key 

'''


class Item:
    def __init__(self, item_name=None, item_description=None, item_quantity=0, item_tags=None):

        self.name = item_name
        self.description = item_description
        self.quantity = item_quantity
        if item_tags is None:
            item_tags = []
        self.tags = item_tags

    def __str__(self):
        text = f"Item: {self.name}\t QTY: {self.quantity}\n"
        for tag in self.tags:
            text += f" [{tag}]"
        text += f"\n \nDescription: {self.description}\n"

        return text


class ItemContainer:
    def __init__(self, container_name):
        self.name = container_name
        self.items = []
        self.size = 0

        self.jdict = {}

    def __str__(self):
        text = f"[{self.name}]:\n"
        for item in self.items:
            text += 45*'-'
            text += f"\n{item}\n"
        return text

    def add_item(self, item=None, item_list=None):
        if item is None:
            for current_item in item_list:
                self.items.append(current_item)
                self.size += 1
            return True
        else:
            self.items.append(item)
            self.size += 1
            return True

    def load_csv(self, csv_filename, key_index='name'):

        with open(csv_filename, encoding='utf-8-sig') as input_file:
            lines = csv.DictReader(input_file)

            for rows in lines:

                key = rows[key_index]
                print(f"Creating {key} object...")

                # Parse Item data
                item_name = rows['name']
                item_description = rows['description']
                item_quantity = int(rows['quantity'])
                item_tags = rows['tags'].split('_')

                # Create new item obj
                new_item = Item(item_name, item_description, item_quantity, item_tags)
                self.size += 1

                # Add to list
                self.items.append(new_item)
                self.jdict[key] = rows
                time.sleep(0.35)


# No max size, add folders and other exclusive features
class Inventory(ItemContainer):
    def __init__(self, inventory_name=""):
        super().__init__(inventory_name)
        '''
        self.folders = ["folder1", "folder2"]
        '''
        self.folders = {'base': []}

    def __str__(self):
        text = ""
        return text

    def add_folder(self, folder_name):
        self.folders[folder_name] = []

    def add_item(self, item=None, item_list=None, folder="base"):
        if item is None:
            for current_item in item_list:
                self.folders[folder].append(current_item)
                self.size += 1
            return True
        else:
            self.folders[folder].append(item)
            self.size += 1
            return True


# Max size
class Backpack(ItemContainer):
    def __init__(self, backpack_name="", backpack_size=20):
        super().__init__(backpack_name)
        self.max_size = backpack_size

    def __str__(self):
        text = ""
        return text


class ItemScreen:
    def __init__(self, item_container_object):
        self.screen_list = self.pagify(item_container_object)

    def pagify(self, item_container):
        pages = []
        active = True
        n = 4
        ite = 0
        ref = item_container.size
        while active:
            new_page = []

            if (ite+n) > ref:
                end = ite + (ref - ite)
                active = False
            else:
                end = ite + n
            for i in range(ite, end):
                new_page.append(item_container.items[ite])
                ite += 1

            pages.append(new_page)

        return pages

    def display(self):
        for screen in self.screen_list:
            for s in screen:
                print(s)
            input("\nPress Enter to Continue...")


if __name__ == "__main__":
    sample_inventory = {
        # "item_name": {"name": "item_name",
        #               "description": "item_description",
        #               "quantity": 0,
        #               "tags": ["tag1", "tag2"]},
        "black jeans": {"name": "black jeans",
                        "description": "a faded pair of black jeans",
                        "quantity": 1,
                        "tags": ["clothes", "old"]},
        "red dress shirt": {"name": "red dress shirt",
                            "description": "A nice Red button up dress shirt",
                            "quantity": 1,
                            "tags": ["clothes", "dress"]},
        "gameboy micro": {"name": "gameboy micro",
                          "description": "An old gameboy micro",
                          "quantity": 1,
                          "tags": ["electronic", "gaming"]}
    }

    # items_list = []
    # for ref_name, item_data in sample_inventory.items():
    #     print(f"Creating {ref_name} object...")
    #     items_list.append(Item(item_data['name'], item_data['description'], item_data['quantity'], item_data['tags']))
    #     time.sleep(0.25)
    print("-" * 50)
    run = True

    bag = ItemContainer("RG's bag")
    bag.load_csv('inventory.csv')
    # bag.add_item(item_list=items_list)

    while run:
        os.system("cls")

        print(f"[{bag.name}'s bag] [{bag.size}]")
        print(f"\n[D]: Display\n[Q]: Quit\n")

        user_input = input("\n>>> ")

        if user_input.lower() == "d":
            os.system("cls")
            # print(bag)
            pages = ItemScreen(bag)
            # pages.display()
            display = pages.screen_list

            for page in display:
                os.system("cls")
                for item in page:
                    print(40*'-')
                    print(item)
                input("Press Enter to Continue...")

        elif user_input.lower() == 'q':
            run = False
        else:
            print("invalid input")
