import os
import sys

import time

""" 
Program: Linked List scene map
Author: rickyg3
Date: 
"""


class Node:
    def __init__(self, object_data=None):
        self.object_data = object_data
        self.next = None

    def __str__(self):
        text = f"[{self.object_data}]"
        return text

    def __next__(self):
        return self.next


class Scene(Node):
    """
    A single screen that displays, inherits from the node class so we can make a scene map
    """
    def __init__(self, object_data):
        super().__init__(object_data)

    def __str__(self):
        text = f"{self.object_data}"
        return text


class SceneMap:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current_node = None

    def __str__(self):
        text = ""
        self.current_node = self.head
        go = True
        while go:
            text += f"[{self.current_node}] -> "
            if self.current_node.next is None:
                go = False
            else:
                self.current_node = self.current_node.next
        text += '[]'
        return text

    def __iter__(self):
        self.current_node = self.head
        if self.head is None:
            self.head = "EMPTY"

        return self

    def __next__(self):
        if self.current_node is None:
            raise StopIteration

        else:
            previous_node = self.current_node
            self.current_node = self.current_node.next
            return previous_node

    def reset(self):
        self.current_node = self.head

    def add_scene(self, scene_data):
        # Maybe add a scene name variable, to store data in a dict, and so we can reference by specific scene name
        if self.head is None:
            new_scene = Scene(scene_data)
            self.head = new_scene
            self.current_node = self.head
            self.tail = self.head
        else:
            self.tail.next = Scene(scene_data)
            self.tail = self.tail.next


if __name__ == "__main__":
    # Should the scene objects just hold display IDs and we have a separate function to create and display the display?

    # Create scene map object
    intro = SceneMap()

    # Sample Data
    data = ['#001', '#002', '#003', '#004']
    # OR
    key_data = {'#001': [], '#002': [], '#003': [], '#004': []}

    # Use data to fill in scene map
    for entry in data:
        intro.add_scene(entry)

    # Print Status to Screen
    print(f"\nHead: {intro.head} \nCurrent: {intro.current_node}\n")

    # Iterate through scene map
    for s in intro:
        print(s)

    # Print Scene map string representation
    print('')
    print(intro)
