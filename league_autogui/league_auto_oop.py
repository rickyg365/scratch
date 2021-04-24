import os
import sys

import time

import pyautogui
import logging

from dependancies.smtptext import *
from dependancies.automation import *

'''
# BUTTON SOURCE
    PLAY = 'buttons\\play.png'
    PLAY_AGAIN = 'buttons\\play_again.png'
    FIND_MATCH = 'buttons\\find_match.png'
    CONFIRM = 'buttons\\confirm.png'
    ACCEPT = 'buttons\\accept.png'
    DECLINE = 'buttons\\decline.png'

    # GAMEMODES
    ARAM = 'buttons\\aram.png'
    SUM_RIFT = 'buttons\\summoners_rift_lit.png'
    ONE_4_ALL = 'buttons\\one_for_all.png'

    # Notification Triggers
    SEND = 'buttons\\specific.png'

'''


class LolAutomations:

    def __init__(self):
        self.raw_button_data = {
            'buttons\\play.png': (730, 280, 650, 350),
            'buttons\\play_again.png': (1280, 1550, 700, 300),
            'buttons\\find_match.png': (1285, 1560, 750, 280),
            'buttons\\confirm.png': (1285, 1560, 750, 280),
            'buttons\\accept.png': (1550, 1200, 900, 450),
            'buttons\\decline.png': (0, 0, 3900, 2300),
        }
        self.buttons = self.process_raw_data(self.raw_button_data)

        self.raw_trigger_data = {
            'buttons\\specific.png': (730, 280, 650, 350)
        }
        self.triggers = self.process_raw_data(self.raw_trigger_data)

        self.raw_gamemode_data = {
            'buttons\\aram.png': (0, 0, 3900, 2300),
            'buttons\\summoners_rift.png': (0, 0, 3900, 2300),
            'buttons\\one_for_all.png': (0, 0, 3900, 2300)
        }
        self.gamemodes = self.process_raw_data(self.raw_gamemode_data)

    def process_raw_data(self, raw_data):
        output_dict = {}
        for image_path, region in raw_data.items():
            base_name, ext = image_path.split(".")
            base_name = base_name.split('\\')
            item_name = base_name[1]
            output_dict[item_name] = SearchObject(image_path, region)

        return output_dict


