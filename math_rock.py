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

    def __add__(self, other):
        return

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


class DiceGame:
    def __init__(self):
        """
        Dice Game base class
        """
        self.score = 0

    def __str__(self):
        text = ""
        return text


if __name__ == '__main__':
    run = True

    num_dice = 4
    cur_dice = {}

    start = 3
    dice = Dice(start)
    d20 = Dice(dtype=20)
    d500 = Dice(dtype=500)

    while run:
        os.system("clear")

        for i in range(num_dice):
            cur_dice[f"d{i+1}"] = Dice(dtype=6)

        # Randomize and Print
        for dice_name, dice_obj in cur_dice.items():
            dice_obj.randomize()
            # print(f"{dice_name}: \t{dice_obj}")
            dice_obj.print()

        # Randomize Dice
        # dice.randomize()
        # d20.randomize()
        # d500.randomize()
        #
        # Print Dice
        # dice.print()
        # d20.print()
        # d500.print()

        a = input("\nAgain?: ")
        if a.lower() == 'q' or a.lower() == 'n':
            run = False


