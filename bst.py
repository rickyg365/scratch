import os
import sys

import time

""" 
Program: Binary Search Tree
Author: medium article
Date: 03/25/2021
"""


# For now only use numbers for the value
class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

    def add_node(self, data):
        if data == self.data:
            return  # Node exists
        if data < self.data:
            if self.left_child:
                self.left_child.add_node(data)
            else:
                self.left_child = BinaryTree(data)

        else:
            if self.right_child:
                self.right_child.add_node(data)
            else:
                self.right_child = BinaryTree(data)

    def find_node(self, value):
        if self.data == value:
            return True
        if value < self.data:
            if self.left_child:
                return self.left_child.find_node(value)
            else:
                return False

        if value > self.data:
            if self.right_child:
                return self.right_child.find_node(value)
            else:
                return False

    def in_order_traversal(self):
        elements = []
        if self.left_child:
            elements += self.left_child.in_order_traversal()

        elements.append(self.data)

        if self.right_child:
            elements += self.right_child.in_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []
        if self.left_child:
            elements += self.left_child.post_order_traversal()
        if self.right_child:
            elements += self.right_child.post_order_traversal()

        elements.append(self.data)

        return elements

    def pre_order_traversal(self):
        elements = [self.data]
        if self.left_child:
            elements += self.left_child.pre_order_traversal()
        if self.right_child:
            elements += self.right_child.pre_order_traversal()

        return elements

    def max_node(self):
        if self.right_child is None:
            return self.data
        return self.right_child.max_node()

    def min_node(self):
        if self.left_child is None:
            return self.data
        return self.left_child.min_node()

    def sum_of_node(self):
        left_sum = self.left_child.sum_of_node() if self.left_child else 0
        right_sum = self.right_child.sum_of_node() if self.right_child else 0
        return self.data + left_sum + right_sum


def build_tree(elements):
    root = BinaryTree(elements[0])
    for i in range(1, len(elements)):
        root.add_node(elements[i])
    return root


if __name__ == '__main__':
    values = [3, 7, 6, 4, 5]
    tree = build_tree(values)

    print(tree.min_node())
    print(tree.max_node())
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())
    print(tree.pre_order_traversal())
    print(tree.find_node(3))
    print(tree.sum_of_node())
