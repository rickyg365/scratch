import random

"""
Program: Random Address Generator
Author: Rickyg3
Date: 07/08/2021
"""

'''
NOTES:

What we can do is make it choose a state first and then that'll limit which cities 
and which streets to use for each city.

Really need a database so that the random addresses are better.

'''


class Address:
    # Use these for now, use database later hehe
    PREFIXES = [
        "South",
        "North",
        "East",
        "West"
    ]
    SUFFIXES = [
        "BLVD",
        "Place",
        "Street",
        "Avenue"
    ]
    STREET_NAMES = [
        "Martin Luther King",
        "Main",
        "Figuroa",
        "Foothill",
        "Vermont",
        "Euclid",
        "Trifling",
        "Crenshaw",
        "Hoover"
    ]
    CITIES = [
        "Los Angeles",
        "Seattle",
        "New York",
        "Chicago",
        "Upland",
        "Montclair",
        "Tolleson",
        "Avondale"
    ]
    STATES = [
        "Kentucky",
        "Arizona",
        "Washington",
        "Oregon",
        "California",
        "New Mexico",
        "Texas",
        "Nevada",
        "Utah"
    ]

    def __init__(self):
        self.street_num = 0
        self.prefix = ""
        self.street_name = ""
        self.suffix = ""
        self.city = ""
        self.state = ""
        self.zip_code = ""

        # Number of Choices
        self.pre_count = len(self.PREFIXES)
        self.suf_count = len(self.SUFFIXES)
        self.street_count = len(self.STREET_NAMES)
        self.city_count = len(self.CITIES)
        self.state_count = len(self.STATES)

        self.has_pre = False
        self.has_suf = False

        self.randomize()

    def __str__(self):
        text = f"{self.street_num} "

        if self.has_pre:
            text += f"{self.prefix} "

        text += f"{self.street_name} "

        if self.has_suf:
            text += f"{self.suffix} "

        text += f"{self.city} {self.state} {self.zip_code}"

        return text

    def prefix_suffix_chance(self):
        p_chance = random.randint(0, 100)
        s_chance = random.randint(0, 100)

        if p_chance > 50:
            self.has_pre = True

        if s_chance > 50:
            self.has_suf = True

    def randomize_num(self):
        d1 = random.randint(0, 9999)

        self.street_num = f"{d1}"

    def randomize_street(self):
        r = random.randint(0, self.street_count - 1)
        self.street_name = self.STREET_NAMES[r]

    def randomize_city(self):
        r = random.randint(0, self.city_count - 1)
        self.city = self.CITIES[r]

    def randomize_state(self):
        r = random.randint(0, self.state_count - 1)
        self.state = self.STATES[r]

    def randomize_pre(self):
        r = random.randint(0, self.pre_count - 1)
        self.prefix = self.PREFIXES[r]

    def randomize_suf(self):
        r = random.randint(0, self.suf_count - 1)
        self.suffix = self.SUFFIXES[r]

    def randomize(self):
        self.prefix_suffix_chance()

        self.randomize_num()
        if self.has_pre:
            self.randomize_pre()
        self.randomize_street()

        if self.has_suf:
            self.randomize_suf()

        self.randomize_city()
        self.randomize_state()

    def reset(self):
        self.street_num = 0
        self.prefix = ""
        self.street_name = ""
        self.suffix = ""
        self.city = ""
        self.state = ""
        self.zip_code = ""

        self.has_pre = False
        self.has_suf = False


if __name__ == "__main__":
    user = input("How many times should we loop?: ")

    for _ in range(int(user)):
        new_obj = Address()
        print(new_obj)
