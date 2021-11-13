import os

import time
import random

import pandas as pd
from pyfiglet import Figlet

from termcolor import colored
from colorama import init
init()

from items import InventoryItem
from inventory import Inventory, InventoryAnalyzer
from csv_py_obj import read_csv


"""
This one is the front end basically

"""
"""
ideas:
 - provide graphics/charts for grocery data
    - total cost 
    - pie chart with categories (produce, dairy, junk, ...)
    - item "page" that displays all that items info in a nice format
 
 
special name convention:
   item - brand - flavor
 
special quantity convention:
   number of units - size per unit, or unit name
 
calculated values
   - total cost = total price of all items
   - time to consumption = date purchased - date finished, time it took to finish good
   - quantity needed = quantity purchased/(time to consumption/ 1 month), quantity of item needed to last the whole month
    
"""


def clear_screen():
    os.system("cls")


if __name__ == "__main__":
    # fonts: big, chunky, cosmic, doom, graffiti, isometric(1-4: good but way too big), larry3d, poison,
    # rectangles, slant, smisome1, standard
    # favs: smslant, banner3-D
    fig = Figlet(font="smslant")

    my_text = "   Grocery Manager"

    # show intro screen
    clear_screen()
    width, height = os.get_terminal_size()
    version = "Version 1.0, by @rickyg3"
    print("\n\n", colored(fig.renderText(my_text), "yellow"))

    print(colored(f"{version: ^{str(width)}}", "magenta"))
    # print(f"{'Coded by @rickyg3': ^{str(width)}}")

    # separator
    separator = colored(f"""{"="*width}""", "green")
    # usage
    # usage = colored(f"Usage: ", "red")
    # usage += colored(f"<option> <flag>\n", "blue")
    # flags
#     flags = colored(f"Available flags:\n", "red")
#     flags += colored(f"""
#     -m   Multiple
#     -s   Single
#     -p   Previous
# """, "blue")
    # Options
    options = colored(f"""Options:

 [1]  View item/s
 [2]  Find item/s
 [3]  Update item/s
 [4]  Status Report
 
 [F]  File options (export, save, load)
 [S]  Preferences (bar or no bar)
 [Q]  Quit program
""", "yellow")

    # add a help menu flag, -h,with examples; Example: 1 -m    (add multiple items)
    sample_menu = f"""
{separator}
{options}
"""
    print(sample_menu)
    print("loading...")
    data = read_csv()

    my_inventory = Inventory()
    analyzer = InventoryAnalyzer()

    for key, item in data.items():
        # for key, val in item.items():
        #     print(f"{key}: {val} {type(val)}")
        processed_item = InventoryItem(**item)
        processed_item.validate_types()
        # prepped_item = raw_item.validate_types()
        my_inventory.add_item(processed_item)

    user_input = input(colored("[+] Enter an option:  ", "green"))
    match user_input:
        case "1":
            clear_screen()
            print(my_inventory)
            input("\nPress ENTER to continue...")

        case "2":
            clear_screen()
            find_input = input("Select item id: ")
            print(my_inventory.find_item(int(find_input)))

        case "3":
            clear_screen()
            print("Update item")

        case "4":
            clear_screen()
            threshold_value = 0.8
            bar_width = width//2
            report = analyzer.summary_bar(my_inventory(), threshold_value, bar_width, sep="")

            print(f"\n[ Low Status Report ]  (< {threshold_value*100:.0f}%) : \n{width*'-'}\n", report)
            print(f"{width*'-'}\n")

        case "f":
            clear_screen()
            print("file options")

        case "s":
            clear_screen()
            print("Update preferences")

        case "q":
            print("\n[ Quitting Program ]\n")
