import os
import sys

import time
import random

import pytest

""" 
Program: Math Rock (Dice)
Author: rickyg3
Date: 03/26/2021
"""

''' 
Designs:

 1. 
    .---------.
    |         |
    |    *    |
    |         |
    '---------'
    
    .---------.
    |         |
    |  *   *  |
    |         |
    '---------'
    
    .---------.
    | *       |
    |    *    |
    |       * |
    '---------'
    
    .---------.
    | *     * |
    |         |
    | *     * |
    '---------'
    
    .---------.
    | *     * |
    |    *    |
    | *     * |
    '---------'
    
    .---------.
    | *     * |
    | *     * |
    | *     * |
    '---------'
    
 2.
    [     ]
    [  *  ]
    [     ]
    
    [     ]
    [ * * ]
    [     ]
    
    [*    ]
    [  *  ]
    [    *]
    
    [*   *]
    [     ]
    [*   *]
    
    
    [*   *]
    [  *  ]
    [*   *]
    
    [*   *]
    [*   *]
    [*   *]

    
'''


def clear_screen():
    os.system("cls")


def getDiceGraphics(dice_num):
    data = []
    if dice_num == 1:
        data = [
            f".-----------.",
            f"|           |",
            f"|           |",
            f"|     *     |",
            f"|           |",
            f"|           |",
            f"'-----------'"
        ]

    elif dice_num == 2:
        data = [
            f".-----------.",
            f"|           |",
            f"|           |",
            f"|  *     *  |",
            f"|           |",
            f"|           |",
            f"'-----------'"
        ]
    elif dice_num == 3:
        data = [
            f".-----------.",
            f"| *         |",
            f"|           |",
            f"|     *     |",
            f"|           |",
            f"|         * |",
            f"'-----------'"
        ]

    elif dice_num == 4:
        data = [
            f".-----------.",
            f"| *       * |",
            f"|           |",
            f"|           |",
            f"|           |",
            f"| *       * |",
            f"'-----------'"
        ]
    elif dice_num == 5:
        data = [
            f".-----------.",
            f"| *       * |",
            f"|           |",
            f"|     *     |",
            f"|           |",
            f"| *       * |",
            f"'-----------'"
        ]
    elif dice_num == 6:
        data = [
            f".-----------.",
            f"| *       * |",
            f"|           |",
            f"| *       * |",
            f"|           |",
            f"| *       * |",
            f"'-----------'"
        ]
    else:
        print("Invalid Value")
        data = ["empty"]
    return data


class Dice:
    def __init__(self, value=None, dtype=6):
        """
        Dice Object
        1. Dice object as a container, new_dice =  Dice(value, dice_type) the graphic in this case, rows of strings
        2. Dice object to make it easier to create a dice object. internally stores all possible rows of strings
        """
        self.value = value
        self.display = []
        self.dtype = dtype

        self.load(value)

    def __str__(self):
        text = ""
        for row in self.display:
            text += f"{row}"
        return text

    def __add__(self, other, spacing=1):
        new_display = []
        if len(self.display) == len(other.display):
            for r in range(len(self.display)):
                line = self.display[r] + spacing*' ' + other.display[r]
                new_display.append(line)
            return new_display
        else:
            print("Unable to add")
        return []

    def print(self):
        for row in self.display:
            print(row)

    def load(self, new_value):
        self.value = new_value

        if self.value is not None and self.dtype == 6:
            try:
                self.display = getDiceGraphics(self.value)
            except NameError:
                self.display = [f"[{self.value}]"]
        elif self.value is None:
            self.randomize()
        else:
            self.display = [f"[{self.value}]"]

    def randomize(self):
        r = random.randint(1, self.dtype)

        self.load(r)


class DiceCollection:
    def __init__(self, new_dice=None):
        self.dice = []
        if new_dice is None:
            length = 0
        else:
            length = 1

            self.dice.append(new_dice)

        self.length = length

    def __str__(self):
        pass

    def add_dice(self, new_dice):
        self.dice.append(new_dice)

    def show(self):
        count = 0
        dice_holder = Dice(dtype=6)

        for dice in self.dice:
            dice_holder.display = dice_holder + dice
            dice_holder.value = dice_holder.value + dice.value

        dice_holder.print()


class DiceGame:
    def __init__(self):
        """
        Dice Game base class
        """
        self.score = 0
        self.running = True

    def __str__(self):
        text = ""
        return text

    def run(self):
        while self.running:
            sys.stdout.write(f"running...\r")


if __name__ == '__main__':

    run = True

    num_dice = int(input("How many dice?: "))
    dice_type = int(input("Dice Type: d"))

    cur_dice = {}

    while run:
        clear_screen()

        for i in range(num_dice):
            cur_dice[f"d{i+1}"] = Dice(dtype=dice_type)

        # Randomize and Print
        for dice_name, dice_obj in cur_dice.items():
            dice_obj.randomize()

            if dice_obj.dtype == 6:
                dice_obj.print()
            else:
                print(f"{dice_name}: \t{dice_obj}")

        a = input("\nAgain?: ")
        if a.lower() == 'q' or a.lower() == 'n':
            run = False


