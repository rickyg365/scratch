from items import GroceryItem
from Inventory import Inventory


class TestInventory:
    """ Unit Test: Test component,  Integration Test: test together """
    def __init__(self):
        # Test that will be run during run_test method
        self.active_test = [
            self.add_item_test,
            self.remove_item_test,
            self.find_item_test
        ]

        # Reference Data
        self.sample_grocery_obj = GroceryItem(**{
            "item_id": 5,
            "name": "Yerba Mate",
            "type": "DRINK",
            "price": 3.69
        })

        self.sample_grocery_obj_list = [
            GroceryItem(**{
                "item_id": 1,
                "name": "Carrots",
                "type": "PRODUCE",
                "price": 1.25
            }),
            GroceryItem(**{
                "item_id": 2,
                "name": "Ground Beef",
                "type": "MEAT",
                "price": 9.24
            }),
            GroceryItem(**{
                "item_id": 3,
                "name": "Milk",
                "type": "DAIRY",
                "price": 3.45
            })
        ]

        # Create Standard Inventory
        self.testee = Inventory()

        for test_item in self.sample_grocery_obj_list:
            self.testee.add_item(test_item)

    def run_test(self):
        # Print Intro
        print(f"\nRunning Test:\n")
        for current_test in self.active_test:
            # Reset Test Object
            self.reset_testee()

            # Run Test
            current_test()
            print(f"[\u2713] {current_test.__name__}: Passed")
        print("")

    def reset_testee(self):
        """ Recreates a new default Test Inventory using provided data """
        self.testee = Inventory()

        for test_item in self.sample_grocery_obj_list:
            self.testee.add_item(test_item)

    def add_item_test(self):
        """ Test Inventory.add_item(GroceryObj(**item_data)) method """
        # Expected Output
        add_item_list = [
            *self.sample_grocery_obj_list,
            self.sample_grocery_obj
        ]

        # Test Steps
        self.testee.add_item(self.sample_grocery_obj)

        # Test Assertion
        assert self.testee.length == 4, f"Incorrect Length, gave {self.testee.length} instead of 4"
        assert self.testee.items == add_item_list, \
            f"Failed to add item:\n\nActual: \n{self.testee.items}\n\nExpected: \n{add_item_list}\n"

    def remove_item_test(self):
        """ Test Inventory.remove_item(item_id) method """
        # Expected Output
        remove_item_list = [
            GroceryItem(**{
                "item_id": 1,
                "name": "Carrots",
                "type": "PRODUCE",
                "price": 1.25
            }),
            GroceryItem(**{
                "item_id": 3,
                "name": "Milk",
                "type": "DAIRY",
                "price": 3.45
            })
        ]

        # Test Steps
        self.testee.remove_item(2)

        # Test Assertion
        assert self.testee.length == 2, f"Incorrect Length, gave {self.testee.length} instead of 2"
        assert self.testee.items == remove_item_list, \
            f"Failed to remove item\n\nActual: \n{self.testee.items}\n\nExpected: \n{remove_item_list}\n"

    def modify_item_test(self):
        pass

    def find_item_test(self):
        # Expected Output
        sample_output_obj = GroceryItem(**{
                "item_id": 1,
                "name": "Carrots",
                "type": "PRODUCE",
                "price": 1.25
            })

        # Test Steps
        return_obj = self.testee.find_item(1)

        # Test Assertion
        assert return_obj == sample_output_obj, \
            f"Failed to find item\nActual: \t{return_obj}\nExpected: \t{sample_output_obj}"


if __name__ == "__main__":
    # Create test object
    test = TestInventory()

    # Run Tests
    test.run_test()
