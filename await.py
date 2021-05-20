import time

import asyncio

# import win32gui, win32con, win32ui


if __name__ == "__main__":

    # title = "My Number"
    for x in enumerate(range(1, 11)):
        index, num = x
        print(
            # f"\n{title + ' ' + str(num):.30}"
            # f"\nIndex: [{index + 1}] {num:03} {num*num:4} {num*num*num:5}"
            # f"\n{30*'-'}"
            f"[{index + 1:02}]: {num:3} {num * num:4}  {num * num * num:5}"
        )
