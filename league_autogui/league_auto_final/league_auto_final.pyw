import os
import sys

import re
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


class LolHandler:
    # Buttons
    play_button = SearchObject('buttons\\play.png', 'play', (730, 280, 650, 350))
    play_again_button = SearchObject('buttons\\play_again.png', 'play_again', (1280, 1550, 700, 300))
    find_match_button = SearchObject('buttons\\find_match.png', 'find_match', (1285, 1560, 750, 280))
    confirm_button = SearchObject('buttons\\confirm.png', 'confirm', (1285, 1560, 750, 280))
    accept_button = SearchObject('buttons\\accept.png', 'accept', (1550, 1200, 900, 450))
    decline_button = SearchObject('buttons\\decline.png', 'decline', (0, 0, 3900, 2300))

    # Triggers
    queue_up = SearchObject('buttons\\specific.png', 'specific', (2800, 1400, 1100, 900))

    # Game Modes
    aram_button = SearchObject('buttons\\aram.png', 'aram', (0, 0, 3900, 2300))
    sum_rift_button = SearchObject('buttons\\summoners_rift.png', 'summoners_rift', (0, 0, 3900, 2300))
    one_for_all_button = SearchObject('buttons\\one_for_all.png', 'one_for_all', (0, 0, 3900, 2300))

    def __init__(self, input_gamemode='aram', priority_timer=0):
        self.gamemode = input_gamemode
        self.current_gamemode = self.aram_button
        self.valid_gamemodes = ['aram', 'summoners', 'one']

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
        # Checks for valid game mode type
        if gamemode_type.lower() in self.valid_gamemodes:
            self.gamemode = gamemode_type.lower()
            # Assign current gamemode variable to the correct gamemode button
            if self.gamemode == 'aram':
                self.current_gamemode = self.aram_button
            elif self.gamemode == 'summoners':
                self.current_gamemode = self.sum_rift_button
            elif self.gamemode == 'one':
                self.current_gamemode = self.one_for_all_button
        else:
            print(f"Invalid gamemode [{gamemode_type}]")

    # Maybe this one should be handled outside or just be optional
    def open_client(self):
        # Open League client
        pyautogui.hotkey('win', 'd')
        time.sleep(0.1)
        pyautogui.press('win')
        time.sleep(0.2)
        pyautogui.write('lol', interval=0.25)  # type with quarter-second pause in between each key
        pyautogui.press('enter')

    #
    def lock_in_gamemode(self):
        # Select Game mode
        self.current_gamemode.move_click(max_loops=1000, slow_amount=0.1)
        time.sleep(0.6)

        self.confirm_button.move_click()
        time.sleep(0.9)

        # Find match
        self.find_match_button.move_click()

    def accept_match(self, max_loops=1000, slow_amount=0.0):
        self.accept_button.move_click(max_loops=max_loops, slow_amount=slow_amount)
        self.notifier.send(f"\n[{self.gamemode.upper()}] Match is ready!")
        # in case it pops up again
        # accept_again, accept_location = self.accept_button.locate_button(repeat=True, slow=0.3, max_loops=45)
        # if accept_again:
        #     self.notifier.send(f"\n[Failed] Trying Again")
        #     pyautogui.moveTo(accept_location)
        #     self.notifier.send(f"[{self.gamemode}] Match is ready!")
        # I think it might be easier to just call the function again with a different set of max loops

    def monitor_mode(self):
        """
        Loop that takes a screenshot of a certain portion of the screen
        or
        just checks a certain region for certain commands
        """

        self.queue_up.locate_button(repeat=True, slow=2.2, max_loops=2500)

    def after_match(self):
        """
        Handles going through the menu after a match
        """
        # after a match is over
        self.play_again_button.move_click()
        time.sleep(0.9)

        self.find_match_button.move_click()
        # find_button_click('decline.png', loop_var=True)

        # For when you're in low priority queue
        time.sleep(self.low_priority_timer*60)
        self.notifier.send(f"Timer Done! \nWaited: {self.low_priority_timer} min.")

        # accept match
        self.accept_button.move_click()
        self.notifier.send(f"\n[{self.gamemode}] Match is ready!")

        # in case it pops up again
        if self.accept_button.locate_button(repeat=True, slow=0.5, max_loops=25):
            self.notifier.send(f"\n[Failed] Trying Again")
            self.accept_button.move_click()
            self.notifier.send(f"[{self.gamemode}] Match is ready!")


if __name__ == "__main__":
    # Initialize Client Handler instance
    client_handler = LolHandler()

    raw_input = pyautogui.prompt("Select your settings: \n"
                                 "\n    Config: Start, monitor, after "
                                 "\n    Gamemode: summoners, aram, one for all: "
                                 "\n \nInput:  [CONFIG] [GAME_MODE] [QUEUE_TIMER]", "Setting")

    master_pattern = re.compile(r'(start|monitor|after) ?(aram|summoners rift|one for all)? ?(\d+\.?\d*)?')
    # Defaults
    # I think I can completely remove these, test later
    config = ""
    gamemode = 'aram'
    timer = 0.0

    start = re.search(master_pattern, raw_input)
    if start:
        config = start[1]
        gamemode = start[2]
        timer = start[3]
        if gamemode is None:
            gamemode = 'aram'
        if timer is None:
            timer = '0.0'

    if config == 'start':
        # set game mode and timer
        client_handler.set_gamemode(gamemode)
        client_handler.set_timer(float(timer))

        print(client_handler)

        # Open League client
        client_handler.open_client()

        # Searches for play button trigger
        time.sleep(0.5)
        client_handler.play_button.locate_button(repeat=True, slow=0.4)
        time.sleep(1)
        client_handler.play_button.move_click(max_loops=20)

        time.sleep(0.9)

        # Select Game mode
        client_handler.lock_in_gamemode()

        # For when you're in low priority queue
        if client_handler.low_priority_timer > 0.0:
            time.sleep(client_handler.low_priority_timer * 60)
            client_handler.notifier.send(f"Timer Done! \nWaited: {client_handler.low_priority_timer} min.")

        # accept match
        client_handler.accept_match()
        client_handler.accept_match(max_loops=100, slow_amount=0.5)

    elif config == 'monitor':

        client_handler.set_gamemode(gamemode)
        client_handler.set_timer(float(timer))

        print(client_handler)
        client_handler.monitor_mode()

        # Open League client
        client_handler.open_client()

        # Searches for play button trigger
        time.sleep(0.5)
        client_handler.play_button.locate_button(repeat=True, slow=0.2)
        client_handler.play_button.move_click()

        time.sleep(1)

        # Select Game mode
        client_handler.lock_in_gamemode()

        # For when you're in low priority queue
        if client_handler.low_priority_timer > 0.0:
            time.sleep(client_handler.low_priority_timer * 60)
            client_handler.notifier.send(f"Timer Done! \nWaited: {client_handler.low_priority_timer} min.")

        # accept match
        client_handler.accept_match()
        client_handler.accept_match(max_loops=100, slow_amount=0.5)

    elif config == 'after':
        client_handler.set_gamemode(gamemode)
        client_handler.set_timer(float(timer))
        client_handler.after_match()
    else:
        print("Invalid Setting")
