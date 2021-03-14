import os

""" 
Program: Periodic Table
Author: rickyg3
03/12/2021
"""
# Make a webscraper to extract this data


class Element:
    def __init__(self, ele_name, ele_symbol, ele_num, ele_mass):
        self.name = ele_name
        self.symbol = ele_symbol
        self.atomic_number = ele_num
        self.atomic_mass = ele_mass

    def __str__(self):
        return f"{self.symbol} | Atomic number: {self.atomic_number}"


class PeriodicTable:
    def __init__(self):
        self.elements = []

    def __str__(self):
        txt = ""

        for element in self.elements:
            txt += f"\n{element}"

        return txt
