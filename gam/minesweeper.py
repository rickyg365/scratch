import os

import time
import random

"""
Program: MineSweeper
Author: rickyg3
Date: 08/14/21 
"""

""" 
[Design Scratch board]

─	━	│	┃	┄	┅	┆	┇	┈	┉	┊	┋	┌	┍	┎	┏
┐	┑	┒	┓	└	┕	┖	┗	┘	┙	┚	┛	├	┝	┞	┟
┠	┡	┢	┣	┤	┥	┦	┧	┨	┩	┪	┫	┬	┭	┮	┯
┰	┱	┲	┳	┴	┵	┶	┷	┸	┹	┺	┻	┼	┽	┾	┿
╀	╁	╂	╃	╄	╅	╆	╇	╈	╉	╊	╋	╌	╍	╎	╏
═	║	╒	╓	╔	╕	╖	╗	╘	╙	╚	╛	╜	╝	╞	╟
╠	╡	╢	╣	╤	╥	╦	╧	╨	╩	╪	╫	╬	╭	╮	╯
╰
   0 1 2 3 4
  ┏━┳━┳━┳━┳━┓
0 ┃X┃ ┃ ┃ ┃ ┃   
1 ┃ ┃ ┃X┃ ┃ ┃
2 ┃ ┃ ┃ ┃ ┃X┃
3 ┗━┻━┻━┻━┻━┛

   0 1 2 3 4
  ┏━━━━━━━━━┓
0 ┃█┃█┃ ┃ ┃█┃   
1 ┃█┃█┃X┃█┃█┃
2 ┃█┃█┃█┃█┃█┃
3 ┗━━━━━━━━━┛


┌─┬─┬─┬─┬─┐
│█│█│█│█│█│
│█│█│X│█│█│ 
│█│█│█│█│█│
└─┴─┴─┴─┴─┘


┌─┬─┬─┬─┬─┐
│ │ │X│ │ │
│ │ │X│ │ │    # ├─┼─┼─┼─┼─┤
│ │ │ │ │X│
└─┴─┴─┴─┴─┘

╭─┬─┬─┬─┬─╮
│ │ │X│ │ │
│ │ │X│ │ │    # ├─┼─┼─┼─┼─┤
│ │ │ │ │X│
╰─┴─┴─┴─┴─╯

╒═╤═╤═╤═╤═╕
│ │ │ │ │X│    # ╞═╪═╪═╪═╪═╡
│ │ │X│ │ │    # ╞═╪═╪═╪═╪═╡
│ │ │ │ │x│
╘═╧═╧═╧═╧═╛
"""


def clear_screen():
    # if os is linux use clear, or mac?
    os.system("cls")


class MineDisplay:
    def __init__(self, num_rows=10, num_cols=10):
        self.y = num_rows
        self.x = num_cols

        self.default_symbol = "▇"

        # doing [[0]*num_cols]*num_rows doesnt work each array is connected and gets updated
        self.screen = []
        self.data = {}

        self.build_screen()

    def __str__(self):
        text = f"\n   {' '.join(str(x) for x in range(self.x))}\n  ┌{'─┬'*(self.x - 1)}─┐\n"
        for y, row in enumerate(self.screen):
            text += f"{y} "
            for x, col_val in enumerate(row):
                text += f"│{col_val}"
            text += "│\n"
        text += f"  └{'─┴'*(self.x - 1)}─┘\n"
        return text

    def build_screen(self):
        for i in range(self.y):
            new_row = []
            for j in range(self.x):
                new_row.append(self.default_symbol)
                # data added, key => ij: value => (visible: bool, char: string)
                # key => {visibility: 1 or 0}ij: char: string >>>  012: " "
                # space char used to represent block in data
                self.data[f"{i}{j}"] = [0, " "]
            self.screen.append(new_row)

    def reset_screen(self):
        self.screen = []
        self.data = {}

        self.build_screen()

    def update_screen(self):
        for i in range(self.y):
            for j in range(self.x):
                key = f"{i}{j}"
                # data added, key => ij: value => (visible: bool, char: string)
                vis, char = self.data[key]

                if vis:
                    if char == " ":
                        self.screen[i][j] = char
                        continue
                    self.screen[i][j] = char

    def change_symbol(self, row_num, col_num, new_symbol=" "):
        update_key = f"{row_num}{col_num}"
        # change data
        self.data[update_key][1] = new_symbol

    def change_visibility(self, row_num, col_num, visibility=None):
        update_key = f"{row_num}{col_num}"

        if visibility is None:
            current_vis = self.data[update_key][0]
            # 0 if vis is 1 and 1 if vis is 0, swap basically
            visibility = 0 if current_vis else 1

        # change data
        self.data[update_key][0] = visibility

    def update_space(self, row_num, col_num, visibility=0, new_symbol=" "):
        """ updates screen """
        # if only indices provided restores to default values
        update_key = f"{row_num}{col_num}"
        # change data
        self.data[update_key] = [visibility, new_symbol]
        # update visibility?
        if visibility == 1:
            if new_symbol == " ":
                self.screen[row_num][col_num] = self.default_symbol
                return

            self.screen[row_num][col_num] = self.data[update_key][1]


