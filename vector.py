import os

from math import hypot
"""
Author: Python Genius @Instagram
03/12/2021
"""


class Vector(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"<{self.x},{self.y}>"

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(self.x or self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


class Calc():
    def __init__(self):
        self.display = ""
        self.entry1 = None
        self.operation = ""
        self.entry2 = None
        self.solution = None
        self.prev_solution = None

    def __str__(self):
        return self.display

    def input_value(self, val):
        if self.entry1 is None:
            self.entry1 = val
        elif self.entry2 is None:
            self.entry2 = val
        else:
            print("clear values")

    def input_operation(self, op):
        valid_operations = "+-*/"
        if op in valid_operations:
            self.operation = op
        else:
            print("Invalid Operation")

    def solve(self):
        if self.operation == "+":
            self.solution = self.entry1 + self.entry2
        elif self.operation == "-":
            self.solution = self.entry1 - self.entry2
        elif self.operation == "*":
            try:
                self.solution = self.entry1 * self.entry2
            except TypeError:
                self.solution = self.entry2 * self.entry1
        elif self.operation == "/":
            self.solution = self.entry1/self.entry2
        else:
            print("Couldn't find operation //solve func.")

    def update_display(self):
        if self.entry1 is None:
            self.display = ""
        elif self.operation == '':
            self.display = f"{self.entry1} "
        elif self.entry2 is None:
            self.display = f"{self.entry1} {self.operation}"
        elif self.solution is None:
            self.display = f"{self.entry1} {self.operation} {self.entry2}"
        else:
            self.display = f"{self.entry1} {self.operation} {self.entry2} = {self.solution}"
            # print("check update display func")

    def clear(self):
        self.display = ""
        self.entry1 = None
        self.operation = ""
        self.entry2 = None
        self.prev_solution = self.solution
        self.solution = None


if __name__ == "__main__":
    # user_input = input("Please input a vector(x y): ")
    # x, y = user_input.split(" ")
    #
    # vector = Vector(int(x), int(y))
    # magnitude = abs(vector)
    #
    # scalar_mul = abs(vector * 2)
    # vector_mul = vector * 2
    #
    # print(f"\nVector: {vector}"
    #       f"\nMagnitude: {magnitude}"
    #       f"\nScalar Multiple: {scalar_mul}"
    #       f"\nVector *2: {vector_mul}\n")

    c = Calc()

    running = True
    while running:
        os.system("cls")
        print(c.display)
        # print(f"+-{len(c.display)*'-'}-+"
        #       f"\n| {c.display} |"
        #       f"\n+-{len(c.display)*'-'}-+")

        user_input = input("\n>>> ")
        # format = v# # or operation(+-*/)

        if user_input == "c":
            c.clear()
        elif user_input[0] == 'v' and len(user_input) >= 4:
            x = user_input[1]
            y = user_input[3]
            c.input_value(Vector(int(x), int(y)))
        elif user_input in "+-*/":
            c.input_operation(user_input)
        elif user_input == "=":
            c.solve()
        elif user_input == 'q':
            running = False
        elif int(user_input) > 0:
            c.input_value(int(user_input))
        else:
            print("Invalid Input")

        c.update_display()

