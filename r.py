import os
import time

import threading
from win10toast import ToastNotifier

"""
Program: Windows Notfication
Author: 
Date: 08/20/21
"""

# Variables


# Functions
# def send_toast(title, message, notif_duration):
#     toast.show_toast(title, message, duration=notif_duration)  # can add icon_path="icon.ico"


# Classes
class ClassName:
    def __init__(self):
        self.var = ""

    def __str__(self):
        text = ""
        return text


if __name__ == "__main__":
    toast = ToastNotifier()

    # Toast Variables
    data = {
        'Title #1': 'Sample message',
        'Title #2': 'Sample message',
        'Title #3': 'Sample message'
    }

    duration = 7
    try:
        for t, msg in data.items():
            # Toast Thread
            toast.show_toast(t, msg, duration=duration, icon_path="question.ico")  # can add icon_path="icon.ico"

            # time.sleep(duration - .25)

    except KeyboardInterrupt:
        print("[Program Stopped]")
        run = False
