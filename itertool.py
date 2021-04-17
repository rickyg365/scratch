import itertools
from itertools import *

import time

card_values = ['K',
               'Q',
               'J',
               'X',
               '9',
               '8',
               '7',
               '6',
               '5',
               '4',
               '3',
               '2',
               'A']
card_values.reverse()
card_suits = [u'\N{black club suit}', u'\N{black diamond suit}', u'\N{black heart suit}', u'\N{black spade suit}']

cards = itertools.product(card_suits, card_values)

'''
.----------------.
| Xs             |
|                |
|                |
|        s       |
|                |
|                |
|            Xs  |
'----------------'


'''

def make_ascii_card(card_suit, card_value):
    ascii_card = "\n"
    ascii_card += f"\n.----------------."
    ascii_card += f"\n| {card_value}{card_suit}             |"
    ascii_card += f"\n|                |"
    ascii_card += f"\n|                |"
    ascii_card += f"\n|                |"
    ascii_card += f"\n|        {card_suit}       |"
    ascii_card += f"\n|                |"
    ascii_card += f"\n|                |"
    ascii_card += f"\n|                |"
    ascii_card += f"\n|             {card_value}{card_suit} |"
    ascii_card += f"\n'----------------'"
    ascii_card += f"\n"
    # ascii_card += f""
    return ascii_card


for card in cards:
    suit = card[0]
    val = card[1]
    print(make_ascii_card(suit, val))
    # print(f"{card[0]} {card[1]}")
    time.sleep(1)
