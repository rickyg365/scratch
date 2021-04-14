import os


"""
Program: Unit Converter
Author: rickyg3
Date: 04/12/2021
"""


class ConvertUnit(object):
    def __init__(self, raw_input):
        self.value = self.parse(raw_input)
        self.units = ["m", "c", "d", "", "da", "h", "km"]

    def parse(self, input):
        pass

