import os

import time

import pyperclip
from tqdm import tqdm

#
# for i in tqdm(range(100)):
#     time.sleep(0.1)
#
# pbar = tqdm(["a", "b", "c", "d", "e", "f"])
# for char in pbar:
#     time.sleep(0.25)
#     pbar.set_description("Processing %s" % char)


# Manual Control
with tqdm(range(100)) as pbar:
    for i in pbar:
        pbar.set_description(f"Loading {i}%")
        # Postfix will be displayed on the right,
        # formatted automatically based on argument's datatype
        time.sleep(0.15)
        # pbar.update(10)


pyperclip.copy("whoa wtf...")
print(pyperclip.paste())
