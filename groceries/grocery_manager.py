import os

import time
import random

import pandas as pd
from pyfiglet import Figlet

from termcolor import colored
from colorama import init
init()

from utilities.grocery_api import *
from utilities.grocery_data_visualizer import *


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
    usage = colored(f"Usage: ", "red")
    usage += colored(f"<option> <flag>\n", "blue")
    # flags
    flags = colored(f"Available flags:\n", "red")
    flags += colored(f"""
    -m   Multiple
    -s   Single
    -p   Previous
""", "blue")
    # Options
    options = colored(f"""Options:

 [1]  Find item/s
 [2]  add item/s 
 [3]  remove item/s
 [4]  update item/s
 [5]  file options (export, save, load)
    
 [Q]  Quit program
""", "yellow")

    # add a help menu flag, -h,with examples; Example: 1 -m    (add multiple items)
    sample_menu = f"""
{separator}
{usage}
{flags}
{options}
"""
    print(sample_menu)
    input(colored("[+] Enter an option:  ", "green"))
