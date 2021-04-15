import os

import pandas as pd
from dependency.load_csv import *


csv_file = 'Minerals_Database.csv'
# mineral_data = load_csv_json(csv_file, key_value="Name")
# mineral_data = load_csv_raw(csv_file)

if __name__ == "__main__":
    mineral_data = pd.read_csv(csv_file)
    print(mineral_data)
