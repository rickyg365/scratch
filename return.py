import os
import time

print("Line", end='')
time.sleep(0.65)
print("\rLine 1", end='')
time.sleep(0.55)
print("\rLine 1 2", end='')
time.sleep(0.45)
print("\rLine 1 2 3", end='')
time.sleep(0.45)
print("\rLine 1 2 3 4", end='')
time.sleep(0.45)
print("\rLine 1 2 3 4 5", end='')
time.sleep(0.45)
print("\rLine 1 2 3 4 5 6", end='')
time.sleep(0.45)
'''

░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░█▀▀█░█▀▀█░░░█▀▀▀░▀▀▀█░░█░░░░
░░░█▄▄█░█▄▄█░░░█▀▀▀░░▄▀░░░▀░░░░
░░░█░░█░█▄▄█░░░▀▀▀▀░▀▀▀▀░░▀░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░


░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░█▀▀▀░█▀▀▀░░░█▀▀▀░▀▀▀█░░█░░░░
░░░█░▀█░█░▀█░░░█▀▀▀░░▄▀░░░▀░░░░
░░░▀▀▀▀░▀▀▀▀░░░▀▀▀▀░▀▀▀▀░░▀░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░

░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░█▀▀▀░█▀▀▀░░░█▀▀▀░▀▀▀█░░█░░░░
░░░█░▀█░█░▀█░░░█▀▀▀░░▄▀░░░▀░░░░
░░░▀▀▀▀░▀▀▀▀░░░▀▀▀▀░▀▀▀▀░░▀░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░

░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░█▀▀▀░█▀▀▀░░░█▀▀▀░▀▀▀█░░█░░░░
░░░█░▀█░█░▀█░░░█▀▀▀░░▄▀░░░▀░░░░
░░░▀▀▀▀░▀▀▀▀░░░▀▀▀▀░▀▀▀▀░░▀░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░

( ͡⚆ ͜ ⚆ )╭╮
∩╮
( ⚆ ͜ ⚆ )
╭∩
'''
inp = input("\n")
path = os.getcwd()
system = os.name
print(path)
# print(system)
if system == 'nt':
    print("OS: Windows")
elif system == "posix":
    print("OS: Linux")
else:
    print(f"OS: {system}")
