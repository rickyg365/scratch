import os

"""
Program:
Author:
Date:
"""
"""

─	━	│	┃	┄	┅	┆	┇	┈	┉	┊	┋	┌	┍	┎	┏
┐	┑	┒	┓	└	┕	┖	┗	┘	┙	┚	┛	├	┝	┞	┟
┠	┡	┢	┣	┤	┥	┦	┧	┨	┩	┪	┫	┬	┭	┮	┯
┰	┱	┲	┳	┴	┵	┶	┷	┸	┹	┺	┻	┼	┽	┾	┿
╀	╁	╂	╃	╄	╅	╆	╇	╈	╉	╊	╋	╌	╍	╎	╏
═	║	╒	╓	╔	╕	╖	╗	╘	╙	╚	╛	╜	╝	╞	╟
╠	╡	╢	╣	╤	╥	╦	╧	╨	╩	╪	╫	╬	╭	╮	╯
╰

   0 1 2 3 4
  ┏━━━━━━━━━┓
0 ┃         ┃   
1 ┃         ┃
2 ┃        █┃
3 ┗━━━━━━━━━┛


# [ top_left, top_right, bot_left, bot_right ]
corners = {
    "round": [ "╭", "╮", "╰", "╯" ],
    "single": [ "┌", "┐", "└", "┘" ],
    "bold": [ "┏", "┓", "┗", "┛" ],
    "double": [ "╔", "╗", "╚", "╝" ]
}

# [ horizontal, vertical ]
walls = {
    "single": [ "┈", "│" ],
    "bold": [ "━", "┃" ],
    "double": [ "═", "║" ]
}

"""

# Variables


# Functions
def func():
    return


# Classes
class Screen:
    def __init__(self, content_width, content_height, data=None, style=None):
        # Size
        self.columns = content_width
        self.rows = content_height

        if data is None:
            data = [[" " for _ in range(content_width)] for j in range(content_height)]

        self.data = data

        if style is None:
            style = "single"

        self.style = style

        # [ top_left, top_right, bot_left, bot_right ]
        self.corners = {
            "round": ["╭", "╮", "╰", "╯"],
            "single": ["┌", "┐", "└", "┘"],
            "bold": ["┏", "┓", "┗", "┛"],
            "double": ["╔", "╗", "╚", "╝"]
        }

        # [ horizontal, vertical ]
        self.walls = {
            "single": ["─", "│"],
            "round": ["─", "│"],
            "bold": ["━", "┃"],
            "double": ["═", "║"]
        }

        self.h_wall = self.walls[style][0]
        self.v_wall = self.walls[style][1]

        self.tl_corner = self.corners[style][0]
        self.tr_corner = self.corners[style][1]
        self.bl_corner = self.corners[style][2]
        self.br_corner = self.corners[style][3]

        self.content = self.build_screen(data)

    def __str__(self):
        # print(f"Style: {self.style}")
        return self.content

    def blank_screen(self):
        """
        less expensive than using blank data and build screen
        """
        text = f"\n{self.tl_corner}{self.h_wall * self.columns}{self.tr_corner}\n"

        for i in range(self.rows):
            text += f"{self.v_wall}{' ' * self.columns}{self.v_wall}\n"

        text += f"{self.bl_corner}{self.h_wall * self.columns}{self.br_corner}"

        # can return or print the screen
        return text

    def build_screen(self, input_data):
        cache_text = f"{self.tl_corner}{self.h_wall*self.columns}{self.tr_corner}\n"
        for row in input_data:
            cache_text += f"{self.v_wall}"
            for column_item in row:
                # can add length verification here
                cache_text += column_item
            cache_text += f"{self.v_wall}\n"

        cache_text += f"{self.bl_corner}{self.h_wall*self.columns}{self.br_corner}"

        return cache_text

    def update_screen(self, new_data):
        self.data = new_data
        self.content = self.build_screen(new_data)

    def display_text(self, display_string, x=0, y=0):
        # x, y is coord x is column y is row
        max_condition = len(display_string) + x > self.columns

        if max_condition:
            display_string = "error!"

        for i, char in enumerate(display_string):
            # print(i, char)
            # input()
            self.data[y][x+i] = char
        self.content = self.build_screen(self.data)

    def add_text(self, text, screen_data, x=0, y=0, style=None):
        ...

    def add_box(self, length, width, x=0, y=0, text=""):
        # smallest is 3x3
        full_box = []  # [[" "for _ in range(width)] for j in range(length)]
        box_data = [[" "for _ in range(width-2)] for j in range(length-2)]

        # add text to box data
        center = (len(box_data)//2) - 1
        max_length = len(box_data[center])

        has_text = text != ""

        # check if theres enough space for string
        if len(text) > max_length:
            has_text = False

        if has_text:
            for _, char in enumerate(text):
                box_data[center][_] = char

        # Build base box
        for i in range(length):
            last = i == length-1
            zero = i == 0

            new_row = []

            for j in range(width):
                last_j = j == width-1
                zero_j = j == 0

                if last or zero:
                    if zero_j:
                        current_char = f"{self.tl_corner}" if zero else f"{self.bl_corner}"
                        new_row = [f"{current_char}"]
                        continue
                    elif last_j:
                        current_char = f"{self.tr_corner}" if zero else f"{self.br_corner}"
                        new_row.append(f"{current_char}")
                        continue

                    new_row.append(f"{self.h_wall}")
                    continue

                if zero_j or last_j:
                    new_row.append(self.v_wall)
                    continue

                new_row.append(box_data[i-2][j-2])

            full_box.append(new_row)


        # first_row = [f"{self.tl_corner}"]
        # for i in range(width-2):
        #     first_row.append(f"{self.h_wall}")
        # first_row.append(f"{self.tr_corner}")
        #
        # full_box.append(first_row)
        #
        # for i in range(length-2):
        #     new_row = [f"{self.v_wall}"]
        #     for j in range(width-2):
        #         # self.data[i + 1][j + 1]
        #         new_row.append(box_data[i][j])
        #     new_row.append(f"{self.v_wall}")
        #     full_box.append(new_row)
        #
        # last_row = [f"{self.bl_corner}"]
        # for i in range(width-2):
        #     last_row.append(f"{self.h_wall}")
        # last_row.append(f"{self.br_corner}")
        # full_box.append(last_row)

        for i in range(length):
            for j in range(width):
                self.data[y+i][x+j] = full_box[i][j]

        self.content = self.build_screen(self.data)

    def reset_display(self):
        self.data = [[" " for _ in range(self.columns)] for j in range(self.rows)]
        self.content = self.blank_screen()


if __name__ == "__main__":
    terminal_width, terminal_height = os.get_terminal_size()
    # height should be terminal height - 2 for border - whatever other space we need for status bars or input
    my_screen = Screen(terminal_width-2, terminal_height-4, style="round")
    screen_data = my_screen.data

    running = True
    while running:
        os.system("cls")
        print(my_screen)
        user_input = input(">>> ")

        if user_input == 'q':
            print("\n[ Quit Program ]\n")
            running = False
        elif user_input == "start":
            # run something
            my_screen.reset_display()
            l, w, x, y = input("Length(outer), Width(outer), x, y: ").split(", ")
            my_screen.add_box(int(l), int(w), int(x), int(y), text="sample")
            continue
        else:
            my_screen.reset_display()
            my_screen.display_text(user_input)
