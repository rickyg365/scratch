import os
import random

import time

"""
Algorithm practice
Author: rickyg3
"""


class Node:
    def __init__(self, value=0):
        # Standard DLL variables
        self.value = value
        self.next = None

        # for future implementation of a doubly linked list
        self.prev = None

    def __str__(self):
        text = f"[{self.value}]"
        return text


class LinkedList:
    def __init__(self, starting_node=None):

        if starting_node is None:
            self.size = 0
            self.head = None
        else:
            self.size = 1
            self.head = starting_node
        self.tail = self.head

    def __str__(self):
        text = f""
        start = self.head

        # Column view
        # for i in range(self.size):
        #     text += f"{i}: {start}\n"
        #     if start is None:
        #         print(f"early None in linked list, iteration: {i}")
        #         break
        #     start = start.next
        # if start is None:
        #     text += f"[None]"
        # else:
        #     text += f"values remaining"

        # Other view
        for i in range(self.size):
            # if start == self.head:
            #     text += f"h|{start} -> "
            # elif start == self.tail:
            #     text += f"{start}|t -> "
            # else:
            #     text += f"{start} -> "
            # add node to string
            text += f"{start} -> "

            start = start.next
        # if the value remaining is none add it to the text else there are still some remaining values and something went wrong
        if start is None:
            text += f"[None]"
        else:
            text += f"- values remaining -"
        return text

    def add_node(self, value):
        if self.head is None:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            self.size += 1
        else:
            new_node = Node(value)
            self.tail.next = new_node
            self.tail = new_node
            self.size += 1

    def get(self, index):
        current_node = self.head
        # if index == 0:
        #     return current_node
        #
        # for i in range(index):
        #     next_node = current_node.next
        #     if i == index-1:
        #         return next_node
        #     if next_node:
        #         current_node = next_node
        #     else:
        #         print(f"\nSomething fucked up...\ncurrent node: {current_node}, next node: {next_node}")
        for i in range(self.size):
            next_node = current_node.next
            # return desired value
            if i == index:
                return current_node
            # going out of range handling
            if next_node is None:
                text = f"\nSomething fucked up..."
                text += f"\n{30 * '-'}"
                text += f"\nGet Index: {index} \nLast Node -> {current_node}, index: {i} "
                text += f"\n{30 * '-'}"
                print(text)
                return None
            # Iterate
            current_node = next_node

    def insert(self, index, value):
        # check index
        if index > self.size:
            # just adds it to the end for now
            index = self.size
            print("Index exceeds linked list side")
            # return False

        new_node = Node(value)
        current_node = self.head
        # Case 1: Empty List
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return True
        # Case 2: Replace Head
        if index == 0:
            new_node.next = current_node
            self.head = new_node
            self.size += 1
            return True
        # Case 3: Last Index, adding to the end
        if index == self.size:
            self.tail.next = new_node
            self.tail = new_node
            self.size += 1
            return True
        # Case 4: Everything Else
        for i in range(self.size):
            # When we get to the node before the desired node
            if (i + 1) == index:
                # Old next node
                old_next = current_node.next
                # make old next node the new nodes next
                new_node.next = old_next
                # make the currents node next the new node
                current_node.next = new_node
                self.size += 1
                return True
            # Iterate
            current_node = current_node.next

    def remove(self, index):
        current_node = self.head

        for i in range(self.size):
            # Case 1: Remove Head
            if index == 0:
                self.head = current_node.next
                self.size -= 1
                return True
            # Case 2: Remove Tail
            if i+1 == self.size - 1:
                current_node.next = None
                self.tail = current_node
                self.size -= 1
                return True
            # Case 3: Remove Something in the middle
            if i+1 == index:
                # current node is previous node so this .next will go to the removal.next
                node_to_remove = current_node.next
                current_node.next = node_to_remove.next
                self.size -= 1
                return True
            # Iterate
            current_node = current_node.next

    def remove_random(self, removal_amount):
        current_length = self.size - 1
        error_text = ""
        if removal_amount > self.size:
            # could also choose to just instantly return an empty list here but then we dont get to see the iterations
            error_text = f"ExcessERROR: removal amount changed to {self.size}"
            removal_amount = self.size

        print(f"removing {removal_amount} elements: ")
        for i in range(removal_amount):
            r = random.randint(0, current_length)

            # print(f"\nSize:  {ll.size}\nList: {ll}")
            print('\t' + 92 * '-')
            ll.remove(r)
            print('\t' + f"- removed index: {r} -")
            current_length -= 1

            print('\t' + f"New List: {self.__str__()}")
            # for dramatic effect
            # time.sleep(0.65)
        if error_text != "":
            print('\n' + error_text)

    def generate_random_list(self, list_length=10):
        for i in range(list_length):
            r = random.randint(1, 999)
            self.add_node(r)


if __name__ == "__main__":
    # Choose list length
    length = int(input("Choose Length: "))

    # Create empty list then generate a random list of [length]
    ll = LinkedList()
    ll.generate_random_list(length)

    # Check the get function with the index past the last index just to see everything is working as intended
    val = ll.get(length)
    print(f"\nValue at index {length}: {val}")

    # Display current list
    print(f"\nSize:  {ll.size}\nList: {ll}\n")

    # Remove n elements from the list
    removal_num = int(input("How many elements to remove?: "))
    ll.remove_random(removal_num)

    # Final list status check
    print(f"\nSize:  {ll.size}\nList: {ll}\n")
