import os
from utility import buildHPBar, box
from items import Bag, Item, HealItem

class Player:
    def __init__(self, name, job="warrior", prebuilt_bag=None):
        if prebuilt_bag is None:
            prebuilt_bag = {}

        self.name = name
        self.job = job

        self.bag = Bag(prebuilt_bag)

        self.is_alive = True

        # Stats
        self.hp = 40

        self.atk = 12
        self.res = 8
        self.spd = 11
        
        self.current_hp = 40


    def __str__(self):

        hp_length = 10
        healthbar = buildHPBar(self.current_hp, self.hp, hp_length)  # static length of 10
        total_length = hp_length + 5

        inner_txt = [
            f" {self.name.capitalize():{total_length-5}}    ",
            f" HP {healthbar} "
        ]

        txt = box(inner_txt, 'round', 'right')

        return txt

    def status_screen():
        ...

    def take_dmg(self, enemy_atk):
        total_dmg = enemy_atk - self.res

        self.current_hp -= total_dmg

        # check if current hp < 0
        if self.current_hp <= 0:
            self.is_alive = False
            return False, "You Died!"

        return True, f"Took {total_dmg} dmg!"

    def deal_dmg(self, enemy_res_amount):
        dmg_dealt = self.atk - enemy_res_amount
        return True, f"Dealt {dmg_dealt} dmg!"

    def heal(self, heal_amount):
        if self.current_hp == self.hp:
            return False, f"Healing Failed! Full HP"

        self.current_hp += heal_amount
        
        if self.current_hp > self.hp:
            result_txt = f"Healing Overload: {self.current_hp - self.hp} HP wasted..."
            self.current_hp = self.hp
            return False, result_txt
        return True, f"Healed {heal_amount}! Current Health -> {self.current_hp}"
    

class Enemy:
    def __init__(self):
        self.name = "Enemy"
        self.is_alive = True

        # Stats
        self.hp = 30

        self.atk = 10
        self.res = 8
        self.spd = 10
        
        self.current_hp = 30


    def __str__(self):
        # len(healthbar) + 5
        # len(self.name) + 11

        hp_length = 10
        healthbar = buildHPBar(self.current_hp, self.hp, hp_length)  # static length of 10

        total_length = hp_length + 5

        inner_txt = [
            f" {self.name:{total_length-5}}    ",
            f" HP {healthbar} "
        ]

        txt = box(inner_txt, 'round')
        
        return txt
    
    def take_dmg(self, enemy_atk):
        total_dmg = enemy_atk - self.res

        self.current_hp -= total_dmg

        # check if current hp < 0
        if self.current_hp <= 0:
            self.is_alive = False
            return False, f"Enemy defeated!"
        return True, ""

    def heal(self, heal_amount):
        self.current_hp += heal_amount
        if self.current_hp > self.hp:
            self.current_hp = self.hp
            return False, f"Healing Failed! {self.current_hp - self.hp} HP wasted"
        result_txt = f"Healed {heal_amount}! Current Health -> {self.current_hp}"
        # return True, result_txt
        return True, result_txt