class MineSweeper:
    def __init__(self):
        self.display = MineDisplay(10, 10)
        self.player = ""
        self.difficulty = {
            "easy": 3,
            "medium": 5,
            "hard": 7
        }
        self.user_input_guesses = []

    def show_screen(self):
        clear_screen()
        self.display.update_screen()
        print(self.display)

    def get_input(self):
        try:
            row, col = input(f"\n[row col] >>> ").strip().split(" ")

            user_guess = f"{row}{col}"
            if user_guess in self.user_input_guesses:
                print(f"\nAlready guessed buddy, try again.")
                time.sleep(1.2)
                return False

            self.user_input_guesses = user_guess
            return row, col

        except ValueError:
            print(f"\nNeed two numbers buddy, try again.")
            time.sleep(1.2)
            return False
            # input("")

    def populate_enemies(self, difficulty='medium'):
        num_enemies = self.difficulty[difficulty]

        already_placed = []
        while num_enemies > 0:
            r_y = random.randint(0, self.display.y - 1)
            r_x = random.randint(0, self.display.x - 1)

            pair = f"{r_y}{r_x}"

            if pair in already_placed:
                continue

            already_placed.append(pair)
            num_enemies -= 1

            self.display.update_space(r_y, r_x, 0, "X")

    def play_round(self):
        # add [5] random enemies
        self.populate_enemies()
        try:
            # Game Loop
            while True:
                # Prepare screen and display
                self.show_screen()

                # Get user input
                guess = self.get_input()

                if not guess:

                    continue
                rownum, colnum = guess
                # make square visible based on user input
                self.display.change_visibility(rownum, colnum)

                # screen updates at beginning of loop so we don't need to call the update screen method
                # unless its game over
                # Check if user input lands on a bomb
                gameover_check = self.display.data[f"{rownum}{colnum}"][1] == "X"

                # if game is over
                if gameover_check:
                    self.show_screen()
                    print("Fuck you've done it now.\n")
                    break

        except KeyboardInterrupt:
            print("\n \n[ Bye Bye ]\n")


if __name__ == "__main__":
    # Create display
    # my_display = MineDisplay(10, 10)

    # Test Methods
    # my_display.change_symbol(1, 1, "O")
    # my_display.change_visibility(1, 1)
    # my_display.update_screen()
    # my_display.update_space(2, 3, 1, "X")
    # my_display.update_space(2, 2, 0, "X")

    # Show Display (and properties)
    # print(my_display)
    # print(my_display.screen)
    # print(my_display.data)

    my_game = MineSweeper()

    my_game.play_round()

"""
Legacy Code:

one round:
 One round
    dimension x => number of columns, dimension y => number of rows
    dimension_x, dimension_y = 10, 10
    my_display = MineDisplay(dimension_y, dimension_x)

    # add [5] random enemies
    num_enemies = 5
    already_placed = []
    while num_enemies > 0:
        r_y = random.randint(0, dimension_y-1)
        r_x = random.randint(0, dimension_x-1)

        pair = f"{r_y}{r_x}"

        if pair in already_placed:
            continue

        already_placed.append(pair)
        num_enemies -= 1

        my_display.update_space(r_y, r_x, 0, "X")

    # Wrap in try loop for keyboard exception, nice quiting
    try:
        # Game Loop
        while True:
            # Prepare screen and display
            clear_screen()
            my_display.update_screen()
            print(my_display)

            # Get user input
            try:
                rownum, colnum = input(f"\n[row col] >>> ").strip().split(" ")
                # need to keep track of which spaces have been guessed and the raise an error
                # or a warning if the user chooses them again
            except ValueError:
                print(f"\nNeed two numbers buddy, try again.")
                time.sleep(1.2)
                # input("")
                continue

            # make square visible based on user input
            my_display.change_visibility(rownum, colnum)

            # screen updates at beginning of loop so we don't need to call the update screen method unless its game over

            # check if user input lands on a bomb
            gameover_check = my_display.data[f"{rownum}{colnum}"][1] == "X"

            # if game is over
            if gameover_check:
                clear_screen()
                my_display.update_screen()
                print(my_display)
                print("Fuck you've done it now.\n")
                break

            # DEBUG
            # print(my_display)
            # print(my_display.screen)
            # print(my_display.data)

    except KeyboardInterrupt:
        print("\n \n[ Bye Bye ]\n")
"""
