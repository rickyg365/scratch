import os

from datetime import datetime
from items import GroceryItem, InventoryItem


global_placeholder_date = datetime.strptime("Jan 1 2005 20:13:50", "%b %d %Y %H:%M:%S")


class GroceryItemTest:
    def __init__(self):
        # Test that will be run during run_test method
        self.active_test = [
            # self.update_quantity_test,
            # self.percentage_left_test,
            # self.is_finished_test
        ]

        # Reference Data
        self.testee = GroceryItem(**{
            "item_id": 5,
            "name": "Yerba Mate",
            "type": "DRINK",
            "price": 3.69
        })

    def run_all(self):
        # Print Intro
        print(f"\nRunning Grocery Item Test:\n")
        for current_test in self.active_test:
            # Run Test
            current_test()

            print(f"[ {current_test.__name__} ]: Passed \u2713")
        print("")

    def display_sample(self):
        print(f"Grocery Item: \n", self.testee)


class InventoryItemTest:
    def __init__(self):
        # Test that will be run during run_test method
        self.active_test = [
            self.update_quantity_test,
            self.percentage_left_test,
            self.is_finished_test
        ]

        # Reference Data
        self.sample_inventory_item = InventoryItem(**{
            "item_id": 5,
            "name": "Yerba Mate",
            "type": "DRINK",
            "price": 3.69,
            "purchase_date": global_placeholder_date,
            "quantity_bought": 5,
            "quantity_remaining": 2,
            "quantity_unit": "cans",
            "expiration_date": global_placeholder_date
        })

        self.sample_inventory_objs = [
            InventoryItem(**{
                "item_id": 1,
                "name": "Carrots",
                "type": "PRODUCE",
                "price": 1.25,
                "purchase_date": global_placeholder_date,
                "quantity_bought": 5,
                "quantity_remaining": 2,
                "quantity_unit": "indv",
                "expiration_date": global_placeholder_date
            }),
            InventoryItem(**{
                "item_id": 2,
                "name": "Ground Beef",
                "type": "MEAT",
                "price": 9.24,
                "purchase_date": global_placeholder_date,
                "quantity_bought": 1,
                "quantity_remaining": 1,
                "quantity_unit": "package",
                "expiration_date": global_placeholder_date
            }),
            InventoryItem(**{
                "item_id": 3,
                "name": "Milk",
                "type": "DAIRY",
                "price": 3.45,
                "purchase_date": global_placeholder_date,
                "quantity_bought": 1,
                "quantity_remaining": 1,
                "quantity_unit": "gallon",
                "expiration_date": global_placeholder_date
            }),
            InventoryItem(**{
                "item_id": 4,
                "name": "Buttermilk Bread",
                "type": "BREAD",
                "price": 5.45,
                "purchase_date": global_placeholder_date,
                "quantity_bought": 2,
                "quantity_remaining": 1,
                "quantity_unit": "loaf",
                "expiration_date": global_placeholder_date
            }),
            InventoryItem(**{
                "item_id": 5,
                "name": "Onions",
                "type": "PRODUCE",
                "price": 3.15,
                "purchase_date": global_placeholder_date,
                "quantity_bought": 3,
                "quantity_remaining": 2,
                "quantity_unit": "indv",
                "expiration_date": global_placeholder_date
            })
        ]

        self.testee = InventoryItem(**{
            "item_id": 5,
            "name": "Yerba Mate",
            "type": "DRINK",
            "price": 3.69,
            "purchase_date": global_placeholder_date,
            "quantity_bought": 5,
            "quantity_remaining": 2,
            "quantity_unit": "cans",
            "expiration_date": global_placeholder_date
        })

    def run_all(self):
        # Print Intro
        print(f"\nRunning Inventory Item Test:\n")
        for current_test in self.active_test:
            self.reset_testee()
            # Run Test
            current_test()

            print(f"[ {current_test.__name__} ]: Passed \u2713")
        print("")

    def reset_testee(self):
        self.testee = InventoryItem(**{
            "item_id": 5,
            "name": "Yerba Mate",
            "type": "DRINK",
            "price": 3.69,
            "purchase_date": global_placeholder_date,
            "quantity_bought": 5,
            "quantity_remaining": 2,
            "quantity_unit": "cans",
            "expiration_date": global_placeholder_date
        })

    def update_quantity_test(self):
        updated_quantity = 1
        self.testee.update_quantity(updated_quantity)

        assert self.testee.quantity_remaining == updated_quantity, \
            f"[ FILTER ]: Failed, \nGot: {self.testee.quantity_remaining} \nExpected: {updated_quantity}"

    def percentage_left_test(self):
        control = self.testee.quantity_remaining/self.testee.quantity_bought
        experimental = self.testee.percentage_left()

        assert experimental == control, \
            f"[ PERCENTAGE_LEFT ]: Failed, Got: {experimental} Expected: {control}"

    def is_finished_test(self):
        control = False
        experimental = self.testee.is_finished()

        assert experimental == control, \
            f"[ PERCENTAGE_LEFT ]: Failed, Got: {experimental} Expected: {control}"

    def display_sample(self):
        print(f"Inventory Item: \n", self.testee)


if __name__ == "__main__":
    GI_test = GroceryItemTest()
    II_test = InventoryItemTest()

    II_test.run_all()

    GI_test.display_sample()
    II_test.display_sample()
