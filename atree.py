import os
import time

import requests
from bs4 import BeautifulSoup

from anytree import Node, RenderTree


if __name__ == "__main__":

    # Root
    starters = Node("Starters")

    # Kanto Region [#1]
    kanto = Node("Kanto", parent=starters)

    # Kanto Starters
    kanto_grass = Node("Grass", parent=kanto)

    bulbasaur = Node("Bulbasaur", parent=kanto_grass)
    ivysaur = Node("Ivysaur", parent=kanto_grass)
    venusaur = Node("Venusaur", parent=kanto_grass)

    kanto_water = Node("Water", parent=kanto)

    squirtle = Node("Squirtle", parent=kanto_water)
    wartortle = Node("Wartortle", parent=kanto_water)
    blastoise = Node("Blastoise", parent=kanto_water)

    kanto_fire = Node("Fire", parent=kanto)

    charmander = Node("Charmander", parent=kanto_fire)
    charmeleon = Node("Charmeleon", parent=kanto_fire)
    charizard = Node("Charizard", parent=kanto_fire)

    # Johto Region [#2]
    johto = Node("Johto", parent=starters)

    # Johto Starters
    johto_grass = Node("Grass", parent=johto)

    chikorita = Node("Chikorita", parent=johto_grass)
    bayleef = Node("Bayleef", parent=johto_grass)
    meganium = Node("Meganium", parent=johto_grass)

    johto_water = Node("Water", parent=johto)

    totodile = Node("Totodile", parent=johto_water)
    croconaw = Node("Croconaw", parent=johto_water)
    feraligatr = Node("Feraligatr", parent=johto_water)

    johto_fire = Node("Fire", parent=johto)

    cyndaquil = Node("Cyndaquil", parent=johto_fire)
    quilava = Node("Quilava", parent=johto_fire)
    typhlosion = Node("Typhlosion", parent=johto_fire)

    # Display Tree
    for pre, fill, node in RenderTree(starters):
        print("%s%s" % (pre, node.name))
