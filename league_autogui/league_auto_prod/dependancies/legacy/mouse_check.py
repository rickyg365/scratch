import os
import time

import pyautogui


if __name__ == "__main__":
    pyautogui.displayMousePosition()
    im = pyautogui.screenshot('random_screenshot.png', region=(0, 0, 500, 500))
