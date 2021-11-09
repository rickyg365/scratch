import os
from typing import List
from dataclasses import dataclass


class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

    def __str__(self):
        return f"{self.value}"

    def __repr__(self):
        return f"value: {self.value}, next: {'None' if self.next is None else self.next.value}"


class LinkedList:
    def __init__(self, head: Node = None):
        self.head = head
        self.length = 0

    def __str__(self):
        current_node = self.head
        output = ""

        while current_node:
            output += f"{current_node} -> "
            current_node = current_node.next

        output += "None"
        return output

    def insert(self, value):
        node = Node(value)

        if self.head is None:
            self.head = node
            return

        current_node = self.head

        while current_node:

            if current_node.next is None:
                current_node.next = node
                return
            current_node = current_node.next

    def update_length(self):

        current_node = self.head
        counter = 0

        while current_node:
            counter += 1

            current_node = current_node.next

        self.length = counter


if __name__ == "__main__":
    raw_list = [x for x in range(1, 11)]  # List of Nodes

    new_ll = LinkedList()

    print(f"Raw List: {raw_list}")

    for i in raw_list:
        new_ll.insert(i)

    new_ll.update_length()

    print(f"Linked List: {new_ll}")
    print(f"Length: {new_ll.length}")
