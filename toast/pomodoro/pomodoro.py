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
    return f"{raw_minutes:02.0f} min, {seconds:02.0f} sec"


# Classes
class ClassName:
    def __init__(self):
        self.var = ""

    def __str__(self):
        text = ""
        return text


class PomoTimer:
    def __init__(self, study_timer=25, short_break_timer=10, long_break_timer=15):
        # 25-50 focus, 10-15 break
        # Cycles before a long break
        self.cycle = 2

        self.study_timer = study_timer*60
        self.short_break = short_break_timer*60
        self.long_break = long_break_timer*60

        self.toast = ToastNotifier()

    def __str__(self):
        text = f"Study: {self.study_timer} \nShort Break: {self.short_break} \nLong Break: {self.long_break} \nCycles: {self.cycle}"
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

        # study_thread = threading.Thread(
        #     target=self.make_toast,
        #     args=('Study', f"{format_time(self.study_timer)}")
        # )
        #
        # break_thread = threading.Thread(
        #     target=self.make_toast,
        #     args=('Short Break', f"{format_time(self.short_break)}")
        # )
        #
        # long_break_thread = threading.Thread(
        #     target=self.make_toast,
        #     args=('Long Break', f"{format_time(self.short_break)}")
        # )
        #
        # study_thread.daemon = True
        # break_thread.daemon = True
        # long_break_thread.daemon = True

        # print("")

        while run:
            for _ in range(self.cycle):
                # Study
                # if _ == 0:
                #     study_thread.start()
                # else:
                #     study_thread.run()
                self.make_toast("Study Time", format_time(self.study_timer))
                self.make_timer("Study", self.study_timer)

                # Break
                # if _ == 0:
                #     break_thread.start()
                #     continue
                # break_thread.run()
                self.make_toast("Short Break", format_time(self.short_break))
                self.make_timer("Break", self.short_break)

            # Study
            # study_thread.run()
            self.make_toast("Study Time", format_time(self.study_timer))
            self.make_timer("Study", self.study_timer)

            # Long Break
            # if not long_break_thread.is_alive():
            #     long_break_thread.start()
            # else:
            #     long_break_thread.run()
            self.make_toast("Long Break", format_time(self.long_break))
            self.make_timer("Long Break", self.long_break)

            # Continue
            cont = input("Do another loop?(Y/N): ")

            if cont.lower() == 'n':
                run = False

            # run = False


if __name__ == "__main__":
    #
    # total_time = float(input("Time: "))
    #
    # print(f"raw time: {total_time:,}s")
    # print(f"formatted time: {format_time(total_time)}")

    os.system("cls")

    my_timer = PomoTimer(1, 1, 2)
    try:
        my_timer.start()
    except KeyboardInterrupt:
        print("\n[Program Stopped]")
