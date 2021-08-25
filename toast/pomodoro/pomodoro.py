import os
import time

import threading
from win10toast import ToastNotifier

"""
Program: Pomodoro Toast Timer
Author: Rickyg3
Date: 08/22/21
"""


# Variables


# Functions
def func():
    return


def split_raw_time(raw_time: int, day=False,) -> (int, int):
    """
    split time
    add flags to do different conversions beside seconds minutes hours
    such as a flag to do days
    """

    if day:
        base = raw_time // 24
        remainder = raw_time % 24

        return base, remainder

    base = raw_time // 60
    remainder = raw_time % 60

    return base, remainder


def format_time(raw_seconds):
    """
    Takes in raw_seconds and formats to hh:mm:ss
    """
    # Variables
    minutes = 0
    hours = 0
    raw_hours = 0
    days = 0

    hour_flag = False
    day_flag = False

    # Parse Time
    raw_minutes, seconds = split_raw_time(raw_seconds)

    if raw_minutes > 60:
        hour_flag = True
        raw_hours, minutes = split_raw_time(raw_minutes)
        # Extra I guess, I could just name raw_hours, hours?
        hours = raw_hours

    if hour_flag and raw_hours > 60:
        day_flag = True
        days, hours = split_raw_time(raw_hours, day=True)

    # Conditions on which one to return
    if day_flag:
        # Timer Display
        # return f"[{days}days ({hours:02.0f}{minutes:02.0f}:{seconds:02.0f})]"
        return f"{days} days ({hours:02.0f} hr, {minutes:02.0f} min, {seconds:02.0f} sec)"

    if hour_flag:
        # Timer Display
        # return f"[{hours:02.0f}:{minutes:02.0f}:{seconds:02.0f}]"
        return f"{hours:02.0f} hours, {minutes:02.0f} min, {seconds:02.0f} sec"

    # Timer Display
    # return f"[{raw_minutes:02.0f}:{seconds:02.0f}]"
    # minute_flag = True
    # second_flag = True
    # f"{minutes if minute_flag else ''} {seconds if second_flag else ''}"
    return f"{raw_minutes:02.0f} min, {seconds:02.0f} sec"


# Classes
class ClassName:
    def __init__(self):
        self.var = ""

    def __str__(self):
        text = ""
        return text


class PomoTimer:
    def __init__(self, study_timer=25, short_break_timer=10, long_break_timer=15, cycle=4, title="p_timer"):
        # 25-50 focus, 10-15 break
        # Cycles before a long break
        self.title = title
        self.cycle = cycle

        self.study_timer = study_timer*60
        self.short_break = short_break_timer*60
        self.long_break = long_break_timer*60

        self.nice_time = f"{format_time(self.study_timer)} {format_time(self.short_break)} {format_time(self.long_break)} "

        self.toast = ToastNotifier()

    def __str__(self):
        text = f"[{self.title}] => Study: {self.study_timer} \nShort Break: {self.short_break} \nLong Break: {self.long_break} \nCycles: {self.cycle}"
        return text

    @ staticmethod
    def make_timer(timer_title, timer_amount):
        # Reference time, perf_counter keeps track of time even while sleep
        start_time = time.perf_counter()

        # Timer Loop
        timed = True
        while timed:
            elapsed_time = time.perf_counter() - start_time
            countdown = timer_amount - elapsed_time

            if countdown//60 > 0:
                minute, sec = split_raw_time(countdown)
                print(f"{timer_title}: [{minute:02.0f}:{sec:02.0f}] ", end="\r")
            else:
                print(f"{timer_title}: [{countdown:02.0f}]          ", end="\r")

            time.sleep(0.12)

            if elapsed_time > (timer_amount - 0.14):
                print(f"{timer_title}: [Finished]                   ", end="\n")
                timed = False

    def make_toast(self, toast_title, toast_msg):
        self.toast.show_toast(toast_title, toast_msg, duration=7, threaded=True)  # can add icon_path="icon.ico"

    def start(self):

        run = True

        while run:
            for _ in range(self.cycle):
                # Study
                self.make_toast("Study Time", format_time(self.study_timer))
                self.make_timer("Study", self.study_timer)

                # Break
                self.make_toast("Short Break", format_time(self.short_break))
                self.make_timer("Break", self.short_break)

            # Study
            self.make_toast("Study Time", format_time(self.study_timer))
            self.make_timer("Study", self.study_timer)

            # Long Break
            self.make_toast("Long Break", format_time(self.long_break))
            self.make_timer("Long Break", self.long_break)

            # Continue
            cont = input("Do another loop?(Y/N): ")

            if cont.lower() == 'n':
                run = False

            # run = False


class TimerHandler:
    def __init__(self, raw_data=None, input_file=""):
        if raw_data is None:
            raw_data = {}

        raw_data_flag = len(raw_data.keys()) > 0
        input_file_flag = input_file != ""

        self.timers = []
        self.choice_dictionary = {}

        # Handle Raw Data

        self.raw_data = raw_data
        if len(raw_data.keys()) > 0:
            self.parse_data()

        self.raw_input_file = input_file
        if input_file_flag:
            self.parse_file()

    def __str__(self):
        text = ""
        for _, timer in enumerate(self.timers):
            text += f"\n[{_+1}]: {timer.title}"
        return text

    def parse_data(self):
        # Build Timers and add to list
        data = self.raw_data

        for title, param in self.raw_data.items():
            study, short_break, long_break, cycle = param

            self.add_timer(study, short_break, long_break, cycle, title)

    def parse_file(self):
        file_path = self.raw_input_file

        # For text files
        with open(self.raw_input_file, 'r') as read_file_in:
            for line in read_file_in:
                print(line)

        # For json files

        # For CSV files

        return "TBI"

    def build_choice_dict(self):
        for index, timer in enumerate(self.timers):
            self.choice_dictionary[timer.title] = index

    def add_timer(self, study_timer, short_break, long_break, cycle=4, title="p_timer"):

        new_timer = PomoTimer(
            study_timer=study_timer,
            short_break_timer=short_break,
            long_break_timer=long_break,
            cycle=cycle,
            title=title
        )

        self.timers.append(new_timer)

    def get_timer(self, timer_title):
        # Choose Timer
        self.build_choice_dict()

        # get by title
        if timer_title in self.choice_dictionary.keys():
            return self.timers[self.choice_dictionary[timer_title]]

        # get by index
        try:
            converted_index = int(timer_title) - 1
        except ValueError:
            converted_index = ""

        condition = converted_index in self.choice_dictionary.values()
        if condition:
            return self.timers[converted_index]

        # Returns default if not a valid choice
        return self.timers[0]

    def choose_timer(self):
        # DEFAULT
        input_choice = self.timers[0]

        # Choose Timer
        print("**Please type full timer name**")
        # Display Available Timers
        print(self)

        try:
            input_choice = input("\nChoose Timer: ").lower()
        except KeyboardInterrupt:
            print("\n \n[Program Stopped]")
            quit()

        return self.get_timer(input_choice)


if __name__ == "__main__":
    # Raw Timer Data
    timers_template = {
        'neuro': (25, 5, 20, 4),
        'adhd': (10, 3, 5, 4),
        'test': (1, 1, 3, 2)
    }

    # Variables
    timer_handler = TimerHandler(timers_template)

    # Clear Display
    os.system("cls")

    # Choose Timer
    choice_timer = timer_handler.choose_timer()

    # Clear Display
    os.system("cls")

    # Run Selected Timer
    try:
        print(f"[{choice_timer.title.upper()}]\n")
        choice_timer.start()
    except KeyboardInterrupt:
        print("\n[Program Stopped]")
