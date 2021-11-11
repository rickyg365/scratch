import os
import datetime
from typing import Optional
from dataclasses import dataclass


# from enum import Enum, auto

# Enum is good for data you don't need to display, maybe just need for comparison within python
# class GroceryType(Enum):
#     PRODUCE = auto()
#     DAIRY = auto()
#     MEAT = auto()
#     DELI = auto()
#     BREAD = auto()
#     PASTA = auto()
#     CONDIMENT = auto()
#     SPICE = auto()
#     CANNED = auto()
#     DRINK = auto()
#     ALCOHOL = auto()
#     JUNK = auto()


@dataclass
class GroceryItem:
    name: str
    type: str
    price: float
    brand: Optional[str] = None
    flavor: Optional[str] = None
    item_id: Optional[int] = None
    description: Optional[str] = None

    def __str__(self):
        self.validate_type(self.type)

        return f"{self.name} \t [{self.item_id:03.0f}]: \t${self.price}  \t{self.type}"

    def __repr__(self):
        self.validate_type(self.type)

        return f"<{self.name}[{self.item_id:03.0f}] : ${self.price} : {self.type}>"

    def validate_type(self, check_type):
        valid_types = [
            "PRODUCE",
            "DAIRY",
            "MEAT",
            "DELI",
            "BREAD",
            "PASTA",
            "CONDIMENT",
            "SPICE",
            "CANNED",
            "DRINK",
            "ALCOHOL",
            "JUNK"
        ]

        if check_type.upper() not in valid_types:
            self.type = "NEW"


class Inventory:
    def __init__(self):
        self.items = []
        self.quick_access = {}
        self.length = 0

        # are we assuming items are ordered by id? in that case we can use the id as the array index num (-1 ofc)

    def __str__(self):
        text = ""
        # text += f"#  NAME \t [_ID]: \tPRICE \tTYPE\n"
        for _, item in enumerate(self.items):
            text += f"{_+1}| {item}\n"
        return text

    def add_item(self, new_item: GroceryItem) -> None:
        """ Add item to list of items """
        self.items.append(new_item)
        self.quick_access[new_item.item_id] = new_item
        self.length += 1

    def remove_item(self, item_id) -> bool:
        """ Remove item using id, returns bool """
        ''' Use Timeit to see which way is faster '''
        # for item in self.items:
        #     if item.item_id == item_id:
        #         self.items.remove(item)
        #         return True
        # return False
        current = self.quick_access.get(item_id, None)

        if current:
            self.items.remove(current)
            self.quick_access.pop(item_id)
            self.length -= 1
            return True
        return False

    """ Modify Item??? func """

    def find_item(self, item_id):
        """ Find item by id, return None if not found """
        current = self.quick_access.get(item_id, None)

        return current


if __name__ == "__main__":
    # Get Terminal Dimensions
    width, height = os.get_terminal_size()

    # Sample Data
    sample_obj = {
        "item_id": 1,
        "name": "carrots",
        "type": "PRODUCE",
        "price": 1.25
    }

    obj_list = [
        {
            "item_id": 1,
            "name": "Carrots",
            "type": "PRODUCE",
            "price": 1.25
        },
        {
            "item_id": 2,
            "name": "Ground Beef",
            "type": "MEAT",
            "price": 9.24
        },
        {
            "item_id": 3,
            "name": "Milk",
            "type": "DAIRY",
            "price": 3.45
        }
    ]

    # Create new blank inventory
    my_inventory = Inventory()

    # Iterate through data and add as GroceryObj to Inventory
    for my_item in obj_list:
        my_inventory.add_item(GroceryItem(**my_item))

    # Display Current Inventory
    print(f"\n[ Current Inventory ], Size: {my_inventory.length}")

    print(f"{width * '-'}")
    print(my_inventory)

    # Edit Inventory
    my_inventory.remove_item(2)

    # Display New Inventory
    print(f"[ Current Inventory ], Size: {my_inventory.length}")

    print(f"{width * '-'}")
    print(my_inventory)

    # Item Lookup
    print(f"[ Item Lookup ]")

    print(f"{width * '-'}")

    # Python anti pattern, find the best way to handle this.
    # null_data = lambda x: "Item not found" if x is None else x
    #
    # print(null_data(my_inventory.find_item(3)))
    #
    # print(null_data(my_inventory.find_item(2)))

    search = my_inventory.find_item(3)
    print("Item not found" if search is None else search)

    fail_search = my_inventory.find_item(2)
    print("Item not found" if fail_search is None else fail_search)

    print("")
