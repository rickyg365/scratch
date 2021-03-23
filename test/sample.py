import os
import sys

import time
import math

import pytest

""" 
Program: Pytest trial
Author: rickyg3
Date: 03/21/2021
"""


# def count(start_number: int):
#     number = start_number
#     for i in range(start_number):
#         # print(f"{start_number-i}")
#         print(f"{number}")
#         if number < 0:
#             break
#         number -= 1
#     return number
#
#
# def test_count():
#     start = 5
#     assert count(start) == 0

def multiple_of(input_num):
    # Output container
    output_list = []

    # Create a dict of values w/ False as the initial value
    multiples = {}
    for i in range(input_num):
        multiples[f"{i+1}"] = False

    # Iterate through and check if multiple
    for current_num_string, status in multiples.items():
        current_num = int(current_num_string)

        # Number is multiple
        if input_num % current_num == 0:
            # Change status in dict
            multiples[current_num_string] = True
            # Add number to output list
            output_list.append(current_num)

    return output_list


if __name__ == "__main__":
    # 78 has more multiples than most can you find a number with more?
    number = int(input("\nPlease select a number: "))

    multiple_list = multiple_of(number)

    print(multiple_list)
