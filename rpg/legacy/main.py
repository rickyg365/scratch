import os
import sys
import time

'''
■


▄
▅
▆
▇
□
.---------------.
| Jojo          |
| HP ■■■■■■■■□□ |
'---------------'
    
    Job: warrior
     
    HP : 40
    ATK: 12
    RES: 8
    SPD: 11

'''

#         txt = f"""
# ╭{'─'*total_length}╮
# │ {self.name.capitalize():{total_length-5}}    │
# │ HP {healthbar} │  
# ╰{'─'*total_length}╯
# """

def clear_screen():
    platform = sys.platform

    if platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')

def buildHPBar(hp_amount, total_hp, hp_bar_length=10):
    hp_fraction = hp_amount/total_hp 
    hp_in_bar = int(hp_fraction * hp_bar_length)
    free_space = hp_bar_length - hp_in_bar

    new_bar = f"{'■'*hp_in_bar}{'□'*free_space}" 
    
    return new_bar


def box(inner_text:list[str], style_choice="round", justify='left') -> str:
    """ assuming every line is the same length """
    if justify == 'right':
        cols, rows = os.get_terminal_size()

    num_lines = len(inner_text)
    line_length = len(inner_text[0])

    styles = {
        "regular": {
            'tlcorner': '┌',
            'trcorner': '┐',
            'blcorner': '└',
            'brcorner': '┘',
            'horizontal': '─',
            'vertical': '│'
        },
        "bold": {
            'tlcorner': '┏',
            'trcorner': '┓',
            'blcorner': '┗',
            'brcorner': '┛',
            'horizontal': '━',
            'vertical': '┃'
        },
        "round": {
            'tlcorner': '╭',
            'trcorner': '╮',
            'blcorner': '╰',
            'brcorner': '╯',
            'horizontal': '─',
            'vertical': '│'
        }
    }

    current_style = styles[style_choice]

    # Top Row
    final_box = ""

    if justify == 'right':
        top_row = f"{current_style['tlcorner']}{current_style['horizontal']*line_length}{current_style['trcorner']}"
        final_box += f"{top_row:>{cols}}"
    else:
        final_box += f"{current_style['tlcorner']}{current_style['horizontal']*line_length}{current_style['trcorner']}"
    
    # Dynamic Middle
    for i in range(num_lines):
        if justify == 'right':
            new_row = f"{current_style['vertical']}{inner_text[i]}{current_style['vertical']}"
            final_box += f"\n{new_row:>{cols}}"
            continue
        final_box += f"\n{current_style['vertical']}{inner_text[i]}{current_style['vertical']}"

    # Bot Row
    if justify == 'right':
        final_row = f"{current_style['blcorner']}{current_style['horizontal']*line_length}{current_style['brcorner']}"
        final_box += f"\n{final_row:>{cols}}"
    else:
        final_box += f"\n{current_style['blcorner']}{current_style['horizontal']*line_length}{current_style['brcorner']}"
    
    return final_box


class Player:
    def __init__(self, name, job="warrior"):
        self.name = name
        self.job = job

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
            result_txt = f"Healing 404: {self.current_hp - self.hp} HP wasted..."
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


class Item:
    def __init__(self):
        pass

    def __str__(self):
        txt = ""
        return txt


class Bag:
    def __init__(self):
        pass

    def __str__(self):
        txt = ""
        return txt


