import os

import pandas as pd

"""
Can load json with pandas to get a dataframe object
or with the json module to get a dictionary
"""


def load_data(file_path="default.csv"):
    loaded_data = pd.read_csv(file_path)

    # string_repr = loaded_data.to_string()

    # can add data processing here

    return loaded_data


def save_data(input_data, file_path="default.csv"):
    try:
        input_data.to_csv(file_path)
    except Exception as e:
        print(e)


def check_data(input_data):

    return True


if __name__ == "__main__":
    # data = {
    #     'd1': 'val 1',
    #     'd2': 'val 2',
    #     'd3': 'val 3',
    #     'd4': 'val 4',
    #     'd5': 'val 5',
    #     'd6': 'val 6',
    #     'd7': 'val 7',
    #     'd8': 'val 8',
    #     'd9': 'val 9'
    # }
    #
    # df = pd.DataFrame(data.values(), index=data.keys())


    ''' make a data frame'''
    # data = {
    #     'A': ['val 1', 'val 2', 'val 3', 'val 4', 'val 5', 'val 6', 'val 7', 'val 8', 'val 9'],
    #     'B': ['val 1', 'val 2', 'val 3', 'val 4', 'val 5', 'val 6', 'val 7', 'val 8', 'val 9'],
    #     'C': ['val 1', 'val 2', 'val 3', 'val 4', 'val 5', 'val 6', 'val 7', 'val 8', 'val 9'],
    #     'D': ['val 1', 'val 2', 'val 3', 'val 4', 'val 5', 'val 6', 'val 7', 'val 8', 'val 9'],
    #     'E': ['val 1', 'val 2', 'val 3', 'val 4', 'val 5', 'val 6', 'val 7', 'val 8', 'val 9'],
    #     'F': ['val 1', 'val 2', 'val 3', 'val 4', 'val 5', 'val 6', 'val 7', 'val 8', 'val 9'],
    #     'G': ['val 1', 'val 2', 'val 3', 'val 4', 'val 5', 'val 6', 'val 7', 'val 8', 'val 9'],
    #     'H': ['val 1', 'val 2', 'val 3', 'val 4', 'val 5', 'val 6', 'val 7', 'val 8', 'val 9'],
    #     'I': ['val 1', 'val 2', 'val 3', 'val 4', 'val 5', 'val 6', 'val 7', 'val 8', 'val 9']
    # }
    #
    # # make index
    # # assuming all data points have same size value list
    # indexes = []
    # first_row = list(data.keys())[0]
    # for i in range(len(data[first_row])):
    #     indexes.append(f"{i+1}")
    #
    # df = pd.DataFrame(data, index=indexes)
    # print(df)

    my_data = load_data()
    # save_data(df)

    print('\nData Frame:\n', my_data.head(3))

    row_one = my_data.loc[1]
    print('\nFirst Row:\n', row_one, row_one.dtype)

    one = my_data.loc[1]['A']
    print('\nFirst Value:\n', one)

