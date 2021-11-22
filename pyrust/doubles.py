import re
import string
import random

# Rust Library
import myrustlib
import pytest

"""
On Mac OS, you will need to rename the output from *.dylib to *.so. 
On Windows, you will need to rename the output from *.dll to *.pyd.
"""


""" Test Python String Processing """
# pairs of repeated chars, sequential


# Python ZIP version
def count_doubles(value):
    """ Count doubles(sequential) w/ ZIP iterator """
    total = 0

    for c1, c2 in zip(value, value[1:]):
        if c1 == c2:
            total += 1

    return total


# Python REGEX version
def count_doubles_regex(value):
    """ Count doubles(sequential) w/ REGEX """
    double_re = re.compile(r'(?=(.)\1)')

    return len(double_re.findall(value))


# Testing
num_chars = 1_000_000
test_value = ''.join(random.choice(string.ascii_letters) for i in range(num_chars))


def test_pure_python(benchmark):
    benchmark(count_doubles, test_value)


def test_regex(benchmark):
    benchmark(count_doubles_regex, test_value)


def test_rust(benchmark):
    benchmark(myrustlib.count_doubles, test_value)


if __name__ == "__main__":
    sample_val = "abbcdefdefg"

    print("Sample: ", count_doubles(sample_val))
