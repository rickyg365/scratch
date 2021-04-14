import os
import sys

import numpy as np
import matplotlib.pyplot as plt

from load.load_csv import *


if __name__ == "__main__":
    pi = np.pi

    # x = np.arange(0.0, 10.0, 0.5)
    # y = [x**2 for x in x]

    x = np.arange(1, 10)
    y1 = x + 2
    y2 = x*6
    y3 = x/5

    # Can do multiple in one graph
    plt.plot(x, y1, color="red")
    plt.plot(x, y2, color="blue")
    plt.plot(x, y3, color="green")
    plt.grid(True)
    plt.title("Multiple Line Charts")
    plt.xlabel("This is x-axis label")
    plt.ylabel("This is y-axis label")
    plt.show()

    # Simple Bar
    # bar_x = [1, 2, 3]
    # bar_y = [5, 2, 1]
    # plt.bar(bar_x, bar_y, width=0.45, color="red")
    #
    # plt.title("Bar Chart")
    # plt.xlabel("This is x-axis label")
    # plt.ylabel("This is y-axis label")
    # plt.show()

    student_names = ["Patrick", "Spongebob", "Sandy", "Squidward"]
    name_index = np.arange(len(student_names))
    exam_scores = [2, 25, 98, 76]
    plt.bar(name_index, exam_scores, width=0.45, color="red")

    plt.title("Bar Chart")
    plt.xlabel("This is x-axis label")
    plt.ylabel("This is y-axis label")
    plt.xticks(name_index, student_names)
    plt.show()


    # pie chart
    percent = [60, 30, 10]
    language = ["Python", "Java", "C++"]

    plt.pie(percent, labels=language)
    plt.title("Simple Pie Chart")
    plt.show()

