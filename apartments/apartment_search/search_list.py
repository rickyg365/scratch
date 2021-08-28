import random
import time

from aprt_search import *

"""
This is gonna be an apartment list viewer later we can add the manager functionality for now,
it only takes in a list of urls as a text file, later we can create a front end 
and add urls and update the text file and such
"""

if __name__ == "__main__":

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
    }

    aprt_data = {}

    with open('aprt_list.txt', 'r') as in_file:
        for i, line in enumerate(in_file):
            os.system('cls')
            print(f"Apartment #{i+1}")
            new_data = search_aprt(line.strip(), headers)

            if new_data is None:
                print(f"[url failed]: {line}")
                input()
            else:
                # Add to dictionary with name as key
                key = new_data['name']
                aprt_data[key] = new_data

                print(f"\n[SUCCESSFUL]: {key}")

            time.sleep(2)

    # create list of names from apartment data keys (apartment name)
    choice_list = []

    for name in aprt_data:
        choice_list.append(name)

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
