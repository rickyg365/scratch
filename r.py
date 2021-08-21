import os

from win10toast import ToastNotifier

"""
Program: Windows Notfication
Author: 
Date: 08/20/21
"""

# Variables


# Functions
def func():
    return


# Classes
class ClassName:
    def __init__(self):
        self.var = ""

    def __str__(self):
        text = ""
        return text


if __name__ == "__main__":
    toast = ToastNotifier()

    title = "Title"
    body = "This is a sample msg"
    dur = 50

    toast.show_toast(title, body, duration=dur)  # can add icon_path="icon.ico"
