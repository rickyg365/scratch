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

# class LolButtons:
#
#     def __init__(self):
#         self.raw_button_data = {
#             'buttons\\play.png': (730, 280, 650, 350),
#             'buttons\\play_again.png': (1280, 1550, 700, 300),
#             'buttons\\find_match.png': (1285, 1560, 750, 280),
#             'buttons\\confirm.png': (1285, 1560, 750, 280),
#             'buttons\\accept.png': (1550, 1200, 900, 450),
#             'buttons\\decline.png': (0, 0, 3900, 2300),
#         }
#         self.buttons = self.process_raw_data(self.raw_button_data)
#
#         self.raw_trigger_data = {
#             'buttons\\specific.png': (730, 280, 650, 350)
#         }
#         self.triggers = self.process_raw_data(self.raw_trigger_data)
#
#         self.raw_gamemode_data = {
#             'buttons\\aram.png': (0, 0, 3900, 2300),
#             'buttons\\summoners_rift.png': (0, 0, 3900, 2300),
#             'buttons\\one_for_all.png': (0, 0, 3900, 2300)
#         }
#         self.gamemodes = self.process_raw_data(self.raw_gamemode_data)
#
#     def process_raw_data(self, raw_data):
#         output_dict = {}
#         for image_path, region in raw_data.items():
#             base_name, ext = image_path.split(".")
#             base_name = base_name.split('\\')
#             item_name = base_name[1]
#             output_dict[item_name] = SearchObject(image_path, item_name, region)
#
#         return output_dict
#
#     # client_objects = LolButtons()
#     # # Buttons
#     # play_button = client_objects.buttons['play']
#     # accept_button = client_objects.buttons['accept']
#     # confirm_button = client_objects.buttons['confirm']
#     # find_match_button = client_objects.buttons['find_match']
#     #
#     # # Gamemodes
#     # aram_button = client_objects.gamemodes['aram']
#     # sum_rift_button = client_objects.gamemodes['summoners_rift']
#     # one_for_all_button = client_objects.gamemodes['one_for_all']
#     #
#     # # Triggers
#     # queue_up = client_objects.triggers['specific']


