import os
import random
import time
import keyboard


"""
Display Prototype:
.-------------------------.
|                         |
|                         |
|                         |
|                         |
|                         | 
|                         |
|                         |
|                         |
'-------------------------'

To Do List:
    - make a line at a certain x,y coord of certain length, in certain direction
    - make a 2d shape
    - make a collision detecting function

"""


class Display:
    """
    Creates a 2d array that acts as a display,

        Properties:
            - content_length: width, how many characters per row
            - content_rows: height, number of rows present
            - raw_content: 2d array of dynamic values

        Methods:
            - update_tile: change an indv. tile at given x, y location
            - build_empty_content: change all the content of each cell into empty space
            - build_x_content: change all the content of each cell into the chosen character
            - build_display: Converts raw content array into string format and adds border
            - __str__: calls build display and returns the string!
    """
    def __init__(self, content_length=25, content_rows=8, content_array=None):
        self.content_length = content_length
        self.content_rows = content_rows

        if content_array is None:
            content_array = self.build_empty_content()

        self.raw_content = content_array

        self.status = "|Status|: [+++++++++++++++]"

    def __str__(self):
        text = self.build_display()
        return text

    def update_tile(self, row_num, col_num, new_tile="#"):
        self.raw_content[row_num][col_num] = new_tile

    def make_line(self, x, y, length, new_tile="#", direction='x'):
        if direction == 'x':
            for _ in range(length):
                self.update_tile(x, y + _, new_tile)
        else:
            for _ in range(length):
                self.update_tile(x + _, y, new_tile)

    def save_default(self):
        default_copy = []
        for row in self.raw_content:
            row_copy = []
            for item in row:
                row_copy.append(item)
            default_copy.append(row_copy)

        return default_copy

    def build_empty_content(self):
        content_array = []
        for i in range(self.content_rows):
            content_row = []
            for j in range(self.content_length):
                content_row.append(" ")
            content_array.append(content_row)

        return content_array

    def build_x_content(self, input_char=' '):
        content_array = []
        for i in range(self.content_rows):
            content_row = []
            for j in range(self.content_length):
                content_row.append(input_char)
            content_array.append(content_row)

        return content_array

    def build_status(self, spacer_tile=' '):
        # THis func should be in a player class and return it to the display object so it can update
        first_half = " [Status]"

        hp = 25
        atk = 12
        res = 8
        spd = 15

        second_half = f" HP:{hp:02}"
        second_half += f" ATK:{atk:02}"
        second_half += f" DEF:{res:02}"
        # second_half += f" SPD: {spd:02}"

        max_length = self.content_length + 2

        # +2 for the border
        diff = max_length - len(first_half + second_half)

        spacer = (diff-1)*spacer_tile

        if diff < 0:
            big_space = (max_length - len(second_half))*spacer_tile
            return second_half + big_space

        return first_half + spacer + second_half + ' '

    def build_display(self):
        """ Builds the display just using an array of the content """
        output_display = ""

        top_border = '.' + self.content_length*'-' + '.'
        output_display += top_border

        side_border_char = '|'
        for row in range(self.content_rows):
            output_display += '\n'
            output_display += side_border_char
            output_display += "".join(self.raw_content[row])
            output_display += side_border_char

        bot_border = "\n'" + self.content_length*"-" + "'"
        output_display += bot_border
        output_display += '\n' + self.build_status()

        return output_display

    # def refresh(self, delay_rate=1):
    #     run = True
    #     while run:
    #         try:
    #             os.system("cls")
    #             print(self)
    #             time.sleep(delay_rate)
    #
    #         except KeyboardInterrupt:
    #             print("ERROR: \n")
    #             run = False


def run_display(display_object=Display(), delay_rate=.35):
    run = True

    x, y = 0, 0
    # RATIO 8/25
    x_vel = 1
    y_vel = display_object.content_length//display_object.content_rows
    # round(display_object.content_length/(display_object.content_rows-1))   # (25/8) ~= 3

    hero = "@"
    reset = " "

    display_object.update_tile(x, y, hero)

    while run:
        try:
            os.system("cls")

            # print current screen
            print(display_object)

            # set old x & y to the current x and y before we add the respective velocity values
            old_x, old_y = x, y
            # set max x & y base on number of rows and characters per row
            max_x = display_object.content_rows - 1
            max_y = display_object.content_length - 1

            # Check for keys
            # print(keyboard.read_key())
            # Need an extra keyboard.read_key() here
            # I think because we get an up and a downstroke read of each key when we press, ont sure look into it
            keyboard.read_key()

            update_x = x + x_vel
            update_y = y + y_vel

            update_nx = x - x_vel
            update_ny = y - y_vel

            current_key = keyboard.read_key()
            if current_key == 'w' or current_key == 'up':
                if update_nx <= 0:
                    x = 0
                else:
                    x = update_nx
            elif current_key == 'a':
                if update_ny <= 0:
                    y = 0
                else:
                    y = update_ny
            elif current_key == 's' or current_key == 'down':
                if update_x >= max_x:
                    x = max_x
                else:
                    x = update_x
            elif current_key == 'd':
                if update_y >= max_y:
                    y = max_y
                else:
                    y = update_y

            elif current_key == 'left':
                if y - 1 <= 0:
                    y = 0
                else:
                    y -= 1

            elif current_key == 'right':
                if y + 1 >= max_y:
                    y = max_y
                else:
                    y += 1

            else:
                print(f"\n{current_key} not recognized...")
                time.sleep(.75)

            # Reset old hero position
            display_object.update_tile(old_x, old_y, reset)
            # Add hero to his new position
            display_object.update_tile(x, y, hero)

            # time.sleep(delay_rate)

        except KeyboardInterrupt:
            print("\n[DISPLAY STOPPED]\n")
            run = False


