import os
import random


def repeater(func):
    def inner(a):
        count = int(input("How many times would you like to repeat?: "))
        for i in range(count):
            func(a)
    return inner


class RandomList:
    def __init__(self, list_length=1):
        self.length = list_length
        self.data = []
        self.bounds = (1, 50)

    def __str__(self):
        text = f"{self.data}"
        return text

    def rand_list(self):
        self.data = []
        for _ in range(self.length):
            rand_int = random.randint(self.bounds[0], self.bounds[1])
            self.data.append(rand_int)
        print(self.data)

    @repeater
    def set_attr(self):
        self.length = int(input("\nChoose list length: "))
        self.rand_list()


if __name__ == "__main__":
    new_list = RandomList()

    new_list.set_attr()

    # print(new_list)
