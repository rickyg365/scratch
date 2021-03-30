import os
import sys

import time
import math

""" 
Program: 
Author: rickyg3
Date: 03/29/2021
"""


class Display:
    """
    Draw objects using only a reference to starting point, then add a function to chek if exceeds the bounds of
    """
    def __init__(self, display_width, display_height):
        # Declare Screen member variable
        self.screen = []
        self.blank_screen = []

        self.height = display_height
        self.width = display_width

        # Objects
        # create an object class to avoid this uglyness
        # self.objects = [{"point": ['#', (0, 0)]}]

        # Initialize screen matrix using dimensions
        for i in range(self.height):
            new_line = []
            for j in range(self.width):
                new_line.append(' ')
            self.screen.append(new_line)

    def clean(self):
        for i in range(self.height):
            for j in range(self.width):
                self.update_cell(' ', (i, j))

    def update_cell(self, new_char, new_position):
        x, y = new_position
        self.screen[x][y] = new_char

    # def add_object(self, object_name, object_data, starting_position):
    #     # Starting coordinates
    #     x, y = starting_position
    #
    #     for r in range(len(object_data)):
    #         for c in range(len(object_name[0])):
    #             self.update_cell('#')

    def show(self):
        screen_out = ""

        for row in self.screen:
            line = "".join(row)
            # print(line)
            screen_out += line + "\n"

        print(screen_out)

    # def update_object(self, object_name, new_position):


if __name__ == "__main__":
    main_screen = Display(40, 20)

    run = True

    while run:
        # # os.system("cls")
        # main_screen.show()
        # 
        # position = input("Choose location (row, col): ")
        # # parse data
        # try:
        #     raw = position.split(",")
        #     row = int(raw[0].strip())
        #     col = int(raw[1].strip())
        # 
        # except ValueError:
        #     # run = False
        #     print("Invalid Input!")
        #     continue
        # main_screen.clean()
        # main_screen.update_cell("#", (row, col))
        # 
        # # main_screen.show()

        # Velocity
        x = 0
        y = 19

        v_x = 2
        v_y = 4

        t = 12

        for i in range(t):
            if y < 0:
                y = 0
            elif y > 19:
                y = 19
            os.system("cls")
            main_screen.clean()
            print(x, y)
            main_screen.update_cell('#', (y, x))
            main_screen.show()
            # input("")
            time.sleep(0.30)

            x = x + v_x
            if i < t/2:
                y = y - v_y
            else:
                y = y + v_y
