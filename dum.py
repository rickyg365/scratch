import os
import time


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

        self.depth = 1

    def __str__(self):
        # Initialize variables
        left = self.left
        right = self.right

        # Check for empty values
        if left is None:
            left = "N/A"
        if right is None:
            right = "N/A"

        # Create String
        string = f"[{left} <-{self.value}-> {right}]"

        return string


class Tree:
    def __init__(self, init_value=None):
        self.root = Node(init_value)

    def __str__(self):
        string = ""
        return string

    # This isnt a good print function, look at the node def of str
    # But this is a good way to see recursion it shows how the program goes through the list
    # def print_tree(self, current_node):
    #
    #     if current_node is None:
    #         print(" ")
    #         return 0
    #     else:
    #         print(current_node)
    #
    #     left_path = self.print_tree(current_node.left)
    #     right_path = self.print_tree(current_node.right)
    #
    #     return True

    def get_depth(self, current_node, depth):

        if current_node is None:
            return 0

        left_depth = self.get_depth(current_node.left, depth+1)
        right_depth = self.get_depth(current_node.right, depth+1)

        # print("\n-")
        # print(depth)
        # print(left_depth)
        # print(right_depth)

        return depth + max(left_depth, right_depth)


if __name__ == "__main__":
    my_tree = Tree(1)
    my_tree.root.left = Node(2)
    my_tree.root.right = Node(3)

    my_tree.root.left.left = Node(4)
    my_tree.root.left.right = Node(5)

    my_tree.root.right.left = Node(6)
    my_tree.root.right.right = Node(7)

    depth = my_tree.get_depth(my_tree.root, 0)

    # my_tree.print_tree(my_tree.root)
    print(my_tree.root)
    print(depth)
