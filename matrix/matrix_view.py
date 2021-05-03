import os

import time

import random
import logging

from matrix import *


def clear_screen():
    os.system('cls')


if __name__ == "__main__":
    # Configure Log
    logging.basicConfig(filename='matrix_log.log',
                        filemode='w',
                        datefmt='[%m-%d-%Y]:%H:%M:%S ',
                        format='%(asctime)s:%(name)s: %(levelname)s: %(message)s',
                        level=logging.DEBUG)

    # Loggers
    main_log = logging.getLogger(__name__)

    title = "[Random Matrix Generator]"
    options = '''
[G]: Generate Random Matrix
[C]: Custom Matrix    
[L]: Check Log
[H]: Help Menu
[Q]: Quit
'''

    # Info
    main_log.info(f"Starting Main log: {title}")

    matrices = []

    run = True

    while run:
        clear_screen()
        print(title)
        print(options)
        user_input = input(">>> ")
        # main_log.debug(f"User Input: {user_input}")
        if user_input.upper() == 'Q':
            main_log.info("Quit Menu")
            print("\nBye Bye!\n")
            run = False
        elif user_input.upper() == 'G':
            main_log.info("Generate Random Menu")
            clear_screen()
            rows = int(input("How many rows?: "))
            cols = int(input("How many columns?: "))
            print("")

            new_matrix_data = []
            for i in range(rows):
                new_temp_row = []
                for j in range(cols):
                    new_entry = random.randint(0, 99)
                    new_temp_row.append(new_entry)
                new_matrix_data.append(new_temp_row)
            # instantiate object
            new_matrix = Matrix(new_matrix_data)
            matrices.append(new_matrix)

            # debug info
            main_log.debug(f"{rows}x{cols}: {new_matrix_data}")

            print(new_matrix)
            input("Press Enter to continue...")

        elif user_input.upper() == 'C':
            main_log.info("Custom Matrix Menu")
            clear_screen()
            rows = int(input("How many rows?: "))
            cols = int(input("How many columns?: "))

            new_matrix_data = []
            for i in range(rows):
                new_row_raw = input(f"Please input row[{i}]: ").split(' ')
                # new_row_txt = new_row_raw.split(' ')
                new_row = []
                for text in new_row_raw:
                    new_row.append(int(text))

                new_matrix_data.append(new_row)
            # instantiate object
            new_matrix = Matrix(new_matrix_data)
            matrices.append(new_matrix)

            # debug info
            main_log.debug(f"{rows}x{cols}: {new_matrix_data}")

            print('\n', new_matrix)
            input("Press Enter to continue...")

        elif user_input.upper() == 'L':
            main_log.info("Check Log Menu")
            clear_screen()

            for counter, matrix in enumerate(matrices):
                print(f"Matrix #{counter+1}:")
                print(matrix)
            input()

        elif user_input.upper() == 'H':
            main_log.info("Help Menu")
            ...
        else:
            print("Invalid Input")
            time.sleep(1.5)

            # Warning
            main_log.warning(f"Invalid Input: {user_input}")

    main_log.info("Bye Bye!")

