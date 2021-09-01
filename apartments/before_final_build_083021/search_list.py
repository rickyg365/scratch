import random
import time

import json

from aprt_search import *

"""
This is gonna be an apartment list viewer later we can add the manager functionality for now,
it only takes in a list of urls as a text file, later we can create a front end 
and add urls and update the text file and such
"""

#
# def process_aprt_name(raw_aprt_name):
#     words = raw_aprt_name.split(' ')
#
#     file_name_word = words[0]
#
#     if file_name_word.lower() == 'the':
#         file_name_word = words[1]
#
#     return file_name_word.lower()


def save_json(filename, data):
    file_path = f"json/{filename}.json"

    # if file_path in already_exist:
    #     return False

    clean_data = json.dumps(data, indent=4)

    with open(file_path, 'w') as out_file:
        out_file.write(clean_data)

    return True


if __name__ == "__main__":
    # VARIABLES
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
    }

    # aprt_data, is to have the newly acquired data in an accessible format
    aprt_data = {}
    # choice list stores the apartment names also known as the keys to the apartment dict
    choice_list = []
    # this is a list of the raw data
    apartment_list_data = []

    with open('aprt_list.txt', 'r') as in_file:
        for i, line in enumerate(in_file):
            # display
            os.system('cls')
            print(f"Apartment #{i+1}")

            # search url for data
            new_data = search_aprt(line.strip(), headers)

            # if no data
            if new_data is None:
                print(f"[url failed]: {line}")
                input()
            else:
                # add to dictionary, w/ name as key, data as value
                key = new_data['name']
                aprt_data[key] = new_data

                # create list of names from apartment data keys (apartment name)
                choice_list.append(key)

                # add to list of data to be saved as json
                apartment_list_data.append(new_data)

                print(f"\n[SUCCESSFUL]: {key}")

            time.sleep(2)

    save_json('apartment_list', apartment_list_data)

    while True:
        os.system('cls')

        # print apartment choices
        print(f"[ Apartment List ]\n")

        for i, name in enumerate(choice_list):
            print(f"[{i + 1}]: {name}")

        # user input
        choice = input("\n>>> ")

        # Validate Input
        valid_choices = [str(i+1) for i in range(len(aprt_data))]
        exit_choices = [
            'q',
            'exit',
            'quit',
        ]

        if choice in exit_choices:
            # Quit Program
            print("\n[exiting program]\n")
            break

        if choice in valid_choices:
            # create key from choice
            choice_key = int(choice) - 1

            # select data to display
            choice_data = aprt_data.get(choice_list[choice_key])

            display_data(choice_data)

        input()
