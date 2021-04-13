import os


"""
Program: Byte Categorizer
Author: @python_genius, insta
Date: 04/12/21
"""


class GetSize(object):
    def __init__(self, bytes_=0):
        self.bytes_ = bytes_
        self.factor = 1024
        self.units = ["", "K", "M", "G", "T", "P"]

    def size_categorize(self):
        for unit in self.units:
            if self.bytes_ < self.factor:
                return f"{self.bytes_:.2f}{unit}B"
            self.bytes_ /= self.factor

    def __str__(self):
        return str(self.size_categorize())


if __name__ == "__main__":
    print(GetSize(735256437))
