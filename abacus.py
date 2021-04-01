import os
import sys

import time
import math

""" 
Program: 
Author: rickyg3
Date: 03/29/2021
"""


""" 
Designs:

1. [classic]
    
    .---------------------.
    | [|] [|] [|] [|] [|] | 
    |  |   |   |   |   |  |
    |---------------------|
    |  |   |   |   |   |  |
    | [|] [|] [|] [|] [|] |
    | [|] [|] [|] [|] [|] |
    | [|] [|] [|] [|] [|] |
    | [|] [|] [|] [|] [|] |
    '---------------------'
    
    
2. [simple]

    # # # # #
    ---------
    # # # # #
    # # # # #
    # # # # #
    # # # # #
    
    Ex. 
    #: 176
              # #
        ---------
            # # #
              #  
    
"""


class Bead:
    def __init__(self, active=False):
        self.active = active

    def __str__(self):
        text = ""
        if self.active:
            text += "[|]"
        else:
            text += " | "

        return text


class Abacus:
    def __init__(self, num_columns=5):

        self.number = None
        self.length = 0

        self.beads = []
        self.columns = num_columns

        # initialize empty or full abacus
        for i in range(5):
            row = []
            for j in range(self.columns):
                # row.append(Bead(active=True))
                row.append(Bead())
            self.beads.append(row)

        # Set_number

    def __str__(self):
        text = "\n"

        # Top
        text += f".---------------------."

        # Top beads
        text += f"\n| "

        for bead in self.beads[0]:
            text += f"{bead} "

        text += f"|"

        # Divider
        text += f"\n|---------------------|"

        #  Bottom beads

        for i in range(1, 5):
            text += f"\n| "
            for j in range(self.columns):
                text += f"{self.beads[i][j]} "
            text += f"|"

        # Bottom
        text += f"\n'---------------------'"

        return text

    def set_number(self, number):
        # Process Number,  int -> str -> list
        #  I think this is unique to python, type conversion, I could also use floor division by 10 to get
        #  digit by digit and append it to the list
        digits = f"{number}"
        digits = list(digits)
        length = len(digits)

        self.number = digits
        self.length = length

        # Check if number length is greater than the abacus column number
        if self.length > self.columns:
            print("HugeNumberERROR: need more columns for that number ")
        else:
            diff = self.columns - self.length
            count = 0

            for i in range(diff, 5):
                current_num = int(self.number[count])
                if current_num >= 5:
                    self.beads[0][i].active = True
                    current_num -= 5
                if current_num > 0:
                    # print(current_num)
                    for n in range(current_num):
                        self.beads[n+1][i].active = True
                count += 1


if __name__ == "__main__":
    # a = Abacus()
    # print(a)
    run = True

    while run:
        a = Abacus()
        os.system("clear")
        user_num = input("Please select a number: ")
        a.set_number(user_num)
        print(a)
        input("Again? ")
