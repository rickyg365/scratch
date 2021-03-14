import os


class Object():
    def __init__(self, obj_id):
        # References a txt or json file with all objects and their attributes using ID
        self.data = {"001": [
                         "E",
                         "Enemy",
                         "Starts a fight"
                     ],
                     "002": [
                         "#",
                         "Treasure chest",
                         "contains gold or an item"
                     ],
                     "004": [
                         "|",
                         "vertical wall",
                         "blocks horizontal movement"
                     ],
                     "005": [
                         "-",
                         "horizontal wall",
                         "blocks vertical movement"
                     ],
                     "003": [
                         "$",
                         "Merchant",
                         "Buy and sell items"
                     ]}  # {"obj_id": [obj_attributes]}

        self.obj_id = obj_id
        self.char = self.data[obj_id][0]

    def __str__(self):
        return self.char


class Map():
    def __init__(self):
        self.height = 11
        self.width = 21

        self.center = [(self.height//2), (self.width//2)]
        # Can be maybe a separate class?
        # Can do a list of of custom object objects or maybe a dictionary with the object id and a position?
        self.objects = {"0_0": "001", "1_1": "002", "10_20": "003"}  # {"i_j": "Object_id"}
        self.character = '@'
        #
        self.display = []

        # Initialize display
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(" ")
            self.display.append(row)

    def display_screen(self):
        screen = ""  # "\n"

        # for row in self.display:
        #     for value in row:
        #         screen += value
        #     screen += '\n'

        for i in range(self.height):
            for j in range(self.width):
                obj = self.check_obj(i, j)
                if obj is None:
                    if i == self.center[0] and j == self.center[1]:
                        screen += self.character
                    else:
                        screen += self.display[i][j]
                else:
                    screen += f"{obj}"
            screen += '\n'
        print(screen)

    def check_obj(self, i_pos, j_pos):
        pos = f"{i_pos}_{j_pos}"

        if pos not in self.objects.keys():
            return None
        else:
            return Object(self.objects[pos])


d = Map()
d.display_screen()


class Movement():
    def __init__(self, starting_x=0, starting_y=0):
        self.starting_point = [starting_x, starting_y]
        self.x = starting_x
        self.y = starting_y
        self.current_point = ""

        self.directions = {'w': 'up',
                           'a': 'left',
                           's': 'down',
                           'd': 'right'}

        self.log = []

    def __str__(self):
        return f"{self.starting_point} -> {self.current_point}"

    def validate(self, input_val):
        if input_val in self.directions.keys():
            return True
        else:
            return False

    def act(self, uinput):
        check = self.validate(uinput)

        if check:
            action = self.directions[uinput]

            if action == 'up':
                self.y += 1
            elif action == 'left':
                self.x -= 1
            elif action == 'down':
                self.y -= 1
            elif action == 'right':
                self.x += 1
            self.current_point = [self.x, self.y]
        else:
            print("Input not mapped")


# m = Movement()
# m.act('w')
# print(m)
# m.act('w')
# m.act('w')
# print(m)
