import os

import re

import time
import random

"""

"""


class Matrix:
    def __init__(self, matrix_data=None):
        if matrix_data is None:
            matrix_data = []
        self.data = matrix_data

        self.rows = len(self.data)
        self.columns = len(self.data[0])

        self.longest_entry_length = 0
        self.get_longest_item_length()

    def __str__(self):
        matrix = ""
        for row in self.data:
            for item in row:
                new_entry = f"{item}"
                if len(new_entry) < self.longest_entry_length:
                    difference = self.longest_entry_length - len(new_entry)
                    new_entry += f"{difference*' '}"
                matrix += (new_entry + ' ')
            matrix += '\n'
        return matrix

    def __add__(self, other):
        new_matrix = []
        # check if both objects have the same dimensions
        for i in range(self.rows):
            new_row = []
            for j in range(self.columns):
                new_row.append(self.data[i][j] + other.data[i][j])
            new_matrix.append(new_row)

        return Matrix(new_matrix)

    def get_longest_item_length(self):
        for row in self.data:
            for item in row:
                item_length = len(f"{item}")
                if item_length > self.longest_entry_length:
                    self.longest_entry_length = item_length

    def diagonalize(self):
        ...

    def orthonormalize(self):
        ...

    def find_determinant(self):
        ...

    def rref(self):
        '''
         1  1 -1  -2
         2 -1  1   5
        -1  2  2   1


         1  2  3  9
         2 -1  1  8
         3  0 -1  3

         sol:
          1 0 0  2
          0 1 0 -1
          0 0 1  3

        '''
        # # only reducing rows to have leading 1
        # for i in range(self.rows):
        #     # new_row = []
        #     while self.data[i][i] != 1:
        #         # what do we do
        #         for ele in self.data[i]:
        #
        ...


if __name__ == "__main__":
    # matrix_to_be = [
    #     ['v11', 'v12', 'v13'],
    #     ['v21', 'v22', 'v23'],
    #     ['v31', 'v32', 'v33']
    # ]
    # matrix_to_be = [
    #     [11, 12, 13],
    #     [21, 22, 23],
    #     [31, 32, 33]
    # ]
    matrix_to_be = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    matrix_two_be = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    new_matrix_obj = Matrix(matrix_to_be)
    second_matrix = Matrix(matrix_two_be)

    third_matrix = new_matrix_obj + second_matrix

    print(new_matrix_obj)

    print(second_matrix)

    print(third_matrix)

