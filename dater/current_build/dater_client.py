import os

from modules.date_api import *
from modules.itinerary import *

"""
Program: Date Chooser client interface [ version 1.1 ]
Author: Rickyg3
Date: 09/24/2021
"""

'''
Add saving of which data has been seen already
'''


def clear_screen():
    # Add self checking of operating system so that appropriate command is chosen
    """
    Example:
        cases = {
            'windows': 'cls',
            'linux': 'clear',
            'mac': 'clear'
        }
    """
    os.system('cls')


# Create DateHandler instance using default filepath, reads data from json and loads into working memory
# my_date_handler = DateHandler()
# print(my_date_handler)

# present user with options
'''
Multiple Screen EXAMPLE:
SCREEN 1

    [1]: Choose Random Date
    [2]: Interact with date data

SCREEN 2

    Show list of all dates
    
    [2]: Add Date
    [3]: Edit Date
    [4]: Remove Date
    [5]: Select different database file


EXAMPLE:

    [1]: Choose Random Date
    [2]: Add Date
    [3]: Edit Date
    [4]: Remove Date
    [5]: Select different database file
    
>>> #user-input#

or could add in a login just for fun lmfao

[user_name]: #user-input#

'''
# Process Action using date_api methods

# Option 1
# random_date = my_date_handler.select_random()
# print(dictionary_print_format(random_date))

# Option 2
# my_date_handler.add_date()

# Option 3
# date_key = ""
# date_attribute = ""
# date_value = ""
#
# my_date_handler.edit_date(date_key, date_attribute, date_value)
#
# # Option 4
# date_key = ""
#
# my_date_handler.remove_date(date_key)
#
# # Option 5
# new_file = ""
#
# my_date_handler.load_data(new_file)


# Display result

if __name__ == "__main__":
    title = "\nDate Selector Program [ Version 1.0 ]\n"
    main_menu = f"\n [1]: Choose Random Date\n [2]: Interact with date data\n [q]: Quit"
    data_menu = f"\n [1]: Add Date\n [2]: Edit Date\n [3]: Remove Date\n [4]: Select different database file\n [q]: Quit"

    date_handler = DateHandler()

    current_menu = main_menu

    while True:
        clear_screen()
        print(title)
        print(current_menu)

        user_input = input("\n>>> ")

        menu_flag = False if current_menu == data_menu else True

        if menu_flag:
            if user_input.lower() == 'q':
                print("\n[ exiting program ]\n")
                break
            if user_input == '1':
                random_date = date_handler.select_random()
                print(dictionary_print_format(random_date))
                input("")
            if user_input == '2':
                current_menu = data_menu

        else:
            if user_input.lower() == 'q':
                print("[ exiting program ]")
                current_menu = main_menu
            if user_input == '1':
                clear_screen()

                print(f"\nLet's make a new date obj!")
                date_name = input("\nName: ")
                date_location = input("Location: ")
                date_cost = input("Cost: ")
                date_transport = input("Transportation: ")

                new_date_obj = {
                    "name": date_name,
                    "visited": 0,
                    "location": date_location,
                    "schedule": "NaN",
                    "transport": date_transport,
                    "cost": date_cost,
                    "itinerary": "NaN"
                }
                correct = input(f"Does this look right?\n{dictionary_print_format(new_date_obj)}\n>>>")
                # if correct.lower() == 'y':
                # add functionality to check later
                date_handler.add_date(
                    name=date_name,
                    location=date_location,
                    transport=date_transport,
                    cost=date_cost
                )

            if user_input == '2':
                # Edit date
                clear_screen()

                date_name = input("\nName: ")
                attribute = input("What would you like to edit?: ")
                updated_value = input("New Value: ")

                key = date_handler.search_by_name(date_name)

                if key is None:
                    input("\nCould not find date")
                    continue

                date_handler.edit_date(
                    date_key=key,
                    attribute_name=attribute,
                    new_value=updated_value
                )

                input(f"{date_name} successfully added!")

            if user_input == '3':
                # Remove date
                clear_screen()

                date_name = input("\nName: ")

                key = date_handler.search_by_name(date_name)

                if key is None:
                    input("\nCould not find date")
                    continue

                date_handler.remove_date(key)

                input(f"{date_name} successfully removed!")

            if user_input == '4':
                # Change file path
                clear_screen()

                new_file_path = input("\nEnter new file path: ")

                # Maybe add some validation for the file path in the future

                date_handler.load_data(new_file_path)
