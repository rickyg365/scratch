import os

from test_toast import *

"""
Program: Windows Notification Timer
Author: Rickyg3
Date: 08/21/21
"""


# Variables


# Functions
def func():
    return


# Classes
class Timer:
    def __init__(self):
        self.time_started = time.time()
        self.start_time = time.time()

        self.current_time = time.time()

        self.end_time = 0

        self.notif_handler = WinNotif()

    def __str__(self):
        text = f"{self.end_time - self.start_time}"
        return text

    def reset(self):
        self.start_time = time.time()
        self.current_time = time.time()
        self.end_time = 0

    def start(self):
        # print("[Timer Started]")
        self.start_time = time.time()
        self.notif_handler.flip_flag('start')

    def stop(self):
        # print("[Timer Stopped]")
        self.end_time = time.time()

    def run_timer(self, timer_length):
        self.notif_handler.edit_flag('start', "Timer Started", f"{timer_length}s")

        self.start()
        self.notif_handler.run_toast('start')
        self.current_time = time.time()

        while (self.current_time - self.start_time) < timer_length:
            self.current_time = time.time()
            # save this print statement for the command line version
            # print(f"[{(self.current_time-self.start_time):02.2f}]   ", end='\r')

            time.sleep(.15)

        self.stop()
        print(f"Elapsed Time: {self.end_time - self.start_time:.2f}")
        # has to be after the self.stop() or else it wont have the correct end_time
        self.notif_handler.edit_flag('done', 'Timer Done', f" time elapsed: {(self.end_time - self.start_time):.2f}")
        self.notif_handler.run_toast('done')


if __name__ == "__main__":
    my_timer = Timer()
    my_timer.run_timer(int(input("Timer: ")))

    # my_timer.start()
    # time.sleep(2)
    # my_timer.stop()
    #
    # print(f"Total Time: {my_timer.end_time - my_timer.start_time}")
