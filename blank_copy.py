import os
import sys

import time

""" 
Program: 
Author: rickyg3
Date: 
"""

""" 
# DISPLAY
_____________________
.  .
.  .

* *
* *

[][]
[][]
_____________________
data = [
    [][],
    [][]
    ]


__add__:
    self.data1 = [] []
    self.data2 = [] []
    
    self.data1[0] + self.data2[0]
    self.data1[1] + self.data2[1] 

"""


class Chunk:
    def __init__(self, x=2, y=2):
        self.x = x
        self.y = y
        # The object is a string for now but what if we make it a custom object?
        self.data = []
        for i in range(self.x):
            row_data = []
            for j in range(self.y):
                row_data.append("*")
            self.data.append(row_data)
        # print(self.data)

    def __str__(self):
        txt = ''
        for i in range(self.x):
            for j in range(self.y):
                txt += f"{self.data[i][j]}"
            txt += '\n'
        return txt

    def __add__(self, other):
        x_match = False
        y_match = False

        if self.x == other.x:
            x_match = True
        if self.y == other.y:
            y_match = True

        if x_match and y_match:
            new_data = []
            for r in range(self.x):
                new_row = []
                for data in self.data[r]:
                    new_row.append(data)
                for data in other.data[r]:
                    new_row.append(data)
                new_data.append(new_row)
            return Collection(new_data)

        else:
            print(f"sizeMatchError: {self.x}!={other.x} or {self.y}!={other.y}")

    def update_spot(self, new_value, x, y):
        self.data[x][y] = new_value


# Make this class not inherit and just use the template to update a chunk
class StatusBar(Chunk):
    """
    Design, x = 3, y = 16
    .--------------.
    | [##########] |
    '--------------'


    def Maxright
        the rightmost coordinate with which we could still see the whole status bar
        the magic number is the chunk column number minus the status bar y number
        plus or minus one lol


    """
    # Add in a chunk variable that we can use to paste this on top of it must be the minimum dimensions
    def __init__(self, base_chunk=None, loc_x=0, loc_y=0):
        # Location variables
        self.location_x = loc_x
        self.location_y = loc_y

        # Size internal variable
        self.x = 3
        self.y = 16
        # If given a chunk
        if base_chunk is None:
            super().__init__(self.x, self.y)
            self.base = base_chunk
        else:
            self.base = base_chunk

        self.health_amount = 100
        self.template = []
        self.update_template(self.health_amount)

        # Update values using template
        if self.base is None:
            self.set_bar()
        else:
            self.set_bar(self.location_x, self.location_y)

    def set_bar(self, start_row=0, start_col=0):
        if self.base is None:
            for i in range(self.x):
                for j in range(self.y):
                    current_char = f"{self.template[i][j]}"
                    self.data[start_row + i][start_col + j] = current_char
        else:
            for i in range(self.x):
                for j in range(self.y):
                    current_char = f"{self.template[i][j]}"
                    r = start_row + i
                    c = start_col + j
                    self.base.update_spot(current_char, r, c)  # [start_row + i][start_col + j] = current_char
            
    def update_template(self, health_amount):
        # Construct
        spacing1 = 0
        spacing2 = 0
        diff = self.y - 16
        if diff <= 0:
            pass
        elif (self.y - 16) % 2 == 0:
            spacing1 = diff // 2
            spacing2 = diff // 2
        else:
            spacing1 = diff // 2
            spacing2 = diff // 2 + 1

        # Health Bar
        active = (health_amount // 10)
        health_bar = (active * '#' + active % 10 * ' ')

        self.template = [
            list(f".{(self.y - 2) * '-'}."),
            list(f"|{spacing1 * ' '} [{health_bar}] {spacing2 * ' '}|"),
            list(f"'{(self.y - 2) * '-'}'")
        ]

    def update_health(self, new_amount: int):
        self.health_amount = new_amount
        self.update_template(new_amount)
        self.set_bar(self.location_x, self.location_y)


class Collection:
    def __init__(self, data):
        self.data = data
        self.x = len(self.data)
        self.y = len(self.data[0])

    def __str__(self):
        txt = ''
        for row in range(self.x):
            for col in range(self.y):
                txt += f"{self.data[row][col]}"
            txt += '\n'
        return txt

    def __add__(self, chunk):
        x_match = False

        if self.x == chunk.x:
            x_match = True

        if x_match:
            new_data = []
            for r in range(self.x):
                new_row = []
                for data in self.data[r]:
                    new_row.append(data)
                for data in chunk.data[r]:
                    new_row.append(data)
                new_data.append(new_row)
            return Collection(new_data)

        else:
            print(f"sizeMatchError: {self.x}!={chunk.x}")


if __name__ == "__main__":
    # # CHUNKS
    # chunk1 = Chunk(1, 1)
    # chunk2 = Chunk(1, 1)
    #
    # print("Chunks")
    # print(chunk1)
    # print(chunk2)
    #
    # # COLLECTIONS
    # raw_data = [
    #     ["*", "*", "*", "*"],
    #     ["*", "*", "*", "*"],
    #     ["*", "*", "*", "*"]
    # ]
    #
    # collection1 = Collection(raw_data)
    # collection2 = chunk1 + chunk2
    #
    # print("Collections")
    # print(collection1)
    # print(collection2)
    #
    # # Array of chunks into a collection
    # list_chunks = []
    # collection = None
    # for n in range(10):
    #     new_chunk = Chunk(3, 3)
    #     list_chunks.append(new_chunk)
    #     if n == 1:
    #         collection = list_chunks[0] + new_chunk
    #     elif n == 0:
    #         pass
    #     else:
    #         collection += new_chunk
    #
    # print(collection)

    # Make an array of chunks into a display?
    display = Chunk(25, 50)
    print(display)

    # hbar = StatusBar()
    # print(hbar)
    # 
    # hbar.update_health(50)
    # print(hbar)

    hbar = StatusBar(display, 10, 10)
    print(display)

    hbar.update_health(50)
    print(display)