class LolHandler:
    '''
            play_button = SearchObject('buttons\\play.png', 'play', (730, 280, 650, 350))
            play_again_button = SearchObject('buttons\\play_again.png', 'play_again', (1280, 1550, 700, 300))
            find_match_button = SearchObject('buttons\\find_match.png', 'find_match', (1285, 1560, 750, 280))
            confirm_button = SearchObject('buttons\\confirm.png', 'confirm', (1285, 1560, 750, 280))
            accept_button = SearchObject('buttons\\accept.png', 'accept', (1550, 1200, 900, 450))
            decline_button = SearchObject('buttons\\decline.png', 'decline', (0, 0, 3900, 2300))
            queue_up = SearchObject('buttons\\specific.png', 'specific', (730, 280, 650, 350)
            aram_button = SearchObject('buttons\\aram.png', 'aram', (0, 0, 3900, 2300))
            sum_rift_button = SearchObject('buttons\\summoners_rift.png', 'summoners_rift', (0, 0, 3900, 2300))
            one_for_all_button = SearchObject('buttons\\one_for_all.png', 'one_for_all', (0, 0, 3900, 2300))

    '''

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
        # self.client_objects = LolButtons()

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

    def open_client(self):
        # Open League client
        pyautogui.hotkey('win', 'd')
        time.sleep(0.1)
        pyautogui.press('win')
        time.sleep(0.1)
        pyautogui.write('lol', interval=0.15)  # type with quarter-second pause in between each key
        pyautogui.press('enter')
        # time.sleep(100)

    def lock_in_gamemode(self):
        # Select Game mode
        self.current_gamemode.move_click()
        print("")
        time.sleep(0.5)

        self.confirm_button.move_click()
        print("")
        time.sleep(0.9)

        # Find match
        self.find_match_button.move_click()
        print("")

    def accept_match(self):
        self.accept_button.move_click(max_loops=1000)
        self.notifier.send(f"\n[{self.gamemode.upper()}] Match is ready!")
        # in case it pops up again
        accept_again, accept_location = self.accept_button.locate_button(repeat=True, slow=0.3, max_loops=35)
        if accept_again:
            self.notifier.send(f"\n[Failed] Trying Again")
            pyautogui.moveTo(accept_location)
            self.notifier.send(f"[{self.gamemode}] Match is ready!")

    def monitor_mode(self):
        """
        Loop that takes a screenshot of a certain portion of the screen
        or
        just checks a certain region for certain commands
        """

        self.queue_up.locate_button(repeat=True, slow=2.2, max_loops=2000)

    # def start_up(self):
    #     """
    #     Handles launching, signing in, and queueing up
    #     """
    #     # Open League client
    #     self.open_client()
    #
    #     # Searches for play button trigger
    #     self.play_button.locate_button(repeat=True, slow=0.2)
    #
    #     # Get into a game
    #     # print("")
    #     self.play_button.move_click()
    #     # print("")
    #     time.sleep(1)
    #
    #     # Select Game mode
    #     self.lock_in_gamemode()
    #
    #     # find_button_click('decline.png', loop_var=True)
    #
    #     # For when you're in low priority queue
    #     if self.low_priority_timer > 0.0:
    #         time.sleep(self.low_priority_timer*60)
    #         self.notifier.send(f"Timer Done! \nWaited: {self.low_priority_timer} min.")
    #
    #     # accept match
    #     self.accept_match()
        # self.accept_button.move_click(max_loops=100)
        # self.notifier.send(f"\n[{self.gamemode.upper()}] Match is ready!")
        # # in case it pops up again
        # if self.accept_button.locate_button(repeat=True, slow=0.5, max_loops=30):
        #     self.notifier.send(f"\n[Failed] Trying Again")
        #     self.accept_button.move_click()
        #     self.notifier.send(f"[{self.gamemode}] Match is ready!")

    def after_match(self):
        """
        Handles going through the menu after a match
        """
        # after a match is over
        self.play_again_button.move_click()
        print("")
        time.sleep(0.9)

        self.find_match_button.move_click()
        print("")
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
                                 "\n    Config:    \t Gamemode: "
                                 "\n    |1 start:  \t | 1 summoners "
                                 "\n    |2 monitor \t | 2 aram "
                                 "\n    |3 after   \t | 3 one for all "
                                 "\n \nInput:  [CONFIG] [GAME_MODE] [QUEUE_TIMER]", "Setting")
    # # Regex would be waaaay better for parsing
    # start_pattern = re.compile(r'(start|monitor) (aram|summoners rift|one for all)? (\d*\.?\d*)?')
    # after_pattern = re.compile(r'(after) (t|f)? (\d*\.?\d*)?')
    #
    # # Defaults
    # config = ""
    # gamemode = 'aram'
    # timer = 0.0
    # change_mode = 'f'
    #
    # start = re.search(start_pattern, raw_input)
    # if start:
    #     # print(start)
    #     # print(f"config: {start[1]}")
    #     # print(f"gamemode: {start[2]}")
    #     # print(f"timer: {start[3]}")
    #
    #     config = start[1]
    #     print(config)
    #     # gamemode = start[2]
    #     # timer = start[3]
    #     try:
    #         gamemode = start[2]
    #     except IndexError:
    #         pass
    #     try:
    #         timer = start[3]
    #     except IndexError:
    #         pass
    #
    # after = re.search(after_pattern, raw_input)
    # if after:
    #     # print(after)
    #     # print(f"config: {after[1]}")
    #     # print(f"timer: {after[2]}")
    #     config = after[1]
    #     print(config)
    #     try:
    #         change_mode = after[2]
    #     except IndexError:
    #         pass
    #     try:
    #         timer = after[3]
    #     except IndexError:
    #         pass

    master_pattern = re.compile(r'(start|monitor|after) ?(aram|summoners rift|one for all)? ?(\d+\.?\d*)?')
    # Defaults
    config = ""
    gamemode = 'aram'
    timer = 0.0

    start = re.search(master_pattern, raw_input)
    if start:
        # print(start)
        # print(f"config: {start[1]}")
        # print(f"gamemode: {start[2]}")
        # print(f"timer: {start[3]}")

        config = start[1]
        print(config)
        gamemode = start[2]
        timer = start[3]
        if gamemode is None:
            gamemode = 'aram'
        if timer is None:
            timer = '0.0'

    print('*', config)

    if config == 'start':
        # set game mode and timer
        client_handler.set_gamemode(gamemode)
        client_handler.set_timer(float(timer))

        print(client_handler)

        # Open League client
        client_handler.open_client()

        # Searches for play button trigger
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

    elif config == 'monitor':

        client_handler.set_gamemode(gamemode)
        client_handler.set_timer(float(timer))

        print(client_handler)
        client_handler.monitor_mode()

        # Open League client
        client_handler.open_client()

        # Searches for play button trigger
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

    elif config == 'after':
        client_handler.set_gamemode(gamemode)
        client_handler.set_timer(float(timer))
        client_handler.after_match()
    else:
        print("Invalid Setting")


#
# if __name__ == "__main__":
#     # Initialize Client Handler instance
#     client_handler = LolHandler()
#
#     setting = pyautogui.prompt("Select a setting \n- start\n- monitor\n- after", "Setting")
#
#     if setting == 'start':
#         mode = pyautogui.prompt("Select a Gamemode:", "Gamemode")
#         client_handler.set_gamemode(mode)
#
#         print(client_handler)
#         # Open League client
#         client_handler.open_client()
#
#         # Searches for play button trigger
#         client_handler.play_button.locate_button(repeat=True, slow=0.2)
#         client_handler.play_button.move_click()
#
#         time.sleep(1)
#
#         # Select Game mode
#         client_handler.lock_in_gamemode()
#
#         # find_button_click('decline.png', loop_var=True)
#
#         # For when you're in low priority queue
#         if client_handler.low_priority_timer > 0.0:
#             time.sleep(client_handler.low_priority_timer * 60)
#             client_handler.notifier.send(f"Timer Done! \nWaited: {client_handler.low_priority_timer} min.")
#
#         # accept match
#         client_handler.accept_match()
#
#     elif setting == 'monitor':
#         mode = pyautogui.prompt("Select a Gamemode:", "Gamemode")
#         # timer = pyautogui.prompt("How long is your Queue timer?:", "Timer")
#         client_handler.set_gamemode(mode)
#         # client_handler.set_timer(timer)
#
#         print(client_handler)
#         client_handler.monitor_mode()
#         client_handler.start_up()
#
#     elif setting == 'after':
#         change_mode = pyautogui.confirm(text='Change Gamemode?', title='Change Gamemode', buttons=['yes', 'no'])
#         if change_mode == 'ok':
#             new_mode = pyautogui.prompt("Gamemode:", "Change Gamemode")
#             client_handler.set_gamemode(new_mode)
#         client_handler.after_match()
#     else:
#         print("Invalid Setting")
