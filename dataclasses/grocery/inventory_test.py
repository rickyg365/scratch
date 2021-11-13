import os
from datetime import datetime

from items import GroceryItem, InventoryItem
from inventory import Inventory, InventoryAnalyzer


global_placeholder_date = datetime.strptime('Jan 1 2005 20:13:50', '%b %d %Y %H:%M:%S')


class InventoryTest:
    def __init__(self):

        # Test that will be run during run_test method
        self.active_test = [
            self.add_item_test,
            self.remove_item_test,
            self.find_item_test
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

        # sample_inventory_items = [
        #     {
        #         "item_id": 1,
        #         "name": "Carrots",
        #         "type": "PRODUCE",
        #         "price": 1.25,
        #         "purchase_date": global_placeholder_date,
        #         "quantity_bought": 5,
        #         "quantity_remaining": 2,
        #         "quantity_unit": "indv",
        #         "expiration_date": global_placeholder_date
        #     },
        #     {
        #         "item_id": 2,
        #         "name": "Ground Beef",
        #         "type": "MEAT",
        #         "price": 9.24,
        #         "purchase_date": global_placeholder_date,
        #         "quantity_bought": 1,
        #         "quantity_remaining": 1,
        #         "quantity_unit": "package",
        #         "expiration_date": global_placeholder_date
        #     },
        #     {
        #         "item_id": 3,
        #         "name": "Milk",
        #         "type": "DAIRY",
        #         "price": 3.45,
        #         "purchase_date": global_placeholder_date,
        #         "quantity_bought": 1,
        #         "quantity_remaining": 1,
        #         "quantity_unit": "gallon",
        #         "expiration_date": global_placeholder_date
        #     },
        #     {
        #         "item_id": 4,
        #         "name": "Buttermilk Bread",
        #         "type": "BREAD",
        #         "price": 5.45,
        #         "purchase_date": global_placeholder_date,
        #         "quantity_bought": 2,
        #         "quantity_remaining": 1,
        #         "quantity_unit": "loaf",
        #         "expiration_date": global_placeholder_date
        #     },
        #     {
        #         "item_id": 5,
        #         "name": "Onions",
        #         "type": "PRODUCE",
        #         "price": 3.15,
        #         "purchase_date": global_placeholder_date,
        #         "quantity_bought": 3,
        #         "quantity_remaining": 2,
        #         "quantity_unit": "indv",
        #         "expiration_date": global_placeholder_date
        #     }
        # ]

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
        # Create Standard Inventory
        self.testee = Inventory()

        for test_item in self.sample_inventory_objs:
            self.testee.add_item(test_item)

    def run_all(self):
        # Print Intro
        print(f"\nRunning Inventory Test:\n")
        for current_test in self.active_test:
            # Reset Test Object
            self.reset_testee()

            # Run Test
            current_test()
            print(f"[\u2713] {current_test.__name__}: Passed")
        print("")

    def reset_testee(self):
        """ Recreates a new default Test Inventory using provided data """
        # Create Standard Inventory
        self.testee = Inventory()

        for test_item in self.sample_inventory_objs:
            self.testee.add_item(test_item)

    def add_item_test(self):
        """ Test Inventory.add_item(GroceryObj(**item_data)) method """
        # Expected Output
        add_item_list = [
            *self.sample_inventory_objs,
            self.sample_inventory_item
        ]

        # Test Steps
        self.testee.add_item(self.sample_inventory_item)

        # Test Assertion
        assert self.testee.length == 6, f"Incorrect Length, gave {self.testee.length} instead of 6"
        assert self.testee.items == add_item_list, \
            f"Failed to add item:\n\nActual: \n{self.testee.items}\n\nExpected: \n{add_item_list}\n"

    def remove_item_test(self):
        """ Test Inventory.remove_item(item_id) method """
        # Expected Output
        remove_item_list = [
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

        # Test Steps
        self.testee.remove_item(2)

        # Test Assertion
        assert self.testee.length == 4, f"Incorrect Length, gave {self.testee.length} instead of 4"
        assert self.testee.items == remove_item_list, \
            f"Failed to remove item\n\nActual: \n{self.testee.items}\n\nExpected: \n{remove_item_list}\n"

    def modify_item_test(self):
        pass

    def find_item_test(self):
        # Expected Output
        sample_output_obj = InventoryItem(**{
                "item_id": 1,
                "name": "Carrots",
                "type": "PRODUCE",
                "price": 1.25,
                "purchase_date": global_placeholder_date,
                "quantity_bought": 5,
                "quantity_remaining": 2,
                "quantity_unit": "indv",
                "expiration_date": global_placeholder_date
            })

        # Test Steps
        return_obj = self.testee.find_item(1)

        # Test Assertion
        assert return_obj == sample_output_obj, \
            f"Failed to find item\nActual: \t{return_obj}\nExpected: \t{sample_output_obj}"

    def remove_empty_test(self):
        # Clear Empty
        # my_inventory.remove_empty()
        # my_inventory.pretty_print(width)
        # print("\n")
        pass

    def display_sample(self, width):
        # Get Terminal Dimensions
        print(f"")

        # Create new blank inventory
        self.reset_testee()

        # Display Current Inventory
        self.testee.pretty_print(width)
        print(f"\nRemoved Item")

        # Edit Inventory
        self.testee.remove_item(2)

        # Display New Inventory
        self.testee.pretty_print(width)

        # Item Lookup
        print(f"\n[ Item Lookup ]\n{width * '-'}")

        # Python anti pattern, find the best way to handle this.
        # null_data = lambda x: "Item not found" if x is None else x

        search = self.testee.find_item(3)
        print("Item not found" if search is None else search)

        fail_search = self.testee.find_item(2)
        print("Item not found" if fail_search is None else fail_search)

        print("")


class AnalyzerTest:
    def __init__(self):
        # Test that will be run during run_test method
        self.active_test = [
            self.filter_test,
            # self.summary_test,
            # self.summary_bar_test
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

        # Create Standard Inventory
        self.testee = InventoryAnalyzer()

    def run_all(self):
        # Print Intro
        print(f"\nRunning Analyzer Test:\n")
        for current_test in self.active_test:
            # Run Test
            current_test()

            print(f"[ {current_test.__name__} ]: Passed \u2713")
        print("")

    def filter_test(self):
        reference_list = [
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

        produce_filtered_list = self.testee.filter(self.sample_inventory_objs, lambda x: x.type == "PRODUCE")

        assert produce_filtered_list == reference_list, \
            f"[ FILTER ]: Failed, \nGot: {produce_filtered_list} \nExpected: {reference_list}"

    def summary_test(self):

        report = self.testee.summary(self.sample_inventory_objs, threshold=0.8)

        print(f"[ SUMMARY ]:\n{report}")
        pass_test = input("Does this look right?: ")

        if pass_test in "nN":
                print(f"[ SUMMARY ]: Failed")
                return False
        return True

    def display_sample(self, width):
        sample_inventory = [
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
        # Analyze Inventory
        my_report1 = self.testee.summary(sample_inventory, 0.8)
        my_report2 = self.testee.summary_bar(sample_inventory, 0.8, console_width=width // 2, sep="")

        print(f"Low Summary Report: \n{width * '-'}", my_report1)

        print(f"Low Summary Report w/ bar: \n{width * '-'}", my_report2)

        # Filter Inventory -> returns temp copy doesnt actually mutate, this is useful for data
        filtered_items = self.testee.filter(sample_inventory, lambda x: x.type == "PRODUCE")
        print(f"Filtered items: \n{width * '-'}")

        for item in filtered_items:
            print(item)

        last_report = self.testee.summary_bar(filtered_items, 1, console_width=width // 2, sep="")

        print(f"\nLast Low Summary Bar Report w/ filtered items: \n{width * '-'}", last_report)


if __name__ == "__main__":
    # Get Terminal Dimensions
    console_width, height = os.get_terminal_size()

    # Create test object
    test = InventoryTest()

    test.run_all()

    # Show Sample output
    test.display_sample(console_width)

    print(f"{console_width * '-'}")

    # Create Analyzer test object
    analyzer_test = AnalyzerTest()

    analyzer_test.run_all()

    # Show Sample output
    analyzer_test.display_sample(console_width)
