import os
import time

import random


"""
Timer works for seconds add an if clause that converts the time to minutes if its has more than 60 seconds
"""


class Timer:
    def __init__(self):
        self.start_time = 0
        self.end_time = 0

    def __str__(self):
        text = f"[{self.end_time - self.start_time:02.2f}]"
        return text

    @staticmethod
    def format_time(raw_time):
        seconds = raw_time
        # Check for Minutes
        minutes = raw_time//60
        if minutes >= 1:
            seconds = raw_time % 60

        # Check for Hours
        hours = minutes//60
        if hours >= 1:
            minutes = minutes % 60

        return f"{hours:0} {minutes:02}:{seconds:02.2f}"

    def start(self):
        self.start_time = time.time()

    def end(self):
        self.end_time = time.time()

    def run(self, duration):
        self.start_time = time.time()
        while True:
            current_time = time.time()
            if self.start_time + duration < current_time:
                break

            print(f"[{self.format_time(current_time - self.start_time)}] ", end='\r')

            # slow it down some
            time.sleep(.05)


if __name__ == "__main__":

    new_timer = Timer()
    timer_duration = int(input("Timer duration?: "))

    new_timer.run(timer_duration)