class LolHandler:
    def __init__(self, input_gamemode='aram', priority_timer=0):
        self.gamemode = input_gamemode
        # self.gamemodes = ['aram', 'summoners_rift', 'one_for_all']

        self.auto = LolAutomations()

        self.low_priority_timer = priority_timer
        self.notifier = TextNotifier()

        ''' Logging '''
        logging.basicConfig(filename='lol.log', level=logging.DEBUG, filemode='w')

    def __str__(self):
        text = f"[{self.gamemode}] [{self.low_priority_timer} min]"
        return text

    def set_timer(self, new_timer):
        self.low_priority_timer = new_timer

    def set_gamemode(self, gamemode_type):
        if gamemode_type.replace(' ', '_') in self.auto.gamemodes.keys():
            self.gamemode = gamemode_type.lower()
        else:
            print("Invalid gamemode")

    def monitor_mode(self):
        """
        Loop that takes a screenshot of a certain portion of the screen
        or
        just checks a certain region for certain commands
        """
        # Variables
        queue_up = self.auto.triggers['specific']

        queue_up.locate_button(repeat=True)

    def start_up(self):
        """
        Handles launching, signing in, and queueing up
        """
        # Variables
        play_button = self.auto.buttons['play']
        accept_button = self.auto.buttons['accept']
        confirm_button = self.auto.buttons['confirm']
        find_match_button = self.auto.buttons['find_match']

        aram_button = self.auto.gamemodes['aram']
        sum_rift_button = self.auto.gamemodes['summoners_rift']
        one_for_all_button = self.auto.gamemodes['one_for_all']

        # Open League client
        pyautogui.hotkey('win', 'd')
        time.sleep(0.05)
        pyautogui.press('win')
        time.sleep(0.1)
        pyautogui.write('lol', interval=0.15)  # type with quarter-second pause in between each key
        pyautogui.press('enter')
        # time.sleep(100)

        play_button.locate_button(repeat=True, slow=0.1)
        # self.find_play_trigger(self.PLAY)

        # Get into a game
        print("")
        play_button.move_click()
        print("")
        time.sleep(1)

        # Select Game mode
        if self.gamemode == 'aram':
            aram_button.move_click()
        elif self.gamemode == 'summoner':
            sum_rift_button.move_click()
        print("")
        time.sleep(0.5)

        confirm_button.move_click()
        print("")
        time.sleep(0.9)

        # Find match
        find_match_button.move_click()

        print("")
        # find_button_click('decline.png', loop_var=True)

        # For when you're in low priority queue
        # time.sleep(self.low_priority_timer * 60)
        # self.notifier.send(f"Timer Done! \nWaited: {self.low_priority_timer} min.")

        # accept match
        accept_button.move_click(max_loops=100)
        self.notifier.send(f"\n[{self.gamemode.upper()}] Match is ready!")
        # in case it pops up again
        if accept_button.locate_button(repeat=True, slow=0.5, max_loops=30):
            self.notifier.send(f"\n[Failed] Trying Again")
            accept_button.move_click()
            self.notifier.send(f"[{self.gamemode}] Match is ready!")

    def after_match(self):
        """
        Handles going through the menu after a match
        """
        # Variables
        play_again_button = self.auto.buttons['play_again']
        accept_button = self.auto.buttons['accept']
        find_match_button = self.auto.buttons['find_match']

        aram_button = self.auto.gamemodes['aram']
        sum_rift_button = self.auto.gamemodes['summoners_rift']
        one_for_all_button = self.auto.gamemodes['one_for_all']

        # after a match is over
        play_again_button.move_click()
        print("")
        time.sleep(0.9)

        find_match_button.move_click()
        print("")
        # find_button_click('decline.png', loop_var=True)

        # For when you're in low priority queue
        time.sleep(self.low_priority_timer*60)
        self.notifier.send(f"Timer Done! \nWaited: {self.low_priority_timer} min.")

        # accept match
        accept_button.move_click()
        self.notifier.send(f"\n[{self.gamemode}] Match is ready!")

        # in case it pops up again
        if accept_button.locate_button(repeat=True, slow=0.5, max_loops=25):
            self.notifier.send(f"\n[Failed] Trying Again")
            accept_button.move_click()
            self.notifier.send(f"[{self.gamemode}] Match is ready!")


if __name__ == "__main__":
    # Initialize Client Handler instance
    client_handler = LolHandler()

    setting = pyautogui.prompt("Select a setting \n- start\n- monitor\n- after", "Setting")

    if setting == 'start':
        mode = pyautogui.prompt("Select a Gamemode:", "Gamemode")
        # timer = pyautogui.prompt("How long is your Queue timer?:", "Timer")
        client_handler.set_gamemode(mode)
        # client_handler.set_timer(timer)

        print(client_handler)
        client_handler.start_up()

    elif setting == 'monitor':
        mode = pyautogui.prompt("Select a Gamemode:", "Gamemode")
        # timer = pyautogui.prompt("How long is your Queue timer?:", "Timer")
        client_handler.set_gamemode(mode)
        # client_handler.set_timer(timer)

        print(client_handler)
        client_handler.monitor_mode()
        client_handler.start_up()

    elif setting == 'after':
        change_mode = pyautogui.confirm(text='Change Gamemode?', title='Change Gamemode', buttons=['yes', 'no'])
        if change_mode == 'ok':
            new_mode = pyautogui.prompt("Gamemode:", "Change Gamemode")
            client_handler.set_gamemode(new_mode)
        client_handler.after_match()
    else:
        print("Invalid Setting")
