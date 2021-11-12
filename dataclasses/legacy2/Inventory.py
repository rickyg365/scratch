import os
import datetime

from items import GroceryItem, InventoryItem
from typing import List


"""
Ideas:

- split the analyzer into functions that check the data and a seperate class that displays the data

Ex.
1. analyzer: [check which are low, sort by certain criteria]
2. ConsoleReport: [low_summary report, low_summary_bar report]

"""


class Inventory:
    def __init__(self):
        self.items = []
        self.quick_access = {}
        self.length = 0

        # are we assuming items are ordered by id? in that case we can use the id as the array index num (-1 ofc)

    def __str__(self):
        """ Prints all the items """
        text = ""
        # text += f"#  NAME \t [_ID]: \tPRICE \tTYPE\n"
        for _, item in enumerate(self.items):
            text += f"{item}\n"  # {_+1}|   add for debug
        return text

    def __call__(self, *args, **kwargs):
        return self.items

    def pretty_print(self, console_width=0):
        title_bar = f"Current Inventory , Size: {my_inventory.length} \n[ID] Name : Quantity Type"
        visual_break = f"\n{console_width * '-'}"
        inventory = f"\n{my_inventory}"

        # return title_bar + visual_break + inventory
        print(title_bar + visual_break + inventory)

    def add_item(self, new_item: GroceryItem) -> None:
        """ Add item to list of items """
        self.items.append(new_item)
        self.quick_access[new_item.item_id] = new_item
        self.length += 1

    def remove_item(self, item_id) -> bool:
        """ Remove item using id, returns bool """
        ''' Use Timeit to see which way is faster '''

        current = self.quick_access.get(item_id, None)

        if current:
            self.items.remove(current)
            self.quick_access.pop(item_id)
            self.length -= 1
            return True
        return False

    """ Modify Item??? func """

    def find_item(self, item_id) -> InventoryItem:
        """ Find item by id, return None if not found """
        return self.quick_access.get(item_id, None)

    def remove_empty(self):
        for item in self.items:
            if item.is_finished():
                self.remove_item(item.item_id)

    def filter(self, attr: str, condition="default") -> List[InventoryItem]:
        temp_list = []
        match condition:
            case "gt":
                for item in self.items:
                    if item > attr:
                        temp_list.append(item)
                return temp_list
            case "lt":
                for item in self.items:
                    if item < attr:
                        temp_list.append(item)
                return temp_list

            case "default":
                for item in self.items:
                    if item == attr:
                        temp_list.append(item)
                return temp_list


class InventoryAnalyzer:
    def __init__(self):
        self.inventory = None

    def filter(self, items: List[InventoryItem], filter_function) -> List[InventoryItem]:
        temp_list = []
        for item in items:
            condition = filter_function(item)

            if condition:
                temp_list.append(item)

        return temp_list

    def low_summary(self, items: List[InventoryItem], threshold: float = 0.3) -> str:
        """ Returns a Summary of any quantities that are low """
        summary_report = f"\r"

        for item in items:
            percentage_left = item.quantity_remaining/item.quantity_bought

            if percentage_left <= threshold:
                summary_report += f"[{item.item_id:^3}] {item.name:<20}:  {percentage_left*100:-3.0f}% \n"

        return summary_report

    def low_summary_bar(self, items: List[InventoryItem], threshold: float = 0.3, console_width: int = 10, sep: str = "\n") -> str:
        usable_space = console_width-3
        summary_report = f"\r"

        for item in items:
            percentage_left = item.quantity_remaining / item.quantity_bought

            if percentage_left <= threshold:
                optional_bar = f" |{'█' * (round(percentage_left * usable_space)):<{usable_space}}|\n"
                summary_report += f"[{item.item_id:^3}] {item.name:<20}:  {percentage_left*100:-3.0f}%{sep}{optional_bar}"

        return summary_report


if __name__ == "__main__":
    # Get Terminal Dimensions
    width, height = os.get_terminal_size()

    print(f"")

    sample_inventory_objs = [
        {
            "item_id": 1,
            "name": "Carrots",
            "type": "PRODUCE",
            "price": 1.25,
            "purchase_date": datetime.datetime.now(),
            "quantity_bought": 5,
            "quantity_remaining": 2,
            "quantity_unit": "indv",
            "expiration_date": datetime.datetime.now()
        },
        {
            "item_id": 2,
            "name": "Ground Beef",
            "type": "MEAT",
            "price": 9.24,
            "purchase_date": datetime.datetime.now(),
            "quantity_bought": 1,
            "quantity_remaining": 1,
            "quantity_unit": "package",
            "expiration_date": datetime.datetime.now()
        },
        {
            "item_id": 3,
            "name": "Milk",
            "type": "DAIRY",
            "price": 3.45,
            "purchase_date": datetime.datetime.now(),
            "quantity_bought": 1,
            "quantity_remaining": 1,
            "quantity_unit": "gallon",
            "expiration_date": datetime.datetime.now()
        },
        {
            "item_id": 4,
            "name": "Buttermilk Bread",
            "type": "BREAD",
            "price": 5.45,
            "purchase_date": datetime.datetime.now(),
            "quantity_bought": 2,
            "quantity_remaining": 1,
            "quantity_unit": "loaf",
            "expiration_date": datetime.datetime.now()
        },
        {
            "item_id": 5,
            "name": "Onions",
            "type": "PRODUCE",
            "price": 3.15,
            "purchase_date": datetime.datetime.now(),
            "quantity_bought": 3,
            "quantity_remaining": 2,
            "quantity_unit": "indv",
            "expiration_date": datetime.datetime.now()
        }
    ]

    # Create new blank inventory
    my_inventory = Inventory()

    # Iterate through data and add as GroceryObj to Inventory
    for my_item in sample_inventory_objs:
        my_inventory.add_item(InventoryItem(**my_item))

    # Display Current Inventory
    my_inventory.pretty_print(width)

    # Edit Inventory
    my_inventory.remove_item(2)

    # Display New Inventory
    my_inventory.pretty_print(width)

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

    print("\n")

    # Clear Empty
    # my_inventory.remove_empty()
    # my_inventory.pretty_print(width)
    # print("\n")

    # Analyze Inventory
    analyzer = InventoryAnalyzer()

    my_report1 = analyzer.low_summary(my_inventory(), 0.8)
    my_report2 = analyzer.low_summary_bar(my_inventory(), 0.8, console_width=width//2, sep="")

    print(f"Low Summary Report: \n{width * '-'}", my_report1)

    print(f"Low Summary Report w/ bar: \n{width * '-'}", my_report2)

    # Filter Inventory -> returns temp copy doesnt actually mutate, this is useful for data
    filtered_items = analyzer.filter(my_inventory(), lambda x: x.type == "PRODUCE")
    print(f"Filtered items: \n{width * '-'}")

    for item in filtered_items:
        print(item)

    last_report = analyzer.low_summary_bar(filtered_items, 1, console_width=width//2, sep="")

    print(f"\nLast Low Summary Bar Report w/ filtered items: \n{width * '-'}", last_report)
