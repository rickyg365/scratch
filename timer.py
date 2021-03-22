import os
import sys

import time
import datetime

""" 
Program: Timer
Author: riptutorial.com reference
Date: 03/21/2021
"""


def timer(func):
    def inner(*args, **kwargs):
        t1 = time.time()
        # print(f"start time: {t1}\n")
        f = func(*args, **kwargs)
        t2 = time.time()
        # print(f"\nend time: {t2}\n")
        print(f"Runtime took {t2 - t1} seconds")
        return f
    return inner


if __name__ == "__main__":
    @timer
    def example_function():
        time.sleep(1.55)

    example_function()
