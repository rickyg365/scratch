import os
import sys

import time


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


class Item:
    def __init__(self, item_name=None, item_description=None, item_quantity=0, item_tags=None):

        self.name = item_name
        self.description = item_description
        self.quantity = item_quantity
        if item_tags is None:
            item_tags = []
        self.tags = item_tags

    def __str__(self):
        text = f"Item: {self.name} \tQTY: {self.quantity}\n"
        for tag in self.tags:
            text += f"[{tag}] "
        text += f"\n \nDescription: {self.description}\n"

        return text


class ItemContainer:
    def __init__(self, container_name):
        self.name = container_name
        self.items = []
        self.size = 0

    def __str__(self):
        text = f"[{self.name}]:\n"
        for item in self.items:
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


if __name__ == "__main__":
    items_list = []
    for ref_name, item_data in sample_inventory.items():
        print(f"Creating {ref_name} object...")
        items_list.append(Item(item_data['name'], item_data['description'], item_data['quantity'], item_data['tags']))
        time.sleep(0.25)

    print("\n")

    bag = ItemContainer("RG's bag")
    bag.add_item(item_list=items_list)
    print(bag)
