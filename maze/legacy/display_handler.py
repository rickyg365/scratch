import os


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


if __name__ == "__main__":
    pass