class Battle:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def __str__(self) -> str:
        txt = ""
        return txt

    def run(self):
        turn_queue = []

        cols, rows = os.get_terminal_size()

        enemy_first = False

        if self.player.spd < self.enemy.spd:
            enemy_first = True

        turn_summary = ""
        while True:
            if enemy_first:
                # Enemy Turn
                turn_summary += "Enemy Attacks:"
                turn_stat, turn_result = self.player.take_dmg(self.enemy.atk)
                turn_summary += f"\n{turn_result}\n\n"

                # Check if they alive, can maybe use turn stat instead
                '''
                if not turn_stat:
                    if turn_status == 'dead':
                        print("Character Lost!)
                '''
                if not self.enemy.is_alive:
                    print("Hero won")
                    break

                if not self.player.is_alive:
                    print("You have been DEFEATED.")
                    break

            clear_screen()
            print(self.enemy)
            print(self.player)
            print(f"{'-'*cols}")
            # print(turn_summary)
            for line in turn_summary.split('\n'):
                time.sleep(.25)
                print(line)
            print(f"{'-'*cols}")
            
            user_input = input(f">>> ")
            
            turn_summary = ""

            if user_input.lower() == 'q':
                break

            if user_input.lower() == 'a':
                # player turn
                turn_summary += "Hero Attacked!"
                pturn_stat, pturn_result = self.player.deal_dmg(self.enemy.res)
                self.enemy.take_dmg(self.player.atk)

                turn_summary += f"\n{pturn_result}\n\n"

            if user_input.lower() == 'b':
                items = {
                    'medicinal herb': {
                        'id': 1,
                        'name': 'medicinal herb',
                        'type': 'heal',
                        'amount': 15,
                        'reuse': False
                    },
                    'small potion': {
                        'id': 2,
                        'name': 'small potion',
                        'type': 'heal',
                        'amount': 10,
                        'reuse': False
                    },
                    "medium potion": {
                        'id': 3,
                        'name': 'medium potion',
                        'type': 'heal',
                        'amount': 20,
                        'reuse': False
                    },
                    'large potion': {
                        'id': 4,
                        'name': 'large potion',
                        'type': 'heal',
                        'amount': 30,
                        'reuse': False
                    },
                    'escape rope': {
                        'id': 5,
                        'name': 'escape rope',
                        'type': 'utility',
                        'reuse': False
                    }
                }
                # player turn
                sample_bag = {
                    'atk boost': 1,
                    'hp boost': 1,
                    'medicinal herb': 2,
                    'small potion': 3,
                    'medium potion': 1,
                    'large potion': 1,
                    'escape rope': 1,
                }
                clear_screen()
                print("Bag:\n")
                for k, v in sample_bag.items():
                    print(f" [{v}] {k}")
                bag_input = input("\nChoose item: ")
                # Check input

                chosen_item = items[bag_input]

                if chosen_item['type'] == 'heal':
                    heal_stat, heal_result = self.player.heal(chosen_item['amount'])
                    
                    turn_summary += f"{heal_result}\n\n"
                else:
                    turn_summary += f"{chosen_item['name']} used!\n"
                
                sample_bag[bag_input] -= 1
                if sample_bag[bag_input] <= 0:
                    del sample_bag[bag_input]
                time.sleep(1)

            if not self.enemy.is_alive:
                print("Hero won")
                break

            if not self.player.is_alive:
                print("You have been DEFEATED.")
                break

            if not enemy_first:
                # Enemy Turn
                turn_summary += "Enemy Attacked!"
                pturn_stat, pturn_result = self.player.take_dmg(self.enemy.atk)

                turn_summary += f"\n{pturn_result}"
            
                if not self.enemy.is_alive:
                    print("Hero won")
                    break

                if not self.player.is_alive:
                    print("You have been DEFEATED.")
                    break


def main():
    # Hp Bar Test
    # my_hp = buildHPBar(13, 20)
    # print(my_hp)

    # Box Test
    # name = "Pikachu"
    # bar = "########***"
    # inner_text = [
    #     f" {name:13} ",
    #     f" {bar:13} "
    # ]
    
    # new_box = box(inner_text)
    # print(new_box)

    # style1 = box(inner_text, 'regular', 'right')
    # style2 = box(inner_text, 'bold')
    # print(style1)
    # print(style2)

    new_player = Player("hercules")
    new_enemy = Enemy()

    battle = Battle(new_player, new_enemy)
    try:
        battle.run()
    except KeyboardInterrupt:
        print("\n[Quit Program]\n")
    

if __name__ == "__main__":
    main()
