import os
import sys

import time
import logging


"""
Program: Logging Playground
Author: rickyg3
Date: 04/27/2021
"""


if __name__ == "__main__":
    # Configure Log
    logging.basicConfig(filename='sample_log.log',
                        filemode='w',
                        datefmt='[%m-%d-%Y]:%H:%M:%S ',
                        format='%(asctime)s:%(name)s: %(levelname)s: %(message)s',
                        level=logging.DEBUG)

    # Loggers
    main_log = logging.getLogger(__name__)
    sample_log = logging.getLogger('sample_log')

    # Info
    main_log.info("Starting Main log")
    sample_log.info("Starting Sample log")

    # Debug
    # logging.debug("sample msg")
    sample_log.debug("sample debug msg")

    # Variable
    phone = {
        'name': 'Samsung Galaxy S9',
        'price': 990
    }
    sample_log.debug(f"{phone}")

    # Warning
    sample_log.warning("Test Warning")

