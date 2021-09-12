import os
import pytest

"""
Program: A way to  output test in a nice way
Author: Rickyg3
Date: 09/09/2021
"""

"""
Sample Output:

[✓]
[ ]
[x]


☐	☑	☒

"""


# Variables


# Functions
def sum(a, b):
    return a + b


def division_tuple(a, b):
    root = a // b
    remainder = a % b

    return root, remainder


def strip_element(list_element):
    fixed_element = list_element.strip()
    fixed_element = fixed_element.lower()

    return fixed_element


def count_vowel(input_string):
    vowels = 'aeiou'
    counter = {}

    for current_vowel in vowels:
        # adds each vowel to the dictionary with a value of 0 regardless if it is in string or not
        counter[current_vowel] = 0

        if current_vowel in input_string:
            vowel_count = input_string.count(current_vowel)
            counter[current_vowel] = vowel_count

    return counter


# Testing
def test_sum():
    x = 2
    y = 8
    assert sum(x, y) == 10


def test_division_tuple():
    x = 13
    y = 3
    assert division_tuple(x, y) == (4, 1)


def test_strip_element():
    test_list = [
        ' .why',
        ' did.- ',
        ' I ',
        'do ',
        ' this',
    ]

    output_list = list(map(strip_element, test_list))
    sample_list = ['.why', 'did.-', 'i', 'do', 'this']
    # return output_list

    for i, ele in enumerate(sample_list):
        assert output_list[i] == ele


def test_count_vowel():
    test_string = 'you mutha fukka'
    test_output = {
        'a': 2,
        'e': 0,
        'i': 0,
        'o': 1,
        'u': 3
    }
    assert count_vowel(test_string) == test_output


def check(func_name):
    if func_name() is None:
        print('[✓]', func_name.__name__)
    else:
        print('[x]', func_name.__name__)
    return


# Classes
class ClassName:
    def __init__(self):
        self.var = ""

    def __str__(self):
        text = ""
        return text


if __name__ == "__main__":
    # os.system('cls')
    # check(test_sum)
    #
    # check(test_division_tuple)
    #
    # check(test_strip_element)
    #
    # check(test_count_vowel)

    """
    Check random input
    
    def check_input(func_name, x):
        try:
            func_name(x)
        except Exception as e:
            print(e)
        
    """

    functions_to_test = [
        test_sum,
        test_division_tuple,
        test_strip_element,
        test_count_vowel
    ]

    print("\n[ Python Tester ] \n")

    for func in functions_to_test:
        check(func)

    print("\n")
