import os
import sys

import time

import pytest
from sample import *

""" 
Program: Test for sample.py
Author: rickyg3
Date: 03/22/2021
"""


class TestMultiple:
    TEST_CASES = {
        20: [1, 2, 4, 5, 10, 20],
        23: [1, 23],
        29: [1, 29],
        50: [1, 2, 5, 10, 25, 50],
        78: [1, 2, 3, 6, 13, 26, 39, 78]
    }

    def test_multiple_of(self):
        for case, expected in self.TEST_CASES.items():
            assert multiple_of(case) == self.TEST_CASES[case]
