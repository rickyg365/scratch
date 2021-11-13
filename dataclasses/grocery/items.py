import os
from datetime import datetime
from typing import Optional
from dataclasses import dataclass


# from enum import Enum, auto

# Enum is good for data you don't need to display, maybe just need for comparison within python
# class GroceryType(Enum):
#     ESSENTIALS = auto()
#     PRODUCE = auto()
#     DAIRY = auto()
#     MEAT = auto()
#     DELI = auto()
#     BREAD = auto()
#     PASTA = auto()
#     CONDIMENT = auto()
#     SPICE = auto()
#     CANNED = auto()
#     FROZEN = auto()
#     DRINK = auto()
#     ALCOHOL = auto()
#     JUNK = auto()

# @dataclass(order=True) , then just add sort_index ass attribute
# sort_index: float = field(init=False, repr=False)
#
# def __post_init__(self):
#     self.sort_index = self.attr

@dataclass
class GroceryItem:
    # attr_name: attr_type = field(repr=False, default=default_value)
    name: str
    type: str
    price: float
    brand: Optional[str] = None
    flavor: Optional[str] = None
    item_id: Optional[int] = None
    description: Optional[str] = None

    def __str__(self):
        return f"[{self.item_id:^-3.0f}] {self.name:<20}: \t${self.price}  \t{self.flavor}"

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.name}[{self.item_id:03.0f}] : ${self.price} : {self.flavor}>"


@dataclass
class InventoryItem(GroceryItem):
    purchase_date: datetime.date = datetime.now()
    quantity_bought: int = 1
    quantity_remaining: int = 1
    quantity_unit: Optional[str] = None
    expiration_date: Optional[datetime.date] = None

    def __str__(self):
        return f"[{self.item_id:^-3.0f}] {self.name:<20}: \t{self.quantity_remaining}/{self.quantity_bought} {self.quantity_unit} \t{self.flavor}"

    # def __repr__(self):
    #     return f"<{self.__class__.__name__}: {self.name}[{self.item_id:03.0f}] : ${self.price} : {self.type}>"

    def validate_types(self):
        """
        name: str
        type: str
        price: float
        brand: Optional[str] = None
        flavor: Optional[str] = None
        item_id: Optional[int] = None
        description: Optional[str] = None
        purchase_date: datetime.date = datetime.datetime.now()
        quantity_bought: int = 1
        quantity_remaining: int = 1
        quantity_unit: Optional[str] = None
        expiration_date: Optional[datetime.date] = None
        """
        # Have to do
        # Price
        self.price = float(self.price)
        # item_id
        self.item_id = int(self.item_id)
        # purchase_date
        # self.purchase_date = datetime.strptime(self.purchase_date, "%m/%d/%Y")
        # quantity_bought
        self.quantity_bought = int(self.quantity_bought)
        # quantity_remaining
        self.quantity_remaining = int(self.quantity_remaining)
        # expiration_date
        # self.expiration_date = datetime.strptime(self.purchase_date, "%m/%d/%Y")

    def update_quantity(self, new_quantity):
        """ Update remaining quantity """
        self.quantity_remaining = new_quantity

    def percentage_left(self):
        """ Update remaining quantity """
        return self.quantity_remaining/self.quantity_bought

    def is_finished(self):
        """ return true if quantity remaining is 0 """
        return self.quantity_remaining == 0


if __name__ == "__main__":
    # Get Terminal Dimensions
    width, height = os.get_terminal_size()

    # Sample Data
    sample_grocery_obj = {
        "item_id": 1,
        "name": "carrots",
        "type": "PRODUCE",
        "price": 1.25
    }

    sample_inventory_obj = {
        **sample_grocery_obj,
        "purchase_date": datetime.datetime.now(),
        "quantity_bought": 1,
        "quantity_remaining": 1,
        "quantity_unit": "indv",
        "expiration_date": datetime.datetime.now()
    }

    # obj_list = [
    #     {
    #         "item_id": 1,
    #         "name": "Carrots",
    #         "type": "PRODUCE",
    #         "price": 1.25
    #     },
    #     {
    #         "item_id": 2,
    #         "name": "Ground Beef",
    #         "type": "MEAT",
    #         "price": 9.24
    #     },
    #     {
    #         "item_id": 3,
    #         "name": "Milk",
    #         "type": "DAIRY",
    #         "price": 3.45
    #     }
    # ]
    #
    # my_groceries = []
    # my_inventory = []
    #
    # # Iterate through data and add as GroceryObj to Inventory
    # for my_item in obj_list:
    #     my_groceries.append(GroceryItem(**my_item))
    #     my_inventory.append(InventoryItem(**my_item))

    print(f"{'-' * width}")
    print("Groceries: ", GroceryItem(**sample_grocery_obj))
    print("Inventory: ", InventoryItem(**sample_inventory_obj))
    print(f"{'-'*width}")
