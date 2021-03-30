import os
import sys

import time

""" 
Program: 
Author: rickyg3
Date: 
"""


class Character:
    """
    Character class is just a container for any non-playable character.

    sample character:

    self.name = character_name
    self.stats = {
        dialogue: "Howdy do"
        movement: [left, right, up, left, down, right]  # No net movement
    }
    """
    def __init__(self, character_name=""):
        self.name = character_name
        self.stats = {}

    def __str__(self):
        # Display
        display_width, display_rows = os.get_terminal_size()

        text = ""
        text += self.name
        text += f"\n{display_width * '-'}"
        for key, item in self.stats.items():
            text += f"\n{key.capitalize()}: {item}\n"

        text += f"\n{display_width * '-'}"

        return text


class Player(Character):
    """
    Players are playable characters

    sample stats:

    stats = {
        hp: 100
        max_hp: 120
        atk: 12
        res: 8
        spd: 10
    }
    """
    def __init__(self, player_name=""):
        super().__init__(player_name)
        self.is_alive = True

    def __str__(self):
        # Display
        display_width, display_rows = os.get_terminal_size()

        text = ""
        text += self.name
        text += f"\n{display_width*'-'}"
        for key, item in self.stats.items():
            text += f"\n{key.capitalize()}: {item}\n"

        text += f"\n{display_width * '-'}"

        return text


class PlayerCollection:
    def __init__(self):
        self.players = []

    def __str__(self):
        text = ""
        for player in self.players:
            text += f"{player.name}"
        return text


class MainCharacter(Player):
    # Should I make a character class specifically for playable characters instead of inheriting from players any
    # playable can inherit from that character class
    def __init__(self, main_character_name=""):
        super().__init__(main_character_name)
        self.is_alive = True
        self.is_defending = False

    def __str__(self):
        text = f"{self.name}"
        return text

    def heal(self, update_amount):
        diff = self.stats["max_hp"] - self.stats['hp']
        surplus = self.stats['hp'] > self.stats['max_hp']
        if diff == 0:
            print(f"Already full health!")
            return False
        else:
            self.stats['hp'] += update_amount
            if surplus:
                self.stats['hp'] = self.stats['max_hp']
        return True

    def take_damage(self, damage_amount):
        if self.is_defending:
            diff = self.stats['hp'] - (damage_amount - self.stats['res'])
        else:
            diff = self.stats['hp'] - damage_amount

        if diff < 0:
            self.is_alive = False
        else:
            self.stats['hp'] -= damage_amount
        return

    def attack(self, player_object):
        # Find Try except
        atk = self.stats["atk"]

        player_object.take_damage((atk-player_object.stats['res']))

    def defend(self):
        self.is_defending = True


class NPC(Character):
    def __init__(self, npc_name=""):
        super().__init__(npc_name)

    def __str__(self):
        text = f"{self.name}"
        return text


if __name__ == "__main__":
    pass

