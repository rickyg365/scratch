import os
import time

import numpy as np

from datetime import datetime
from typing import List


# Timer Decorator
def time_dat_shit(func):
    """ A simple Timer decorator """
    def wrapper(*args, **kwargs):
        # Start Time
        start = datetime.now()
        func_return_value = func(*args, **kwargs)
        end = datetime.now()

        # Total Time elapsed
        final_time = (end-start).total_seconds()
        print(f"\n[ Executed in {final_time:.1f}s ]")

        # Return function return value
        # return func_return_value
    return wrapper


class BinarySearch:
    def __init__(self, input_array):
        self.array = input_array

    def __str__(self):
        line1 = ""
        line2 = ""
        for ind, item in enumerate(self.array):
            line1 += f"{ind:^3} |"
            line2 += f"{item:^3} |"

        text = line1 + '\n' + line2
        return text

    def bisect_left(self, search_number: int):
        """ returns the index of the first instance of the search number """
        # < 7
        lower = 0
        upper = len(self.array)

        while lower < upper:
            # visualize
            # print(items[lower:upper])
            mid = (lower + upper) // 2
            if self.array[mid] < search_number:
                lower = mid + 1
            else:
                upper = mid

        # can return lower or upper
        return lower

    def bisect_right(self, search_number: int):
        """ returns the index after the last instance of the search number """
        # <= 7
        lower = 0
        upper = len(self.array)

        while lower < upper:
            # visualize
            # print(items[lower:upper])
            mid = (lower + upper) // 2
            if self.array[mid] <= search_number:
                lower = mid + 1
            else:
                upper = mid

        # can return lower or upper
        return lower


@time_dat_shit
def main():
    """
    Notes:
        # 2.5 sec to create array w/out numpy
        sorted_arr = [i for i in range(1, 50_000_001)]

        # 0.1 sec to create with numpy
        sorted_arr = np.arange(1, 50_000_001)
    """
    # Create Arrays, sorted and unsorted
    sorted_arr = np.arange(1, 11)
    unsorted_arr = [9, 3, 2, 5, 7, 1, 6, 4, 10, 8]
    test_arr = [1, 2, 2, 4, 5, 5, 7, 8, 9, 9]

    # print("Sorted: ", sorted_arr)
    # print("Unsorted: ", unsorted_arr)

    # Test BinarySearch class
    search_list = BinarySearch(test_arr)

    print("Bisect Left: ", search_list.bisect_left(5))
    print("Bisect Right: ", search_list.bisect_right(5))


if __name__ == "__main__":
    main()
