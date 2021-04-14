import os
import sys

import csv
import pandas as pd


def load_csv_json(csv_filename):
    new_dict = {}
    with open(csv_filename, encoding='utf-8-sig') as csvf:
        rows = csv.DictReader(csvf)
        for row in rows:
            key = row['id']
            new_dict[key] = row
    return new_dict


if __name__ == "__main__":
    csv_file = 'sample.csv'
    pd_dataframe = pd.read_csv(csv_file)
    print(pd_dataframe)

    json_dict = load_csv_json(csv_file)

    # Data is a dictionary
    for id, data in json_dict.items():
        print(f"#{id}:")
        for keys, element in data.items():
            print(f"\t{keys.title()}: {element}")
