import os

import re
import time
import datetime


"""
Program: Parking Garage System
Date: 05/07/2021
"""


class Garage:
    current_id = 1

    def __init__(self, start=(0, 0), end=(0, 0)):
        self.garage_id = self.current_id
        Garage.current_id += 1
        # Should I do a tuple with 3 values: (Hour, Minutes)
        self.start_time = start
        self.end_time = end  # (0, 0)

    def __str__(self):
        text = f"[{self.garage_id:03}]: Start: {self.start_time[0]:02}:{self.start_time[1]:02}  End: {self.end_time[0]:02}:{self.end_time[1]:02} "

        return text


class Customer:
    def __init__(self):
        ...

    def __str__(self):
        text = ""

        return text


class Car:
    def __init__(self):
        self.make = ""
        self.model = ""
        self.year = ""

    def __str__(self):
        text = ""

        return text


class ReservationSystem:
    def __init__(self):
        self.available_spots = []
        self.unavailable_spots = []
        self.garages = []

    def __str__(self):
        text = ""

        return text

    def reserve_spot(self):
        # Is it users choice which spot or what do we need to make a smart system to auto choose the best spot
        ...


if __name__ == "__main__":
    parking = ReservationSystem()
    for i in range(10):
        new_garage = Garage()
        parking.available_spots.append(new_garage)

    print("\nAvailable Spots: ")
    for spot in parking.available_spots:
        print(spot)
