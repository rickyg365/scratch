import os

"""
To Do:
    1. __add__ addition operator to container class so I can lay things out better under the screen class
    2. add_container add take in matrix functionality
    3. Dungeon Traversal via linked nodes
    
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
    os.system("clear")


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
        self.update(1, 3, 'Fight')
        self.update(1, x-6, 'Items')  # 3 spaces
        # self.update(row#, col#, item)
        # self.update(row#, col# + len(item) + Num_spaces, item)

        self.update(y, 3, 'Party')
        self.update(y, x-6, 'Run')


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
        super().__init__(20, 60)

        size_x = 19
        size_y = 2

        # User Status
        user_stat = Textbox(size_x, 5)
        user_stat.update(1, 1, f"  HP:[==========] ")
        user_stat.update(2, 1, f"  MP:(==========) ")
        user_stat.update(3, 0, f".-------------------.")
        user_stat.update(4, 1, f"  Fight     Items  ")
        user_stat.update(5, 1, f"  Party     Run    ")

        fight_box = Fightbox(size_x, size_y)
        # fight_box = Fightbox(size_x+4, size_y+2)

        # fi = Textbox(size_x, size_y)
        # fi.update(1, 2, f"HP: [======]")
        # fi.update(2, 2, f"MP:  (======)")

        # fi = Textbox(18, 4)
        # fi.update(1, 2, f"Enemy Name")
        # fi.update(3, 2, f"HP: [========]")
        # fi.update(4, 2, f"MP:  (========)")

        fi = Textbox(19, 4)
        fi.update(1, 2, f"Enemy Name")
        # Status
        status = 'burn'
        spacing = 19 - len(status)
        if status == 'burn':
            fi.update(1, spacing, "frzn")

        fi.update(2, 1, f"-------------------")
        fi.update(3, 2, f"HP: [==========]")
        fi.update(4, 2, f"MP:  (==========)")

        empt = Container(1, 4)

        self.add_container(fi, 'l')
        self.add_container(empt)
        self.add_container(user_stat, 'r')
        # self.add_container(fight_box, 'r')


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


class OverWorld(Screen):
    def __init__(self):
        super().__init__(40, 80)

        # Create Containers
        world_map = Textbox(70, 22)

        world_map.update(1, 1, 'Start')
        world_map.update(3, 2, ",.#'''-.,")
        world_map.update(4, 2, "| Heart |")
        world_map.update(5, 2, ";_    ,_;")
        world_map.update(6, 2, "  '-.,'")

        self.add_container(world_map)


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

    # Create Menus that are static
    def run_start():
        start_menu = Menu()
        run = True

        while run:
            clear_screen()
            start_menu.show()

            user_inp = input(f"| ")

            if user_inp == "status":
                pass
            elif user_inp == "items":
                pass
            elif user_inp == "equipment":
                pass
            elif user_inp == "party":
                pass
            elif user_inp == "options":
                pass
            elif user_inp == "exit":
                run = False
            else:
                print("Invalid Input")

    def run_battle():
        battle_screen = Battle()
        battle = True

        while battle:
            clear_screen()
            battle_screen.show()
            user_in = input(f"{(battle_screen.width - 21) * ' '}| ")  # replace spaces w/ character status or info


    def run_overworld():
        over_world = OverWorld()
        clear_screen()
        over_world.show()

        return input("[]: start []: battle []: quit\n \n>over_world>main_char> ")

    # start_menu = Menu()
    # battle_screen = Battle()  # Static for now but will change depending on enemy later
    # over_world = OverWorld()

    # Main Game Loop
    running = True

    while running:
        # clear_screen()
        # over_world.show()
        # u_in = input("[]: start []: battle []: quit\n \n>over_world>main_char> ")
        u_in = run_overworld()

        # Use regex for pattern matching
        if u_in.lower() == 'start':
            # Start Menu
            # u_input = run_start()
            run_start()

        elif u_in.lower() == 'battle':
            # Battle Menu
            run_battle()
            # Battle menu class or function

        elif u_in.lower() == 'q':
            running = False
