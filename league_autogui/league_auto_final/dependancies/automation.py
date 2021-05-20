import os

import time

import pyautogui
import logging

"""

"""

'''
# FUNCTIONS
def find_notification_trigger(image_file):
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
            pyautogui.moveTo(1000 - move_x, 1000)
            time.sleep(90)
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


def find_play_trigger(image_file):
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


def find_trigger(image_file, region=(0, 0, 0, 0), screenshot=False, slow=0.0, timer=1000):
    base_name, ext = image_file.split(".")
    base_name = base_name.split('\\')
    base_name = base_name[1]
    print(f"[{base_name.title()}]")

    # # Screenshot
    if screenshot:
        if region == (0, 0, 0, 0):
            pyautogui.screenshot(f"{base_name}_screenshot.png")
        else:
            pyautogui.screenshot(f"{base_name}_screenshot.png", region)

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


def find_button_click(image_file, region=(0, 0, 0, 0), screenshot=False, repeat=False):
    base_name, ext = image_file.split(".")
    base_name = base_name.split('\\')
    base_name = base_name[1]
    print(f"[{base_name.title()}]")

    # # Screenshot
    if screenshot:
        if region == (0, 0, 0, 0):
            pyautogui.screenshot(f"{base_name}_screenshot.png")
        else:
            pyautogui.screenshot(f"{base_name}_screenshot.png", region)

    counter = 1

    while True:
        if region == (0, 0, 0, 0):
            button = pyautogui.locateCenterOnScreen(image_file, confidence=0.7)
        else:
            button = pyautogui.locateCenterOnScreen(image_file, region, confidence=0.7)

        if button:
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
                return False
'''


class SearchObject:
    def __init__(self, image_file, base_name, region=(0, 0, 3900, 2200)):
        self.raw_image = image_file
        # self.base_image = self.process(image_file)
        self.base_image = base_name
        # set region to whole screen by default
        self.region = region
        # self.screenshot = screenshot
        # self.confidence = confide
        # self.repeat = repeat
        # # Delay between searching for locate button
        # self.slow = slow
        # # Max number of iterations in locate button loop
        # self.max_loop = max_loops

    def set_region(self, left, top, width, height):
        self.region = (left, top, width, height)

    # def process(self, file_name):
    #     base_name, ext = file_name.split(".")
    #     base_name = base_name.split('\\')
    #     base_name = base_name[1]
    #
    #     return f"[{base_name.title()}]"

    def locate_button(self, confide=0.7, slow=0.0, max_loops=500,  take_screenshot=False, repeat=False):
        print(f"[{self.base_image.title()}]")
        counter = 1

        while True:
            if counter > max_loops:
                break

            button = pyautogui.locateCenterOnScreen(self.raw_image, region=self.region, confidence=confide)

            if button:
                if take_screenshot:
                    pyautogui.screenshot(f"{self.base_image}_screenshot.png", self.region)
                print("\nsuccess!")
                return True, button

            else:
                print(f"\rfailed: {counter}", end='')
                counter += 1
                if not repeat:
                    return False, (0, 0)
            if slow > 0.0:
                time.sleep(slow)

# Redo this the moveclick should not depend on the locate button they should work independently even if I have to call the locate button before the move_click
    def move_click(self, max_loops=3, slow_amount=0.0):
        found, button_to_click = self.locate_button(repeat=True, slow=slow_amount, max_loops=max_loops)
        if found:
            pyautogui.moveTo(button_to_click)

            pyautogui.click(button_to_click)
            return True
        else:
            print(f"[{self.base_image}]: Not Found.")
            return False

    # make this one into a decorator that can take a func after if found we could put our text function there
    def trigger_event(self):
        found, button_to_click = self.locate_button()
        if found:
            print("\nTrigger Found!")
            logging.info(f"Trigger Found [{self.base_image.title()}]")
            return True

        else:
            print(f"[{self.base_image}]: Not Found.")
            return False


if __name__ == "__main__":
    new_button = SearchObject('random_image.png', 'random_image', (0, 0, 400, 400))

    new_button.move_click()
    new_button.trigger_event()


