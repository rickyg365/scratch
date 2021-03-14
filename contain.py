import os

"""
To Do:
    add addition operator to container class so I can lay things out better under the screen class
"""

''' Stable base 03/12/2021 '''
# class Container:
#     def __init__(self, x=1, y=1):
#         self.data = []
#         self.width = x
#         self.height = y
#
#         self.total_width = self.width + 2
#         self.total_height = self.height + 2
#
#         # Create empty matrix
#         for row in range(self.height):
#             line = []
#             for col in range(self.width):
#                 line.append(" ")
#             self.data.append(line)
#
#     def __str__(self):
#         # Top Line
#         display = f".{self.width * '-'}.\n"
#         # Display plus left border
#         for i in range(self.height):
#             line = "|"
#             for j in range(self.width):
#                 line += self.data[i][j]
#             # Right border
#             display += line + '|\n'
#         # Bottom Line
#         display += f"'{self.width * '-'}'\n"
#
#         return display
#
#     def __add__(self, other):
#         # Check if the heights are the same
#         # TBI # TBI # TBI # TBI # TBI # TBI # TBI # TBI #
#         new = []
#         # Assuming same height
#         line = ""
#         for row in range(self.height):
#             s = ""
#             for val in self.data[row]:
#                 s += val
#
#             o = ""
#             for ele in other.data[row]:
#                 o += ele
#
#             line += s + o + "\n"
#             new.append(line)
#
#         n = Container((self.width + other.width), self.height)
#
#         n.data = new
#
#         return n
#
#     def update(self, row_num, col_num, new_value):
#         if len(new_value) == 1:
#             self.data[row_num][col_num] = new_value
#         else:
#             self.data[row_num][col_num:(len(new_value) + col_num)] = new_value
#
#     def set_size(self, x, y):
#         self.width = x
#         self.height = y
#
#         self.data = []
#         # Create empty matrix
#         for row in range(self.height):
#             line = []
#             for col in range(self.width):
#                 line.append(" ")
#             self.data.append(line)


# Make a General Container class with all the same properties except the string methods doesnt add any extra stuff
# Make this one into a text box class


def clear_screen():
    os.system("cls")


class Container:
    def __init__(self, x=1, y=1):
        self.data = []
        self.width = x
        self.height = y

        # Create empty matrix
        for row in range(self.height):
            line = []
            for col in range(self.width):
                line.append(" ")
            self.data.append(line)

    def __str__(self):
        # Top Line
        display = ""
        # Display
        for i in range(self.height):
            line = ""
            for j in range(self.width):
                line += self.data[i][j]
            # Right border
            display += line + '\n'
        # Bottom Line
        display += f""

        return display

    def __add__(self, other):
        # Check if the heights are the same
        if self.height != other.height:
            print(f"Height do not match: {self.height} {other.height}")
            return False
        # elif type(other) != type(self):

        # Assuming same height
        line = []
        for row in range(self.height):
            s = []
            for val in self.data[row]:
                s.append(val)

            o = []
            for ele in other.data[row]:
                o.append(ele)

            line.append(s + o)

        n = Container((self.width + other.width), self.height)
        n.data = line

        return n

    def update(self, row_num, col_num, new_value):
        if len(new_value) == 1:
            self.data[row_num][col_num] = new_value
        else:
            self.data[row_num][col_num:(len(new_value) + col_num)] = new_value

    def set_size(self, x, y):
        self.width = x
        self.height = y

        self.data = []
        # Create empty matrix
        for row in range(self.height):
            line = []
            for col in range(self.width):
                line.append(" ")
            self.data.append(line)


# Generalize this into a Textbox container and then make this a specific fight menu or fight box container
class Textbox(Container):
    def __init__(self, x=15, y=2):
        super().__init__(x+2, y+2)

        # Size
        # self.width = 17
        # self.height = 4

        self.text_width = x
        self.text_height = y

        # self.style = style

        # Update Matrix

        # Top
        self.update(0, 0, f".{self.text_width * '-'}.")
        # Bottom
        self.update(-1, 0, f"'{self.text_width * '-'}'")

        # Add side pieces
        for row in range(self.height):
            for col in range(self.width):
                if 0 < row < self.height-1:
                    if col == 0:
                        self.update(row, col, "|")
                    elif col == self.width - 1:
                        self.update(row, col, "|")


