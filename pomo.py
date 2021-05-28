import os
import time

"""
Program: Pomodoro Timer
Author: RickyG3
Date: 05-25-2021
"""


def clear_screen():
    os.system("cls")


class PomoTimer:
    def __init__(self, study_timer=25, short_break_timer=5, long_break_timer=15):
        self.cycle = 4

        self.study_timer = study_timer*60
        self.short_break = short_break_timer*60
        self.long_break = long_break_timer*60

    def __str__(self):
        text = f"Study: {self.study_timer} \nShort Break: {self.short_break} \nLong Break: {self.long_break} \nCycles: {self.cycle}"
        return text

    @ staticmethod
    def make_timer(timer_title, timer_amount):
        # Reference time
        start_time = time.perf_counter()

        # Timer Loop
        timed = True
        while timed:
            elapsed_time = time.perf_counter() - start_time
            countdown = timer_amount - elapsed_time
            minut = int(countdown//60)
            second = countdown % 60
            if minut >= 0:
                print(f"\r{timer_title}: [{minut:02}:{second:02.0f}]", end="")
            time.sleep(0.1)
            if elapsed_time > timer_amount:
                print(f"\r{timer_title}: [Finished]")
                timed = False

    def start(self):

        run = True

        while run:
            for _ in range(self.cycle):
                # Study
                self.make_timer("Study", self.study_timer)
                # Break
                self.make_timer("Break", self.short_break)
            # Study
            self.make_timer("Study", self.study_timer)
            # Long Break
            self.make_timer("Long Break", self.long_break)

            run = False
            # cont = input("Do another loop?(Y/N): ")
            #
            # if cont.lower() == 'n':
            #     run = False


if __name__ == "__main__":
    clear_screen()
    my_timer = PomoTimer(5, 1, 3)
    my_timer.start()
