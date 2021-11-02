import os
import time

"""
Program: Console Pomodoro bar
Author: rickyg3
Date: 10/22/21
"""


# Variables
"""
─	━	│	┃	┄	┅	┆	┇	┈	┉	┊	┋	┌	┍	┎	┏
┐	┑	┒	┓	└	┕	┖	┗	┘	┙	┚	┛	├	┝	┞	┟
┠	┡	┢	┣	┤	┥	┦	┧	┨	┩	┪	┫	┬	┭	┮	┯
┰	┱	┲	┳	┴	┵	┶	┷	┸	┹	┺	┻	┼	┽	┾	┿
╀	╁	╂	╃	╄	╅	╆	╇	╈	╉	╊	╋	╌	╍	╎	╏
═	║	╒	╓	╔	╕	╖	╗	╘	╙	╚	╛	╜	╝	╞	╟
╠	╡	╢	╣	╤	╥	╦	╧	╨	╩	╪	╫	╬	╭	╮	╯
╰	╱	╲	╳	╴	╵	╶	╷	╸	╹	╺	╻	╼	╽	╾	╿

fill
█

■

"""


def progress_bar(iterable, raw_length, title="", delay=0):
    no_title = False
    if title == "":
        no_title = True
        title = "12345"

    space_available = raw_length - (len(title) + 5)
    # print(space_available, raw_length, len(title))

    for index, item in enumerate(iterable):
        per_iter = round((index/len(iterable))*space_available)

        bar = "█" * per_iter
        space = (space_available - len(bar)) * " "

        final_bar = f"[{title}] |{bar}{space}|"
        if no_title:
            final_bar = f"[{100*per_iter / space_available:02.0f} %] |{bar}{space}|"
        # print(f"{per_iter}/{space_available}")
        if index+1 == len(iterable):
            if no_title:
                print(f"[100%] |{'█'*space_available}|")
            else:
                print(f"[{title}] |{'█' * space_available}|")
            yield item
            break

        print(final_bar, end="\r")

        if delay > 0:
            time.sleep(delay)

        yield item


def timer_bar(duration, raw_length, title="Timer Name"):
    length = raw_length - len(title) - 12
    seconds = duration * 60
    per_block = seconds / length
    eta = seconds

    for i in range(length+1):
        bar = "█" * i
        space = (length - i) * " "

        processed_eta = f"{eta//60 if (eta//60 > 0) else abs(eta):02.0f} {'min' if (eta//60 > 0) else 'sec'}"

        final_bar = f"[{title}] {processed_eta} |{bar}{space}|"

        if i == length:
            print(final_bar)
            break

        print(final_bar, end="\r")
        eta -= per_block
        time.sleep(per_block)


if __name__ == "__main__":
    size = os.get_terminal_size()
    columns = size[0]

    myList = [x for x in range(1, 21)]
    total = 0
    for i in progress_bar(myList, columns, "add", delay=1):
        total += i

    for j in progress_bar(myList, columns, "square", delay=1):
        total += j**2

    print(f"total: {total}")
    # size = os.get_terminal_size()
    # columns = size[0]
    #
    # cycles = int(input("\nno. of cycles: "))
    #
    # os.system("cls")
    # for _ in range(cycles):
    #     cycle_no = _ + 1
    #
    #     print(f"Cycle {cycle_no}/{cycles}:")
    #     timer_bar(1/20, columns, "Study")
    #     timer_bar(1/20, columns, "Short")
    #     timer_bar(2/10, columns, "Long")
    #     print("")