def insert_text(display, text, x, y):
    return


def status_box(display, text_input, length=14):
    """

    .------------.
    | stat   box |
    '------------'
    0123456789abcd

    x, y = 1, 1
    max_length = 13

    # .: (x, y), (x+13, y)
    # -: (x+1, y), (x+12, y),
    #    (x+1, y+2), (x+12, y+2)
    # |: (x, y+1), (x+13, y+1)
    # ': (x, y+2), (x+13, y+2)

    stat_box = {

        '.': [
            (x, y),
            (x+max_length, y)
        ]
        '-': [
            (x+1, y),
            (x+(max_length-1), y),
            (x+1, y+2),
            (x+(max_length-1), y+2)
        ],
        '|': [
            (x, y+1),
            (x+max_length, y+1)
        ],
        "'": [
            (x, y+2),
            (x+max_length, y+2)
        ]

    }
    """
    x, y = 1, 1

    max_char = length-4
    max_index = length-1
    if len(text_input) > max_char:
        text_input = text_input[:max_char]
    elif len(text_input) < max_char:
        text_input += (max_char-len(text_input))*" "

    stat_box = {
        '.': [
            (x, y),
            (x + max_index, y)
        ],
        # '-': [
        #     (x + 1, y),
        #     (x + (max_length - 1), y),
        #     (x + 1, y + 2),
        #     (x + (max_length - 1), y + 2)
        # ],
        '|': [
            (x, y + 1),
            (x + max_index, y + 1)
        ],
        "'": [
            (x, y + 2),
            (x + max_index, y + 2)
        ]
    }

    display.make_line(y, x+1, max_index-1, '-')
    display.make_line(y+2, x+1, max_index-1, '-')

    for cha, tups in stat_box.items():
        for tu in tups:
            r, c = tu
            display.update_tile(c, r, cha)

    for index, letter in enumerate(text_input):
        display.update_tile(y+1, x+2+index, letter)


if __name__ == "__main__":
    content = [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    ]

    my_display = Display(32, 16)

    txt = "HelloWorld"
    status_box(my_display, txt)
    # my_display.make_line(8, 16, 5)
    # my_display.make_line(8, 15, 6, direction='y')
    # my_display.make_line(13, 16, 5)
    # my_display.make_line(8, 21, 6, direction='y')

    items = {
        # '#': [
        #     (0, 1),
        #     (1, 0)
        # ],
        '+': [
            (20, 0),
            (20, 1),
            (21, 0),
            (21, 1)
        ]
    }

    for tile, tuples in items.items():
        for tup in tuples:
            row, col = tup
            my_display.update_tile(col, row, tile)


    # my_display.make_line(1, 1, 4)

    # for d in range(16):
    #     if d % 2 != 0:
    #         my_display.make_line(d, 0, 32)

    # my_display.raw_content = my_display.build_x_content('_')
    # print(my_display)

    run_display(my_display)

    # my_display.refresh()


"""
AUTO MOVE:
    # set old x & y to the current x and y before we add the respective velocity values
            old_x, old_y = x, y
            # set max x & y base on number of rows and characters per row
            max_x = display_object.content_rows - 1
            max_y = display_object.content_length - 1

            # Add the respective velocities to x and y
            update_x = x + x_vel
            update_y = y + y_vel
            # Check that velocity doesnt make x value surpass the max if it does set it to the max value
            if update_x >= max_x:
                x = max_x
            else:
                x = update_x

            # if updated y surpasses y_max, set y to y_max
            if update_y >= max_y:
                y = max_y
            else:
                y = update_y

            # print(x, y, old_x, old_y)

            # Reset old hero position
            display_object.update_tile(old_x, old_y, reset)
            # Add hero to his new position
            display_object.update_tile(x, y, hero)
"""


