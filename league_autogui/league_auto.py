import os
import sys

import cv2

import time
import pyautogui


"""
screenWidth, screenHeight = pyautogui.size()  # Get the size of the primary monitor.
currentMouseX, currentMouseY = pyautogui.position()  # Get the XY position of the mouse.
pyautogui.moveTo(100, 150)  # Move the mouse to XY coordinates.
pyautogui.click()          # Click the mouse.
pyautogui.click(100, 200)  # Move the mouse to XY coordinates and click it.
pyautogui.click('button.png')  # Find where button.png appears on the screen and click it.
pyautogui.move(0, 10)      # Move mouse 10 pixels down from its current position.
pyautogui.doubleClick()    # Double click the mouse.
pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)   # Use tweening/easing function to move mouse over 2 seconds.
pyautogui.write('Hello world!', interval=0.25)  # type with quarter-second pause in between each key
pyautogui.press('esc')     # Press the Esc key. All key names are in pyautogui.KEY_NAMES
pyautogui.keyDown('shift')  # Press the Shift key down and hold it.
pyautogui.press(['left', 'left', 'left', 'left'])  # Press the left arrow key 4 times.
pyautogui.keyUp('shift')   # Let go of the Shift key.
pyautogui.hotkey('ctrl', 'c')  # Press the Ctrl-C hotkey combination.
pyautogui.alert('This is the message to display.')  # Make an alert box appear and pause the program until OK is clicked.
"""


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
        button = pyautogui.locateCenterOnScreen(image_file, confidence=0.9)

        if button:
            print("\nTrigger Found!")
            return True

        else:
            print(f"\rfailed: {counter}", end='')
            counter += 1


if __name__ == "__main__":

    # For when you're in low priority queue
    # wait_timer(11)

    ''' New School '''
    # find_trigger('send_it.png')
    find_trigger('specific.png')

    # after a match is over
    find_button_click('play_again.png')
    print("")
    time.sleep(1)
    print("")
    find_button_click('find_match.png')
    print("")
    # find_button_click('decline.png', loop_var=True)
    print("")
    find_button_click('accept.png', repeat=True)

