import os
import time
import random


def clear_screen():
    clear_command = "cls"
    os.system(clear_command)


class Item:
    """
    Base Item class
    """
    def __init__(self, item_id=0, item_name="", attr=None):
        if attr is None:
            attr = {}
        self.id = item_id
        self.name = item_name
        self.attr = attr
        # self.attr = {
        #     "attr1": "value1",
        #     "attr2": "value2",
        #     "attr3": "value3",
        #     "attr4": "value4",
        #     "attr5": "value5",
        #     "attr6": "value6",
        #     "attr7": "value7",
        #     "attr8": "value8",
        # }

    def __str__(self):
        text = f"[{self.id:03}] {self.name}"
        return text


class Collection:
    """
    Base Item class
    """
    CURRENT_ID = 0
    VALID_ITEM_TYPES = ["Item", "Book", "Movie", "Clothes"]

    def __init__(self, collection_name, items=None, item_type="Item"):
        if items is None:
            items = []
        if item_type not in self.VALID_ITEM_TYPES:
            item_type = "Item"
        self.id = 0
        self.name = collection_name

        self.item_type = item_type
        self.items = items

    def __str__(self):
        text = f"[{self.id:03}] {self.name}"
        text += "\n"
        for _ in range(len(self.items)):
            text += f"{self.items[_]}\n"

        return text

    def assign_id(self):
        self.CURRENT_ID += 1
        return self.CURRENT_ID

    def add_item(self, name, attr=None):
        current_id = self.assign_id()
        # Edit this for each collection
        new_item = eval(f"{self.item_type}({current_id}, '{name}', {attr})")
        self.items.append(new_item)


if __name__ == "__main__":
    clear_screen()

    item1 = Item(1, "Item 11", {"1": "1", "2": "2"})
    item2 = Item(2, "Item 12")
    item3 = Item(3, "Item 13")

    my_item_list = [item1, item2, item3]

    coll1 = Collection("new-collection", my_item_list)
    print(coll1)

    coll2 = Collection("2nd-collection")
    coll2.add_item("Item 21", {"1": "1", "2": "2"})
    coll2.add_item("Item 22")
    coll2.add_item("Item 23")
    print(coll2)
