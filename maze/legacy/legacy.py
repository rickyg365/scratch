import os
import random
from enum import Enum, auto
"""
━
┃

─
│

╭
╮

╯
╰
"""


class Display:
    def __init__(self, rows=5, cols=10):

        self.H_WALL = "─"
        self.V_WALL = "│"

        self.TL_CORNER = "╭"
        self.TR_CORNER = "╮"

        self.BL_CORNER = "╰"
        self.BR_CORNER = "╯"

        self.rows = rows
        self.cols = cols

        self.display_data = self.build_empty_data()
        self.cached_display = self.build_screen()

    def __str__(self):
        """
            Problem with this is that it re renders or remakes the display everytime it prints,
            we can have a cache as a member variable self.cahed_display to print and the build_screen function
            will update the cache when it is called
        """
        return self.cached_display

    def build_screen(self):
        """ Builds screen using data from self.display_data """
        text = f"{self.TL_CORNER}{self.cols * self.H_WALL}{self.TR_CORNER}\n"
        for i in range(self.rows):
            text += f"{self.V_WALL}"
            for j in range(self.cols):
                text += self.display_data[i][j]
            text += f"{self.V_WALL}\n"
        text += f"{self.BL_CORNER}{self.cols * self.H_WALL}{self.BR_CORNER}"

        return text

    def update_screen(self):
        """ Rebuilds the screen w/ current_data to update the cached screen """
        self.cached_display = self.build_screen()

    def build_empty_data(self):
        return [[" " for x in range(self.cols)] for i in range(self.rows)]

    def insert_data(self, input_data):
        """ Saves new data after validation and updates screen """
        # check data size
        input_rows = len(input_data)
        input_cols = len(input_data[0])

        if input_rows == self.rows and input_cols == self.cols:
            self.display_data = input_data
            self.update_screen()
            return
        print("[ Display.insert_data: input data is wrong size ]")
        raise IndexError

    def edit_cell(self, new_value, row_num=0, col_num=0):
        """ Edit a single cell at a given position, DOES NOT UPDATE SCREEN """
        # Check to make sure new_value is valid
        length_check = len(new_value) == 1
        type_check = isinstance(new_value, str)

        if not (length_check and type_check):
            raise TypeError

        # Update Value
        self.display_data[row_num][col_num] = new_value


class CreateMazeData:
    def __init__(self, rows, cols):
        """ Eventually want it to take in a dict with all these values set """

        self.rows = rows
        self.cols = cols

        self.has_start = False
        self.has_end = False

        self.start_region = (self.rows * .5, self.cols * .5)
        self.end_region = (self.rows * .7, self.cols * .7)

        self.start_coord = False
        self.end_coord = False

        self.tokens = {
            "start": "@",
            "end": "X",
            "wall": "█",
            "blank": " ",
            "visited": "."
        }

        # Create New display data
        self.occupied_cells = []
        self.new_display_data = self.create_random_maze()

    def __call__(self):
        return self.new_display_data

    def create_random_maze(self):
        new_display_data = []
        # End of start region
        last_start_row = self.start_region[0] - 1
        last_start_col = self.start_region[1] - 1

        # End of end region
        last_end_row = self.rows - 2
        last_end_col = self.cols - 2

        # Iterate through each cell
        for i in range(self.rows):
            new_row = []
            new_occ_row = []
            for j in range(self.cols):
                # Way #1
                # i_low = i == 0
                # i_max = i == rows-1
                #
                # j_low = j == 0
                # j_max = j == cols-1
                #
                # if i_low or j_low or i_max or j_max:
                #     new_row.append(f"█")

                # Way #2
                # Conditions for certain blocks
                start_condition = False
                end_condition = False

                border_conditions = [
                    i == 0,
                    i == self.rows - 1,
                    j == 0,
                    j == self.cols - 1
                ]
                random_condition = random.randint(1, 100) > 70

                # If there's no start yet
                if not self.has_start:
                    # check if its in the predefined start region
                    in_start_region = i < self.start_region[0] and j < self.start_region[1]
                    start_chance = random.randint(1, 100)

                    # if at the end
                    if i == last_start_row and j == last_start_col:
                        start_chance = 100

                    start_condition = start_chance > 99 and in_start_region

                # If there's no end yet
                if not self.has_end:
                    in_end_region = i > self.end_region[0] and j > self.end_region[1]
                    end_chance = random.randint(1, 100)

                    if i == last_end_row and j == last_end_col:
                        end_chance = 100

                    end_condition = end_chance > 90 and in_end_region

                # What each cell is depending on the conditions met
                if any(border_conditions):
                    new_row.append(f"{self.tokens['wall']}")
                    new_occ_row.append(1)

                elif start_condition:
                    new_row.append(f"{self.tokens['start']}")
                    new_occ_row.append(1)
                    self.start_coord = (i, j)
                    self.has_start = True

                elif end_condition:
                    new_row.append(f"{self.tokens['end']}")
                    new_occ_row.append(1)
                    self.end_coord = (i, j)
                    self.has_end = True

                elif random_condition:
                    new_row.append(f"{self.tokens['wall']}")
                    new_occ_row.append(1)

                else:
                    new_row.append(f"{self.tokens['blank']}")
                    new_occ_row.append(0)
            new_display_data.append(new_row)
            self.occupied_cells.append(new_occ_row)
        return new_display_data

    def export_all_data(self):
        """ Creates dictionary of all data and returns it """
        all_data = {
            "coord": [self.start_coord, self.end_coord],
            "region": [self.start_region, self.end_region],
            "dimensions": [self.rows, self.cols],
            "data": self.new_display_data,
            "occupied_data": self.occupied_cells
        }

        return all_data


