import os

import pandas as pd
from dependency.load_csv import *

csv_file = 'data.csv'
# spotify_data = load_csv_json(csv_file, key_value="name")
# spotify_data = load_csv_raw(csv_file)


if __name__ == "__main__":
    spotify_data = pd.read_csv(csv_file)
    # .info())  # no null, this lets us see what we need to fix in our data such as holes or null values
    print(spotify_data)
    # print(spotify_data.loc[[0, 1, 2, 3, 4]])

    # Search for a song
    new_spotify_data = spotify_data.set_index('name')
    song_name = "The One"
    print(new_spotify_data.loc[song_name])

    # search for an artist
    # Need to use regex because artists names have brackets and different quotation marks, or I can clean the data hehe
    artist_spotify_data = spotify_data.set_index('artists')
    print(artist_spotify_data)
    # This is a work around but we could probably clean the data to remove unnecessary characters
    raw_artist_name = "Screamin' Jay Hawkins"
    if "'" in raw_artist_name:
        artist_name = f'["{raw_artist_name}"]'
    else:
        artist_name = f"['{raw_artist_name}']"

    print(artist_spotify_data.loc[artist_name])