class Fightbox(Textbox):
    def __init__(self, x=15, y=2):
        super().__init__(x, y)

        # Add Entries
        entry = ['Fight', 'Items', 'Party', 'Run']
        ''' entries can be a list input and then we sort depending on the number of rows, length of text, etc.'''
        self.update(1, 2, 'Fight')
        self.update(1, 10, 'Items')  # 3 spaces
        # self.update(row#, col#, item)
        # self.update(row#, col# + len(item) + Num_spaces, item)

        self.update(2, 2, 'Party')
        self.update(2, 10, 'Run')


class StartMenu(Textbox):
    def __init__(self):
        super().__init__(11, 6)

        # Add Entries
        # self.update(row#, col#, item)
        # self.update(row#, col# + len(item) + Num_spaces, item)
        ''' entries can be a list input and then we sort depending on the number of rows, length of text, etc.'''
        self.update(1, 2, 'Status')
        self.update(2, 2, 'Items')
        self.update(3, 2, 'Equipment')
        self.update(4, 2, 'Party')
        self.update(5, 2, 'Options')
        self.update(6, 2, 'Exit')


class Screen:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.center = round(self.height/2)
        self.rows = []

    def add_container(self, container, side='l'):
        new_row = None
        if container.width < self.width:
            diff = self.width - container.width
            temp = Container(diff, container.height)
            if side == 'l':
                new_row = container + temp
            elif side == 'r':
                new_row = temp + container
            self.rows.append(new_row)

        if container.height > self.height:
            pass

    def show(self):
        for row in self.rows:
            print(row)


class Battle(Screen):
    def __init__(self):
        super().__init__(20, 40)

        size_x = 15
        size_y = 2

        fight_box = Fightbox(size_x, size_y)

        fi = Textbox(size_x, size_y)
        fi.update(1, 2, f"HP: [======]")
        fi.update(2, 2, f"MP:  (======)")

        self.add_container(fi, 'l')
        self.add_container(fight_box, 'r')


class MainMenu(Screen):
    def __init__(self):
        super().__init__(40, 80)

        # Create Containers
        title = Textbox(40, 5)
        title.update(3, 14,  "Program Name")
        title.update(5, 35, f"V 1.0")

        author = Container(40, 2)
        author.update(0, 30, f"by - rickyg3")

        # l and r justify to Screen size not container size
        self.add_container(title, 'l')
        self.add_container(author, 'l')


class Menu(Screen):
    def __init__(self):
        super().__init__(20, 40)

        items = ["Status", "Party", "Items", "Equipment", "Options", "Exit"]

        mm = StartMenu()

        self.add_container(mm, 'l')


''' Creating and printing '''
# c = Container()
# print(c)


''' Line '''
# for i in range(3):
#     for j in range(15):
#         if i == 0:
#             c.update(i, j, ' ')


''' Container/Text Box '''
# fight_box = Container()
#
# size_x = 15
# size_y = 2
# fight_box.set_size(size_x, size_y)
# OR
# size_x = 15
# size_y = 2
#
# fight_box = Fightbox(size_x, size_y)
#
#
# fi = Textbox(size_x, size_y)


#empty = Container(size_x + 6, size_y + 2)

# Screen Class
# battle_screen = Screen(20, 40)


if __name__ == "__main__":
    # Opening Screen
    clear_screen()
    M = MainMenu()
    M.show()
    input("Press Enter to Continue...")

    # Start Menu
    clear_screen()
    startmenu = Menu()
    startmenu.show()
    u_input = input(f"| ")

    # Battle Menu
    clear_screen()
    battle_screen = Battle()
    battle_screen.show()
    user_input = input(f"{(13 + battle_screen.center) * ' '}| ")  # replace spaces with character status or other info

