import os
import random

# importing display so we can see the data
# from display_handler import Display


def print_matrix(data, title="Title"):
    pure_data = f"{title}:\n"
    for x in range(len(data)):
        for y in range(len(data[0])):
            pure_data += f"{data[x][y]}"
        pure_data += "\n"

    print(pure_data)


class Maze:
    def __init__(self, rows, cols):
        """ Eventually want it to take in a dict with all these values set """

        self.rows = rows
        self.cols = cols

        self.has_start = False
        self.has_end = False

        self.start_region = (self.rows//2, self.cols//2)
        self.end_region = ((self.rows*7)//10, (self.cols * 7)//10)

        self.start_coord = False
        self.end_coord = False

        self.tokens = {
            "start": "S",
            "end": "X",
            "wall": "█",
            "blank": " ",
            "visited": "*"
        }

        # Create New display data
        self.occupied_cells = []
        self.new_display_data = self.create_random_maze()

    def __call__(self):
        return self.new_display_data

    def update_maze_cell(self, location, occupied_val):
        """ (i, j) """
        i, j = location
        occupied_key = {
            0: "blank",
            1: "wall",
            2: "start",
            -1: "end",
            3: "visited"
        }
        self.occupied_cells[i][j] = occupied_val

        token_type = occupied_key[occupied_val]
        self.new_display_data[i][j] = self.tokens[token_type]

    def create_random_maze(self):
        new_display_data = []
        # End of start region
        last_start_row = self.start_region[0] - 1
        last_start_col = self.start_region[1] - 1

        # End of end region
        last_end_row = self.rows - 1
        last_end_col = self.cols - 1

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
                    i < 0,
                    i > self.rows - 1,
                    j < 0,
                    j > self.cols - 1
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
                    new_occ_row.append(2)
                    self.start_coord = (i, j)
                    self.has_start = True

                elif end_condition:
                    new_row.append(f"{self.tokens['end']}")
                    new_occ_row.append(-1)
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


def main():
    """
    Before the export data function we used display to see that it worked

    # Create new Display object, pass in (height, width) and insert maze data
    display = Display(r, c)
    display.insert_data(new_maze_data())

    # Show display
    print(display)
    """
    # Set row height and col width, respectively
    r = 20
    c = 40

    # Create random maze by initializing CreateMazeData object
    new_maze_data = Maze(r, c)

    # Export all data as a dict
    my_data = new_maze_data.export_all_data()

    # Iterate and display data
    for key, value in my_data.items():
        # data attr's to skip
        matrix_keys = [
            "data",
            "occupied_data"
        ]
        # Special case
        if key in matrix_keys:
            print_matrix(value, f"{key} Cells")
            continue
        print(f"{key.capitalize()}:\n{value}\n")


if __name__ == "__main__":
    main()
