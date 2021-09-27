import os

"""
Program:
Author:
Date:
"""


# Variables
import os

import pandas as pd

"""
Can load json with pandas to get a dataframe object
or with the json module to get a dictionary
"""


# Functions
def load_csv(file_path="default.csv"):
    try:
        # index_col = 0 saves the row names
        loaded_data = pd.read_csv(file_path, index_col=0)

        return loaded_data

    except Exception as e:
        print(e)


def save_csv(input_data, file_path="default.csv"):
    try:
        input_data.to_csv(file_path)
    except Exception as e:
        print(e)


def make_dataframe(input_dict, index=None):
    """ make a data frame """

    output_dframe = pd.DataFrame(input_dict)

    if index == 'default':
        return output_dframe

    indexes = []

    if index is None:
        # build index, assuming all data points have same size value list

        first_row_index = list(input_dict.keys())[0]

        for i in range(len(input_dict[first_row_index])):
            indexes.append(f"{i + 1}")

    output_dframe.index = indexes

    return output_dframe


# TESTING


def test_make_dataframe():
    data = {
        'A': ['val 1', 'val 2', 'val 3', 'val 4', 'val 5', 'val 6', 'val 7', 'val 8', 'val 9'],
        'B': ['val 1', 'val 2', 'val 3', 'val 4', 'val 5', 'val 6', 'val 7', 'val 8', 'val 9'],
        'C': ['val 1', 'val 2', 'val 3', 'val 4', 'val 5', 'val 6', 'val 7', 'val 8', 'val 9'],
        'D': ['val 1', 'val 2', 'val 3', 'val 4', 'val 5', 'val 6', 'val 7', 'val 8', 'val 9'],
        'E': ['val 1', 'val 2', 'val 3', 'val 4', 'val 5', 'val 6', 'val 7', 'val 8', 'val 9'],
        'F': ['val 1', 'val 2', 'val 3', 'val 4', 'val 5', 'val 6', 'val 7', 'val 8', 'val 9'],
        'G': ['val 1', 'val 2', 'val 3', 'val 4', 'val 5', 'val 6', 'val 7', 'val 8', 'val 9'],
        'H': ['val 1', 'val 2', 'val 3', 'val 4', 'val 5', 'val 6', 'val 7', 'val 8', 'val 9'],
        'I': ['val 1', 'val 2', 'val 3', 'val 4', 'val 5', 'val 6', 'val 7', 'val 8', 'val 9']
    }

    df = make_dataframe(data)

    print(df)


if __name__ == "__main__":
    current_data = load_csv()

    print(current_data)

    # test_make_dataframe()