def test_default():
    # Sample Data
    sample_display_data = [
        ["1", "2", "3", "4", "5", "6", "7", "8", "9", "X"],
        ["1", "2", "3", "4", "5", "6", "7", "8", "9", "X"],
        ["1", "2", "3", "4", "5", "6", "7", "8", "9", "X"],
        ["1", "2", "3", "4", "5", "6", "7", "8", "9", "X"],
        ["1", "2", "3", "4", "5", "6", "7", "8", "9", "X"]
    ]

    sample_maze_data = [
        ["█", "█", "█", "█", "█", "█", "█", "█", "█", "█"],
        ["█", "S", "█", " ", " ", "█", " ", " ", " ", "█"],
        ["█", " ", " ", " ", "█", " ", " ", "█", " ", "█"],
        ["█", " ", "█", " ", " ", " ", "█", "E", " ", "█"],
        ["█", "█", "█", "█", "█", "█", "█", "█", "█", "█"]
    ]

    incorrect_display_data = [
        ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
        ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
        ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
        ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
        ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    ]

    # Sample Creating new_data
    new_display_data = []

    for i in range(5):
        new_row = []
        for j in range(10):
            new_row.append(f".")
        new_display_data.append(new_row)

    # Create new Display
    new_display = Display()

    print("Initial Display: \n", new_display, sep="")

    # Edit entire Display Data (auto refreshes)
    new_display.insert_data(sample_maze_data)

    # Edit a single cell, NO REFRESH (must manually call)
    # new_display.edit_cell("X", 1, 1)

    new_display.update_screen()
    print("New Display: \n", new_display, sep="")


def test_bigger(rows, cols):
    # Create New display data
    new_display_data = []

    has_start = False
    has_end = False

    start_coord = False
    end_coord = False

    for i in range(rows):
        new_row = []
        for j in range(cols):
            r = random.randint(1, 100)

            # Way #1
            # i_low = i == 0
            # i_max = i == rows-1
            #
            # j_low = j == 0
            # j_max = j == cols-1
            #
            # if i_low or j_low or i_max or j_max:
            #     new_row.append(f"█")

            # Way #2
            border_conditions = [
                i == 0,
                i == rows-1,
                j == 0,
                j == cols-1
            ]
            random_condition = r > 70
            start_condition = False
            end_condition = False

            if not has_start:
                start_var = random.randint(1, 100)
                # upper quadrant
                upper_quadrant = i < (rows * .5) and j < (cols * .5)
                # if at the end
                if i == (rows/2)-1 and j == (cols/2)-1:
                    start_var = 100
                start_condition = start_var > 99 and upper_quadrant

            if not has_end:
                end_var = random.randint(1, 100)
                # Lower Corner
                lower_corner = i > (rows * .7) and j > (cols * .7)

                # if at the end
                if i == (rows - 2) and j == (cols - 2):
                    end_var = 100

                end_condition = end_var > 90 and lower_corner

            if any(border_conditions):
                new_row.append(f"█")
            elif start_condition:
                new_row.append("S")
                start_coord = (i, j)
                has_start = True
            elif random_condition:
                new_row.append(f"█")
            elif end_condition:
                new_row.append("E")
                end_coord = (i, j)
                has_end = True
            else:
                new_row.append(" ")
        new_display_data.append(new_row)

    # Create new Display
    new_display = Display(rows, cols)

    # Insert New Data
    new_display.insert_data(new_display_data)

    print("Final Display: \n", new_display, sep="")
    print("Start Coordinate: ", start_coord)
    print("End Coordinate: ", end_coord)


if __name__ == "__main__":
    # test_default()
    for i in range(1):
        # test_bigger(20, 40)
        r = 20
        c = 40
        new_maze_data = CreateMazeData(r, c)

        display = Display(r, c)
        display.insert_data(new_maze_data())

        print(display)

        my_data = new_maze_data.export_all_data()

        for key, value in my_data.items():
            skip_keys = [
                "data",
                "occupied_data"
            ]
            if key == "occupied_data":
                pure_data = "Occupied Data:\n"
                for x in range(len(new_maze_data.occupied_cells)):
                    for y in range(len(new_maze_data.occupied_cells[0])):
                        pure_data += f"{new_maze_data.occupied_cells[x][y]}"
                    pure_data += "\n"

                print(pure_data)
            if key in skip_keys:
                continue
            print(f"{key.capitalize()}:\n{value}\n")
