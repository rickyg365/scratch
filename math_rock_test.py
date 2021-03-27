import os
import sys

import time

import pytest
from math_rock import *

""" 
Program: Test for math_rock.py
Author: rickyg3
Date: 03/27/2021
"""


dice_a = Dice(dtype=6)
dice_b = Dice(dtype=6)
dice_c = Dice(dtype=6)
dice_d = Dice(dtype=6)
dice_e = Dice(dtype=6)
dice_f = Dice(dtype=6)

my_collection = DiceCollection(dice_a)
my_collection.add_dice(dice_b)
my_collection.add_dice(dice_c)
my_collection.add_dice(dice_d)
my_collection.add_dice(dice_e)
my_collection.add_dice(dice_f)

my_collection.show()


# class TestDice:
#     """
#     dice_a = Dice(dtype=6)
#     dice_b = Dice(dtype=6)
#     list_of_dice = [dice_a, dice_b]
#
#     for d in list_of_dice:
#         d.print()
#         print("")
#
#     new_d = Dice(dtype=6)
#
#     # new_d.display = dice_a + dice_b
#     new_d.display = dice_a.__add__(dice_b, spacing=15)
#
#     # print(new_d)
#     new_d.print()
#
#     """
#     TEST_CASES = {
#         20: [1, 2, 4, 5, 10, 20],
#         23: [1, 23],
#         29: [1, 29],
#         50: [1, 2, 5, 10, 25, 50],
#         78: [1, 2, 3, 6, 13, 26, 39, 78]
#     }
#
#     def test_add(self):
#         for case, expected in self.TEST_CASES.items():
#             assert multiple_of(case) == self.TEST_CASES[case]
