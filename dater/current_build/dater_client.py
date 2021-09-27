import os

from modules.date_api import *
from modules.itinerary import *

"""
Program: Date Chooser client interface [ version 1.1 ]
Author: Rickyg3
Date: 09/24/2021
"""


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
my_date_handler = DateHandler()
print(my_date_handler)

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
random_date = my_date_handler.select_random()
print(dictionary_print_format(random_date))

# Option 2
# my_date_handler.add_date()

# Option 3
date_key = ""
date_attribute = ""
date_value = ""

my_date_handler.edit_date(date_key, date_attribute, date_value)

# Option 4
date_key = ""

my_date_handler.remove_date(date_key)

# Option 5
new_file = ""

my_date_handler.load_data(new_file)


# Display result


if __name__ == "__main__":
    # clear_screen()
    ...
