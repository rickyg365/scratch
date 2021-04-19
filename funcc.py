import os

import time
import random

import numpy as np
import matplotlib.pyplot as plt


# Regular Function Definition
def f(x: float):
    return x**2

# Lambda version
# f = lambda x: x ** 2


if __name__ == "__main__":
    input_num = float(input("Choose a number: "))
    print(f"number: {input_num}\nsquared: {f(input_num)}")

    x1 = float(input("Choose max range: "))
    x2 = float(input("Choose max range: "))

    data1 = np.arange(1, x1, 0.5)
    data2 = np.arange(1, x2, 0.5)

    fdata1 = list(map(f, data1))
    fdata2 = list(map(f, data1))

    # Fix Figure
    plt.title("My graph")
    plt.xlabel("x axis")
    plt.ylabel("y axis")

    plt.subplot(211)
    plt.plot(data1, fdata1)

    plt.subplot(212)
    plt.plot(data2, fdata2)

    plt.show()
