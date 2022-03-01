import os
import sys
import time

from player import Player, Enemy
from utility import clear_screen
from items import Item, HealItem, Bag

'''


'''
# items = {
#     'medicinal herb': {
#         'id': 1,
#         'name': 'medicinal herb',
#         'type': 'heal',
#         'amount': 15,
#         'reuse': False
#     },
#     'small potion': {
#         'id': 2,
#         'name': 'small potion',
#         'type': 'heal',
#         'amount': 10,
#         'reuse': False
#     },
#     "medium potion": {
#         'id': 3,
#         'name': 'medium potion',
#         'type': 'heal',
#         'amount': 20,
#         'reuse': False
#     },
#     'large potion': {
#         'id': 4,
#         'name': 'large potion',
#         'type': 'heal',
#         'amount': 30,
#         'reuse': False
#     },
#     'escape rope': {
#         'id': 5,
#         'name': 'escape rope',
#         'type': 'utility',
#         'reuse': False
#     }
# }
items = {
    'medicinal herb': HealItem(1, 'medicinal herb', False, 15),
    'small potion': HealItem(2, 'small potion', False, 10),
    "medium potion": HealItem(3, 'medium potion', False, 20),
    'large potion': HealItem(4, 'large potion', False, 30),
    'escape rope': Item(5, 'escape rope', 'utility', False)
}

class Battle:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def __str__(self) -> str:
        txt = ""
        return txt

    def run(self):
        cols, rows = os.get_terminal_size()

        enemy_first = False

        if self.player.spd < self.enemy.spd:
            enemy_first = True

        turn_summary = f"""[a] Attack Enemy
[b] Bag / Inventory"""
        while True:
            if enemy_first:
                # Enemy Turn
                turn_summary += "Enemy Attacked:"
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
            
            # Display Current Status
            clear_screen()
            print(self.enemy)
            print(self.player)
            print(f"{'-'*cols}")
            # print(turn_summary)
            for line in turn_summary.split('\n'):
                time.sleep(.25)
                print(line)
            print(f"{'-'*cols}")
            
            # Wait for user input
            user_input = input(f">>> ")
            
            # reset turn summary
            turn_summary = ""

            # Exit condition
            if user_input.lower() == 'q':
                break
            
            # Attack condition
            if user_input.lower() == 'a':
                # player turn
                turn_summary += "You Attack!"
                pturn_stat, pturn_result = self.player.deal_dmg(self.enemy.res)
                self.enemy.take_dmg(self.player.atk)

                turn_summary += f"\n{pturn_result}\n\n"

            # Bag Condition
            if user_input.lower() == 'b':

                # Display Bag
                clear_screen()
                print(self.player.bag)
                bag_input = input("\nChoose item: ")
                # Check input
                
                chosen_item = items[bag_input]

                # Use Item
                use_status, use_result = self.player.bag.use_item(bag_input)

                if use_status:
                    turn_summary += f"{use_result}\n"
                    use_stat, use_result = chosen_item.use(self.player)

                    turn_summary += f"{use_result}\n\n"
                else:
                    turn_summary += f"{use_result}\n"

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
    sample_bag = {
        'atk boost': 1,
        'hp boost': 1,
        'medicinal herb': 2,
        'small potion': 3,
        'medium potion': 1,
        'large potion': 1,
        'escape rope': 1,
    }
    new_player = Player("hercules", prebuilt_bag=sample_bag)
    new_enemy = Enemy()

    battle = Battle(new_player, new_enemy)
    try:
        battle.run()
    except KeyboardInterrupt:
        print("\n[Quit Program]\n")
    

if __name__ == "__main__":
    main()
