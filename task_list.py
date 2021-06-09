import os
import time

import json

"""
Program: Task List
Author: rickyg3
Date: 06/08/2021
"""


class Task:
    def __init__(self, task_name, task_description="", task_id="0"):
        self.id = task_id
        self.name = task_name
        self.description = task_description

    def __str__(self):
        text = f"[{self.id}] {self.name}: {self.description}"
        return text


class TaskList:
    CURRENT_ID = 0

    def __init__(self, list_name, list_description="", list_id="0"):
        self.id = list_id
        self.name = list_name
        self.description = list_description
        self.tasks = []

    def __str__(self):
        text = f"[{self.id}] {self.name}: {self.description}"
        return text

    def print_task_list(self):
        text = ""
        for task in self.tasks:
            text += f"\n{task}"
        return text

    def add_task(self, new_task_name, new_task_description):
        self.CURRENT_ID += 1
        unique_id = f"{self.name[:3].upper()}{self.CURRENT_ID:03}"
        self.tasks.append(Task(new_task_name, new_task_description, unique_id))


class TaskManager:
    CURRENT_ID = 0

    def __init__(self, base_id=0, base_name="default"):
        self.active_id = base_id
        self.active_name = base_name
        self.active_list = None
        self.lists = {}

    def __str__(self):
        text = f""
        return text

    def print_current(self, target_list=None):
        if target_list is None:
            target_list = self.active_list

        print(f"[{target_list.id}] {target_list.name}: ")
        for task in target_list.tasks:
            print(f"\t{task}")

    def create_list(self, new_list_name, new_list_description):
        self.CURRENT_ID += 1
        # unique_list_id = f"{new_list_name[:3].upper()}{self.CURRENT_ID:03}"

        new_list = TaskList(new_list_name, new_list_description, f"{self.CURRENT_ID:03}")  # unique_list_id)

        self.active_id = new_list.id
        self.active_name = new_list.name
        self.active_list = new_list

        self.lists[f"{new_list.id}"] = new_list

    def load_list(self, filename):
        loaded_data = {}
        # load in list from json or excel sheet
        with open(filename, 'r+') as in_list:
            pass

        # get the next Id number
        self.CURRENT_ID += 1
        # unique_list_id = f"{loaded_data.get('name')[:2].upper()}{self.CURRENT_ID:03}"
        self.active_id = self.CURRENT_ID  # unique_list_id

        # Create the new list using the data
        new_list = TaskList(loaded_data.get("name"), loaded_data.get("description"), f"{self.CURRENT_ID}")   # unique_list_id)
        new_list.tasks = loaded_data.get("data")

        # update the active list with the newly created lists info
        self.active_name = new_list.name
        self.active_list = new_list
        self.lists[f"{new_list.id}"] = new_list


if __name__ == "__main__":
    my_task = TaskManager()
    # print(my_task.active_name)
    # print(my_task.active_id)
    # print(my_task.active_list)
    # print(my_task.lists)
    print("")

    list_name = "House Chores"
    list_desc = "Things I need to do around the house"
    my_task.create_list(list_name, list_desc)

    # print(my_task.active_name)
    # print(my_task.active_id)
    # print(my_task.active_list)
    # print(my_task.lists)

    my_list = my_task.active_list

    task_name = "Trash"
    task_desc = "Take out the fookin trash m9"
    my_list.add_task(task_name, task_desc)

    my_list.add_task("Lazy1", "you lazy son of a gun")

    my_list.add_task("LAzy2", "Get to getting on lmao")

    # display_list = [str(task) for task in my_list.tasks]

    my_task.print_current()

    # for item in my_list.tasks:
    #     print(f"{item}")



    # t_name = "trash"
    # t_desc = "Take out the trash"
    # t_id = 2
    # t1 = Task(t_name, t_desc, t_id)
    #
    # print(t1)
