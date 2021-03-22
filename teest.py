import os
import sys

import time

import pytest

""" 
Program: Pytest trial
Author: rickyg3
Date: 03/21/2021
"""


def count(start_number: int):
    number = start_number
    for i in range(start_number):
        # print(f"{start_number-i}")
        print(f"{number}")
        if number < 0:
            break
        number -= 1
    return number


def test_count():
    start = 5
    assert count(start) == 0

