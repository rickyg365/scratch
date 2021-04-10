import os
import sys

import csv

from irl_items import *


''' 
    def load_complete(self, csv_file):
        self.complete_data = {}

        with open(csv_file, encoding='utf-8') as csvf:
            csvreader = csv.DictReader(csvf)

            for rows in csvreader:
                key = rows['Name']
                self.complete_data[key] = rows


'''
def load(csv_filename, key_index):
    final_data = {}

    with open(csv_filename, encoding='utf-8') as input_file:
        lines = csv.DictReader(input_file)

        for rows in lines:
            key = rows[f"{key_index}"]
            final_data[key] = rows
