import os

import re
import time

import pyautogui
import logging

from dependancies.smtptext import *

"""
Program: League Client Handler
Author: rickyg3 - and whoever wrote all these modules im using
Date: 04/21/21
"""


class LolHandler:
    # BUTTONS
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

    def __init__(self, input_gamemode='summoners_rift', priority_timer=0):
        self.gamemode = input_gamemode
        self.gamemodes = ['aram', 'summoners_rift', 'one_for_all']
        self.low_priority_timer = priority_timer
        self.notifier = TextNotifier()

        ''' Logging '''
        logging.basicConfig(filename='lol.log', level=logging.DEBUG, filemode='w')

    def __str__(self):
        text = f"[{self.gamemode}] [{self.low_priority_timer} min]"
        return text

    def set_timer(self, new_timer):
        self.low_priority_timer = new_timer

    def set_gamemode(self, gamemode_type='aram'):
        # maybe use regex for a match?
        if gamemode_type.lower() in self.gamemodes:
            self.gamemode = gamemode_type.lower()
        else:
            print("Invalid Gamemode type")

    def monitor_mode(self):
        """
        Loop that takes a screenshot of a certain portion of the screen
        or
        just checks a certain region for certain commands
        """
        # find_trigger('send_it.png')
        self.find_notification_trigger(self.SEND)

    def start_up(self):
        """
        Handles launching, signing in, and queueing up
        """
        # Open League client
        pyautogui.hotkey('win', 'd')
        pyautogui.press('win')
        time.sleep(0.1)
        pyautogui.write('lol', interval=0.15)  # type with quarter-second pause in between each key
        pyautogui.press('enter')
        # time.sleep(100)

        self.find_play_trigger(self.PLAY)

        # Get into a game
        print("")
        self.play_button()
        print("")
        time.sleep(1)

        # Select Game mode
        if self.gamemode == 'aram':
            self.find_button_click(self.ARAM, repeat=True)
        elif self.gamemode == 'summoner':
            self.find_button_click(self.SUM_RIFT, repeat=True)
        print("")
        time.sleep(0.5)

        self.confirm_button()
        print("")
        time.sleep(0.9)

        # Find match
        self.find_match_button()
        # even if it doesnt find it we can click
        # pyautogui.click()
        # CHEATING
        print("")
        # find_button_click('decline.png', loop_var=True)

        # For when you're in low priority queue
        if self.low_priority_timer > 0:
            time.sleep(self.low_priority_timer * 60)
            self.notifier.send(f"Timer Done! \nWaited: {self.low_priority_timer} min.")

        # accept match
        self.accept_button()
        self.notifier.send(f"\n[{self.gamemode}] Match is ready!")
        # in case it pops up again
        if self.find_trigger(self.ACCEPT, slow=0.5, timer=30):
            self.notifier.send(f"\n[Failed] Trying Again")
            self.accept_button()
            self.notifier.send(f"\n[{self.gamemode}] Match is ready!")
        os.system("exit")

    def after_match(self):
        """
        Handles going through the menu after a match
        """
        # after a match is over
        self.play_again_button()
        print("")
        time.sleep(0.9)

        self.find_match_button()
        print("")
        # find_button_click('decline.png', loop_var=True)

        # For when you're in low priority queue
        if self.low_priority_timer > 0:
            time.sleep(self.low_priority_timer*60)
            self.notifier.send(f"Timer Done! \nWaited: {self.low_priority_timer} min.")

        # accept match
        self.accept_button()
        self.notifier.send(f"\n[{self.gamemode}] Match is ready!")

        # in case it pops up again
        if self.find_trigger(self.ACCEPT, slow=0.5, timer=15):
            self.notifier.send(f"\n[Failed] Trying Again")
            self.accept_button()
            self.notifier.send(f"\n[{self.gamemode}] Match is ready!")

    def accept_button(self):
        image_file = self.ACCEPT

        base_name, ext = image_file.split(".")
        base_name = base_name.split('\\')
        base_name = base_name[1]
        print(f"[{base_name.title()}]")

        left = 1550
        top = 1200
        width = 900
        height = 450

        region = (left, top, width, height)

        counter = 1

        while True:
            button = pyautogui.locateCenterOnScreen(image_file, region=region, confidence=0.7)
            if button:
                # # Screenshot
                # pyautogui.screenshot('accept_search.png', region=region)
                pyautogui.moveTo(button)
                print("\nmoved")
                pyautogui.click(button)
                print("clicked")

                print("\nsuccess!")
                return True

            else:
                print(f"\rfailed: {counter}", end='')
                counter += 1

    def confirm_button(self):
        image_file = self.CONFIRM

        base_name, ext = image_file.split(".")
        base_name = base_name.split('\\')
        base_name = base_name[1]
        print(f"[{base_name.title()}]")

        left = 1285
        top = 1560
        width = 750
        height = 280

        region = (left, top, width, height)

        counter = 1

        while True:
            button = pyautogui.locateCenterOnScreen(image_file, region=region, confidence=0.7)
            if button:
                # # Screenshot
                # pyautogui.screenshot('confirm_search.png', region=region)
                pyautogui.moveTo(button)
                print("\nmoved")
                pyautogui.click(button)
                print("clicked")

                print("\nsuccess!")
                return True

            else:
                print(f"\rfailed: {counter}", end='')
                counter += 1
                return False
            # time.sleep(0.1)

    def decline_button(self):
        image_file = self.DECLINE

        base_name, ext = image_file.split(".")
        base_name = base_name.split('\\')
        base_name = base_name[1]
        print(f"[{base_name.title()}]")

        top = 1450
        left = 1700
        width = 400
        height = 200

        region = (left, top, width, height)

        counter = 1

        while True:
            button = pyautogui.locateCenterOnScreen(image_file, confidence=0.7)
            if button:
                # # Screenshot
                # pyautogui.screenshot('decline_search.png', region=region)
                pyautogui.moveTo(button)
                print("\nmoved")
                pyautogui.click(button)
                print("clicked")

                print("\nsuccess!")
                return True

            else:
                print(f"\rfailed: {counter}", end='')
                counter += 1
                return False
            # time.sleep(0.1)

    def find_match_button(self):
        image_file = self.FIND_MATCH

        base_name, ext = image_file.split(".")
        base_name = base_name.split('\\')
        base_name = base_name[1]
        print(f"[{base_name.title()}]")

        left = 1285
        top = 1560
        width = 750
        height = 280

        region = (left, top, width, height)

        counter = 1
        while True:
            button = pyautogui.locateCenterOnScreen(image_file, region=region, confidence=0.7)
            if button:
                # # Screenshot
                # pyautogui.screenshot('find_match_search.png', region=region)
                pyautogui.moveTo(button)
                print("\nmoved")
                pyautogui.click(button)
                print("clicked")

                print("\nsuccess!")
                return True

            else:
                print(f"\rfailed: {counter}", end='')
                counter += 1
                if counter > 4:
                    return False
            # time.sleep(0.1)

    def play_button(self):
        image_file = self.PLAY
        base_name, ext = image_file.split(".")
        base_name = base_name.split('\\')
        base_name = base_name[1]
        print(f"[{base_name.title()}]")

        left = 730
        top = 280
        width = 650
        height = 350

        region = (left, top, width, height)

        counter = 1

        while True:
            button = pyautogui.locateCenterOnScreen(image_file, region=region, confidence=0.7)
            if button:
                # # Screenshot
                # pyautogui.screenshot('play_search.png', region=region)
                pyautogui.moveTo(button)
                print("\nmoved")
                pyautogui.click(button)
                print("clicked")

                print("\nsuccess!")
                return True

            else:
                print(f"\rfailed: {counter}", end='')
                counter += 1
                return False
            # time.sleep(0.1)

    def play_again_button(self):
        image_file = self.PLAY_AGAIN

        base_name, ext = image_file.split(".")
        base_name = base_name.split('\\')
        base_name = base_name[1]
        print(f"[{base_name.title()}]")

        left = 1280
        top = 1550
        width = 700
        height = 300

        region = (left, top, width, height)

        counter = 1

        while True:
            button = pyautogui.locateCenterOnScreen(image_file, confidence=0.7)
            if button:
                # # Screenshot
                # pyautogui.screenshot('play_again_search.png', region=region)
                pyautogui.moveTo(button)
                print("\nmoved")
                pyautogui.click(button)
                print("clicked")

                print("\nsuccess!")
                return True

            else:
                print(f"\rfailed: {counter}", end='')
                counter += 1
                return False
            # time.sleep(0.1)

    def find_notification_trigger(self, image_file):
        base_name, ext = image_file.split(".")
        base_name = base_name.split('\\')
        base_name = base_name[1]
        print(f"[{base_name.title()}]")

        left = 2800
        top = 1400
        width = 1100
        height = 900

        region = (left, top, width, height)

        counter = 1
        move_x = 100
        while True:
            button = pyautogui.locateCenterOnScreen(image_file)  # , confidence=0.9
            if counter % 100 == 0:
                move_x *= -1
                pyautogui.dragTo(1000 - move_x, 1000)
            if button:
                # # Screenshot
                # pyautogui.screenshot('notif_search.png', region=region)
                print("\nTrigger Found!")
                logging.info(f"Trigger Found [{base_name.title()}]")
                logging.error(f"[{base_name.title()}] failed: {counter - 1} times")
                return True

            else:
                print(f"\rfailed: {counter}", end='')
                counter += 1
            # time.sleep(0.1)

    def find_play_trigger(self, image_file):
        base_name, ext = image_file.split(".")
        base_name = base_name.split('\\')
        base_name = base_name[1]
        print(f"[{base_name.title()}]")

        left = 730
        top = 280
        width = 650
        height = 350

        region = (left, top, width, height)

        counter = 1

        while True:
            button = pyautogui.locateCenterOnScreen(image_file, region=region, confidence=0.9)  # , confidence=0.9
            if counter == 100:
                time.sleep(260)
            if button:
                # # Screenshot
                # pyautogui.screenshot('play_trigger_search.png')
                print("\nTrigger Found!")
                logging.info(f"Trigger Found [{base_name.title()}]")
                logging.error(f"[{base_name.title()}] failed: {counter - 1} times")
                return True

            else:
                print(f"\rfailed: {counter}", end='')
                counter += 1
            time.sleep(0.6)

    def find_trigger(self, image_file, slow=0.0, timer=1000):
        base_name, ext = image_file.split(".")
        base_name = base_name.split('\\')
        base_name = base_name[1]
        print(f"[{base_name.title()}]")

        top = 1400
        left = 1000
        width = 800
        height = 400

        region = (left, top, width, height)

        counter = 1

        while True:
            if counter > timer:
                break
            button = pyautogui.locateCenterOnScreen(image_file, region=region, confidence=0.9)  # , confidence=0.9
            if button:
                # # Screenshot
                # pyautogui.screenshot('find_trigger_search.png', region=region)
                print("\nTrigger Found!")
                logging.info(f"Trigger Found [{base_name.title()}]")
                logging.error(f"[{base_name.title()}] failed: {counter - 1} times")
                return True

            else:
                print(f"\rfailed: {counter}", end='')
                counter += 1

            if slow > 0:
                time.sleep(slow)

    def find_button_click(self, image_file, repeat=False):
        base_name, ext = image_file.split(".")
        base_name = base_name.split('\\')
        base_name = base_name[1]
        print(f"[{base_name.title()}]")

        counter = 1
        run = True
        while run:
            button = pyautogui.locateCenterOnScreen(image_file, confidence=0.7)
            if button:
                # # Screenshot
                # pyautogui.screenshot('button_search.png')
                pyautogui.moveTo(button)
                print("\nmove")
                pyautogui.click(button)
                print("click")

                print("\nsuccess!")
                return True

            else:
                print(f"\rfailed: {counter}", end='')
                counter += 1
                if not repeat:
                    run = False


