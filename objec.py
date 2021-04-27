import os

import re

import random

"""
class Person


class Car


sample names:

robert nichi 
ethan hawking
neil degrasse tyson
ash ketchum
ash

"""


class Person:
    def __init__(self, full_name='first middle last'):
        name_pattern = r'^([a-zA-Z]{2,}\s)([a-zA-Z]{2,})'
        matches = re.search(name_pattern, full_name)

        self.first_name = matches[1]
        # if matches[1]:
        #     self.middle_name = matches[1]
        if matches[2]:
            self.last_name = matches[2]
        self.garage = ['Rolls Royce', 'AUDI', 'BMW']

    def __str__(self):
        text = f"f:{self.first_name} l:{self.last_name}\n{self.first_name}'s Garage:\n"
        for ind, car_name in enumerate(self.garage):
            text += f"\nCar {ind + 1}: {car_name}"
        return text


class Car:
    def __init__(self):
        pass

    def __str__(self):
        text = ""
        return text


if __name__ == "__main__":
    name = input("Yo whats your name?: ")
    print("")
    new_person = Person(name)
    print(new_person)
