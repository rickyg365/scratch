import os

"""
Program: MineSweeper
Author: rickyg3
Date: 08/14/21 
"""
"""
[TBI]:
- add different styles (curved corners thicker bars, maybe even a different default symbol)
- implement game class or just write it out under main
- add continue option to continue last game

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
                # ▇, █
                new_row.append(self.default_symbol)
                # data added, key => ij: value => (visible: bool, char: string)
                # key => {visibility: 1 or 0}ij: char: string >>>  012: " "
                # space char used to represent block in data
                self.data[f"{i}{j}"] = [0, " "]
            self.screen.append(new_row)

    def update_screen(self):
        for i in range(self.y):
            for j in range(self.x):
                key = f"{i}{j}"
                # data added, key => ij: value => (visible: bool, char: string)
                vis, char = self.data[key]
                if vis:
                    if char == " ":
                        self.screen[i][j] = self.default_symbol
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


if __name__ == "__main__":
    # Create display
    my_display = MineDisplay(10, 10)

    # Test Methods
    # my_display.change_symbol(1, 1, "O")
    # my_display.change_visibility(1, 1)
    # my_display.update_screen()
    # my_display.update_space(2, 3, 1, "X")
    # my_display.update_space(2, 2, 0, "X")

    # Show Display (and properties)
    print(my_display)
    # print(my_display.screen)
    # print(my_display.data)