if __name__ == "__main__":
    # Initialize Client Handler instance
    client_handler = LolHandler()

    raw_input = pyautogui.prompt("Select your settings: \n{ start, monitor, after} "
                                 "{aram, summoners rift, one for all} {Queue Timer}", "Setting")
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

        # try:
        #     gamemode = start[2]
        #     print(gamemode)
        # except IndexError:
        #     pass
        # try:
        #     timer = start[3]
        #     print(timer)
        # except IndexError:
        #     pass

    print('*', config)

    if config == 'start':
        # mode = pyautogui.prompt("Select a Gamemode:", "Gamemode")
        # timer = pyautogui.prompt("How long is your Queue timer?:", "Timer")
        client_handler.set_gamemode(gamemode)
        print(timer)
        client_handler.set_timer(float(timer))

        print(client_handler)
        client_handler.start_up()

    elif config == 'monitor':
        # mode = pyautogui.prompt("Select a Gamemode:", "Gamemode")
        # timer = pyautogui.prompt("How long is your Queue timer?:", "Timer")
        client_handler.set_gamemode(gamemode)
        client_handler.set_timer(float(timer))

        print(client_handler)
        client_handler.monitor_mode()
        client_handler.start_up()

    elif config == 'after':
        # change_mode = pyautogui.confirm(text='Change Gamemode?', title='Change Gamemode', buttons=['yes', 'no'])
        # new_mode = pyautogui.prompt("Gamemode:", "Change Gamemode")
        client_handler.set_gamemode(gamemode)
        client_handler.set_timer(float(timer))
        client_handler.after_match()
    else:
        print("Invalid Setting")
