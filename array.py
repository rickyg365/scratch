import os
import sys

import time

""" 
Program: 
Author: rickyg3
Date: 
"""


def clear_screen():
    os.system("cls")


class Animation:
    def __init__(self):
        self.frames = []
        self.current_index = 0

    def __str__(self):
        text = ""
        return text

    def add_frame(self, frame_obj):
        # if type(frame_obj) == 'list':
        self.frames = frame_obj

    def iterate_frame(self, loop=2):
        for i in range(loop):
            clear_screen()
            for frame in self.frames:
                display = ""
                for line in frame:
                    clear_screen()
                    display += line + '\n'
                sys.stdout.write(display)
                time.sleep(0.35)

    def reverse_iterate(self):
        pass


if __name__ == '__main__':
    # FRAMES
    frame1 = [
        f".----------------------.",
        f"| Malfoy         lvl.3 |",
        f"|----------------------|",
        f"| [@@@@@@@@@@@@@@@@@@] |",
        f"'----------------------'"
    ]

    frame2 = [
        f".----------------------.",
        f"| Malfoy         lvl.3 |",
        f"|----------------------|",
        f"| [@@@@@@@@@@@@@@@@  ] |",
        f"'----------------------'"
    ]

    frame3 = [
        f".----------------------.",
        f"| Malfoy         lvl.3 |",
        f"|----------------------|",
        f"| [@@@@@@@@@@@@@@    ] |",
        f"'----------------------'"
    ]

    frame4 = [
        f".----------------------.",
        f"| Malfoy         lvl.3 |",
        f"|----------------------|",
        f"| [@@@@@@@@@@@@      ] |",
        f"'----------------------'"
    ]

    frame5 = [
        f".----------------------.",
        f"| Malfoy         lvl.3 |",
        f"|----------------------|",
        f"| [@@@@@@@@@@        ] |",
        f"'----------------------'"
    ]

    frame6 = [
        f".----------------------.",
        f"| Malfoy         lvl.3 |",
        f"|----------------------|",
        f"| [@@@@@@@@          ] |",
        f"'----------------------'"
    ]

    frame7 = [
        f".----------------------.",
        f"| Malfoy         lvl.3 |",
        f"|----------------------|",
        f"| [@@@@@@            ] |",
        f"'----------------------'"
    ]

    frame8 = [
        f".----------------------.",
        f"| Malfoy         lvl.3 |",
        f"|----------------------|",
        f"| [@@@@              ] |",
        f"'----------------------'"
    ]

    frame9 = [
        f".----------------------.",
        f"| Malfoy         lvl.3 |",
        f"|----------------------|",
        f"| [@@                ] |",
        f"'----------------------'"
    ]

    frame10 = [
        f".----------------------.",
        f"| Malfoy         lvl.3 |",
        f"|----------------------|",
        f"| [                  ] |",
        f"'----------------------'"
    ]

    health_frames = [
        frame1,
        frame2,
        frame3,
        frame4,
        frame5,
        frame6,
        frame7,
        frame8,
        frame9,
        frame10
    ]
    # print(frame10)
    health_animation = Animation()
    health_animation.add_frame(health_frames)

    health_animation.iterate_frame()
