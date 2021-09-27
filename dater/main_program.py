import os
from rand_dt import *

"""
Program: Dater program
Author:
Date:
"""


# Variables


# Functions
def func():
    return


# Classes
class ClassName:
    def __init__(self):
        self.var = ""

    def __str__(self):
        text = ""
        return text


if __name__ == "__main__":
    # Create date manager obj

    date_data_path = 'dates.json'
    completed_data_data_path = 'visited_dates.json'

    date_selector = DateManager(date_data_path, completed_data_data_path)

    random_date = date_selector.select_random()

    # mark date as complete and add a timestamp
    date_selector.complete_activity(random_date['name'])

    # save any new data added to dates.json
    date_selector.save_dates()

    # show status
    print(date_selector)
