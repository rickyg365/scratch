import os

from grocery_item_model import GroceryItem, ActiveItem

terminal_width, terminal_height = os.get_terminal_size()


def test_result(test_name="TEST", status=False):
    base = f"[ {test_name} ]: "
    status_msg = "Failed"
    
    if status:
        status_msg = "Passed"
    
    return f"{base}{status_msg}"



def test_grocery_item(debug=True):
    # Works (Partial Data)

    raw_item_data = {
        "id": 0,
        "name": "str",
        "description": "str",
        "brand": "str",
        "tags": ["str1", "str2"]
    }

    new_item = GroceryItem(**raw_item_data)

    print(test_result("GroceryItem", True))

    if debug:
        print(f"\nGrocery Item:\n{new_item}\n")


def test_active_item(debug=True):
    # Works (Partial Data)

    raw_item_data = {
        "id": 0,
        "name": "str",
        "description": "str",
        "brand": "str",
        "tags": ["str1", "str2"],
        "price": 10.00,
        "store": "str",
        "quantity": 1,
        "quantity_unit": "str",
    }

    new_item = ActiveItem(**raw_item_data)
    
    print(test_result("ActiveItem", True))

    if debug:
        print(f"\nActive Item:\n{new_item}\n")


def main():
    DEBUG=True

    run_test = lambda x: x(DEBUG)
    test_list = [
        test_grocery_item, 
        test_active_item
    ]

    for current_test in test_list:
        # Run Test
        run_test(current_test)
        
    

if __name__ == "__main__":
    main()

