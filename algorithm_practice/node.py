import os
import sys

import time


class Node:
    def __init__(self, input_value=0):
        self.value = input_value
        self.left = None
        self.right = None

    def __str__(self):
        text = f"[{self.value}]\nleft: {self.left}\t \tright: {self.right}"
        return text

    # def add_child(self, new_value):
    #     if new_value < self.value:
    #         if self.left:
    #             self.left.add_child(new_value)
    #         else:
    #             self.left = Node(new_value)
    #
    #     elif new_value > self.value:
    #         if self.right:
    #             self.right.add_child(new_value)
    #         else:
    #             self.right = Node(new_value)


class BinarySearchTree:
    def __init__(self, root_value=None, root_node=None):
        if root_node is None:
            root_node = Node(root_value)

        self.root = root_node

    def __str__(self):
        text = ""
        
        return text

    def add_node(self, node_value=0, node_object=None):
        current = self.root
        if node_object:
            if node_object.value < current.value:
                if current.left:
                    current.left.add_node(node_object=node_object)
                else:
                    current.left = node_object
            elif node_object.value > current.value:
                if current.right:
                    current.right.add_node(node_object=node_object)
                else:
                    current.right = node_object
        else:
            if node_value < current.value:
                if current.left:
                    current.left.add_node(node_value)
                else:
                    current.left = Node(node_value)
            elif node_value > current.value:
                if current.right:
                    current.right.add_node(node_value)
                else:
                    current.right = Node(node_value)

    # def depth(self, max_depth=2):
    #     current_depth = 0
    #     if current_depth < max_depth:
    #         if .left is None:
    #             pass
    #         else:
    #             func(.left)
    #
    #         if .right is None:
    #             pass
    #         else:
    #             func(.right)
    #     elif current_depth == max_depth:


