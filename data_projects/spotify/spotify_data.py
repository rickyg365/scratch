import os

import pandas as pd
from dependency.load_csv import *

csv_file = 'data.csv'
# spotify_data = load_csv_json(csv_file, key_value="name")
# spotify_data = load_csv_raw(csv_file)


if __name__ == "__main__":
    spotify_data = pd.read_csv(csv_file)
    new_spotify_data = spotify_data.set_index('name')
    print(new_spotify_data)   # .info())  # no null, this lets us see what we need to fix in our data such as holes or null values
    # print(spotify_data.loc[[0, 1, 2, 3, 4]])
