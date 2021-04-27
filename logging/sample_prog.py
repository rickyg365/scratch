import os
import sys

import time
import logging

import numpy as np

# Configure Log
logging.basicConfig(filename='sample_prog.log',
                    filemode='w',
                    datefmt='[%m-%d-%Y]:%H:%M:%S ',
                    format='%(asctime)s:%(name)s: %(levelname)s: %(message)s',
                    level=logging.DEBUG)

# Loggers
main_log = logging.getLogger(__name__)
parse_list_log = logging.getLogger('parse_list_log')

if __name__ == "__main__":
    main_log.info("Starting Program")

    def cube(input_num):
        output = ''
        try:
            output = input_num ** 3
        except TypeError:
            variable = {
                'Value': f"{input_num}",
                'Type': f"{type(input_num)}"
            }
            parse_list_log.warning(f"Input was not a float: {variable}")
        finally:
            parse_list_log.debug(f"input: {input_num} output: {output}")
        return output

    # num_list = [x for x in range(11)]
    num_list = np.arange(0, 10, 0.5)

    # num_list = ['0.0', 0.0, 2, 34, 'hi', True]

    new_list = list(map(cube, num_list))

    print(f"Original list: {num_list}")
    print(f"New list: {new_list}")
