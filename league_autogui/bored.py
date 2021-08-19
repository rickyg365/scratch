import os
import sys
import re
import time
import random

'''
{ start , monitor , after }
{aram , summoners rift , one for all} 
{ 0 , 0.0 , 19.1 , 20 , 30 }

start aram 20

start aram 19.2

monitor aram 20

start summoners rift 19.2

after 19.2

after 20

after 19.0

after 0.2

start aram 19.2

'''

if __name__ == "__main__":

    # raw_input = input("Select your settings: \n{ start, monitor, after} {aram, summoners rift, one for all} {Queue Timer}")

    raw_input = 'after'
    # Regex would be waaaay better for parsing
    master_pattern = re.compile(r'(start|monitor|after) (aram|summoners rift|one for all)? (\d*\.?\d*)?')
    # after_pattern = re.compile(r'(after) (\d*\.?\d*)?')

    parsed_input = re.search(master_pattern, raw_input)
    if parsed_input:
        print(parsed_input)
        print(f"config: {parsed_input[1]}")
        print(f"gamemode: {parsed_input[2]}")
        print(f"timer: {parsed_input[3]}")
        # try:
        #     timer = parsed_input[3]
        #     # print("yup")
        # except IndexError:
        #     print("nope")


    # start = re.search(master_pattern, raw_input)
    # if start:
    #     print(start)
    #     print(f"config: {start[1]}")
    #     print(f"gamemode: {start[2]}")
    #     print(f"timer: {start[3]}")
    #     try:
    #         yup = start[3]
    #         print("yup")
    #     except IndexError:
    #         print("nope")

    # after = re.search(after_pattern, raw_input)
    # if after:
    #     print(after)
    #     print(f"config: {after[1]}")
    #     print(f"timer: {after[2]}")

