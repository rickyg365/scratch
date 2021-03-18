import os
import sys


""" 
Program: Celestial Objects
Author: rickyg3
Date: 03/17/2021
"""


class CelestialCollection:
    def __init__(self, name, size, data=None):
        if data is None:
            data = []
        self.name = name
        self.size = size
        self.data = data

    def __str__(self):
        text = ""

        for count, data in enumerate(self.data):
            text += f"{count+1}. {data}\n \n"
        return text

    def add_body(self, body_obj):
        self.data.append(body_obj)


class CelestialBody:
    def __init__(self, name, mass, size):
        self.name = name
        self.mass = mass
        self.size = size

    def __str__(self):
        text = f"{self.name}\nMass: {self.mass} kg\tSize: {self.size} km"

        return text


class Galaxy(CelestialCollection):
    def __init__(self, galaxy_name="", galaxy_size=None):
        super().__init__(galaxy_name, galaxy_size)

    def __str__(self):
        text = f"{self.name}:\n \n"
        for count, item in enumerate(self.data):
            text += f"  {count+1}: {item.name} [{item.star}]\n"
        return text


class StarSystem(CelestialCollection):
    def __init__(self, star_obj, system_name="", system_size=None):
        super().__init__(system_name, system_size)
        self.star = star_obj.name
        self.data.append(star_obj)

    # def __str__(self):
    #     text = ""
    #     return text


class Star(CelestialBody):
    def __init__(self, star_name="", system_name="", star_mass=None, star_size=None):
        super().__init__(star_name, star_mass, star_size)
        self.system_name = system_name

    # def __str__(self):
    #     text = ""
    #     return text


class Planet(CelestialBody):
    def __init__(self, planet_name="", planet_mass=None, planet_size=None):
        super().__init__(planet_name, planet_mass, planet_size)
        self.distance_to_star = 0

    # def __str__(self):
    #     text = ""
    #     return text


if __name__ == "__main__":
    # Create Objects

    # Star Object
    sun = Star("Sun", "Solar System", 1.99e30, 695508)
    # Terrestrial/Rocky Planets
    mercury = Planet("Mercury", 5.97e24, 6378.137)
    venus = Planet("Venus", 5.97e24, 6378.137)
    earth = Planet("Earth", 5.97e24, 6378.137)
    mars = Planet("Mars", 5.97e24, 6378.137)
    # GaseousGiant Planets
    jupiter = Planet("Jupiter", 5.97e24, 6378.137)
    saturn = Planet("Saturn", 5.97e24, 6378.137)
    uranus = Planet("Uranus", 5.97e24, 6378.137)
    neptune = Planet("Neptune", 5.97e24, 6378.137)
    pluto = Planet("Pluto", 5.97e24, 6378.137)

    # Solar System
    solar_system = StarSystem(sun, sun.system_name)

    solar_system.add_body(mercury)
    solar_system.add_body(venus)
    solar_system.add_body(earth)
    solar_system.add_body(mars)

    solar_system.add_body(jupiter)
    solar_system.add_body(saturn)
    solar_system.add_body(uranus)
    solar_system.add_body(neptune)
    solar_system.add_body(pluto)

    # Galaxy
    milky_way = Galaxy("Milky Way")
    milky_way.add_body(solar_system)

    # Display
    width, rows = os.get_terminal_size()

    # Top Border
    print(f"{width//2 * '_'}\n")

    # Galaxy
    title = "[Galaxy]"
    # print(f"{title}{(width//2-len(title)) * '_'}\n" )
    print(f"{title} {milky_way}")

    # Star System
    title = "[Star System]"
    print(f"{width // 2 * '-'}\n")
    print(f"{title} {solar_system.name}:\n")
    print(solar_system)

    # Celestial Body info
    title = "[Solar System]"
    print(f"{width // 2 * '-'}\n")
    print(f"{title} Heavenly Body Info:\n")
    for system in solar_system.data:
        if system.name == "Sun":
            pass
        else:
            print(system)
            print("")
    # print(f"{earth}\n \n{sun}")
    print(f"{width//2 * '_'}\n")

'''
milky_way.solar_system.earth

Milky Way
    '-> Solar System
            '-> Earth
'''
