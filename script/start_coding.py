import os
import sys

import time
import pyautogui

def wait_timer(wait_time_min):
    wait_time_sec = wait_time_min * 60
    time.sleep(wait_time_sec)


def find_button_click(image_file, repeat=False):
    base_name, ext = image_file.split(".")
    print(f"[{base_name.title()}]")
    # print(base_name, ext)
    counter = 1
    run = True
    while run:
        if base_name == 'accept':
            left = 1300
            top = 1200
            width = 900
            height = 500

            region = (left, top, width, height)
            button = pyautogui.locateCenterOnScreen(image_file, region=region, confidence=0.7)
        else:
            button = pyautogui.locateCenterOnScreen(image_file, confidence=0.7)
        if button:
            print("")
            pyautogui.moveTo(button)
            print("move")
            pyautogui.click(button)
            print("click")

            print("\nsuccess!")
            return True

        else:
            print(f"\rfailed: {counter}", end='')
            counter += 1
            if not repeat:
                # print("")
                run = False
        time.sleep(0.1)


def find_trigger(image_file):
    base_name, ext = image_file.split(".")
    print(f"[{base_name.title()}]")
    # print(base_name, ext)
    counter = 1
    run = True
    while run:
        left = 2800
        top = 1400
        width = 1100
        height = 900

        region = (left, top, width, height)
        button = pyautogui.locateCenterOnScreen(image_file)  # , confidence=0.9

        if button:
            print("\nTrigger Found!")
            return True

        else:
            print(f"\rfailed: {counter}", end='')
            counter += 1
        # time.sleep(0.1)


if __name__ == "__main__":
    find_trigger('start_coding.png')

    # # Open CMD and switch to desired directory
    # # Windows key + 1 hotkey?
    # pyautogui.hotkey('win', '1')
    #
    # # CMD version
    # # pyautogui.hotkey('win', 'r')  # Press the Ctrl-C hotkey combination.
    # # pyautogui.write('cmd', interval=0.15)
    # # pyautogui.press('enter')
    # # time.sleep(0.2)
    # # type cd {directory_path} + press enter
    # time.sleep(1.2)
    # # pyautogui.click(2000, 1000)
    # pyautogui.write('cd Documents\\python_scripts\\git_ready\\scratch\\league_autogui', interval=0.10)
    # pyautogui.press('enter')
    # # time.sleep(0.4)

    # Open Pycharm
    # Go to Desktop
    pyautogui.hotkey('win', 'd')
    # Press window key
    pyautogui.press('win')
    # type pych + press enter
    pyautogui.write('pych', interval=0.15)  # type with quarter-second pause in between each key
    pyautogui.press('enter')

