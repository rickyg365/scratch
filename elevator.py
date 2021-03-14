import os


class Elevator():
    def __init__(self, initial_instructions=""):
        self.starting_floor = 0
        self.current_floor = 0
        self.instructions = initial_instructions

        self.instruct(initial_instructions)

    def __str__(self):
        return f"{self.starting_floor} -> {self.current_floor}"

    def instruct(self, instructions):
        self.instructions = instructions
        for ins in instructions:
            if ins == "(":
                self.current_floor += 1
            elif ins == ")":
                self.current_floor -= 1
            else:
                print("Invalid entry skipping over it")


if __name__ == "__main__":
    secret = input("Enter instructions: ")

    e = Elevator(secret)
    print(e)
