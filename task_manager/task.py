import os
import time

import re
import logging


class Task:
    def __init__(self, task_name, task_detail, task_tags=None):

        self.name = task_name
        self.show_details = False
        self.details = task_detail
        if task_tags is None:
            task_tags = []
        self.tags = task_tags

        self.status = False

    def __str__(self):
        text = f"{self.name}\t"
        for tag in self.tags:
            text += f"[{tag}] "

        if self.show_details:
            text += f"\n     {self.details}"

        return text


# class User:
#     def __init__(self):
#         pass
#
#     def __str__(self):
#         text = f""
#         return text


class TaskList:
    def __init__(self, list_name):
        self.name = list_name
        # maybe make into dict
        self.tasks = {}

    def __str__(self):
        title = f"{self.name}'s task list"
        bar = f"-{len(self.name) * '-'}----------------------"
        # print(len(bar))

        text = f"""
{bar}
{title.center(len(bar),' ')}
{bar}
"""
        for task in self.tasks.values():
            if task.status:
                text += f"\n[x]: {task}\n"
            else:
                text += f"\n[ ]: {task}\n"

        return text

    def add_task(self, new_task_name, new_task_details, new_task_tags):
        new_task = Task(new_task_name, new_task_details, new_task_tags)
        # self.tasks.append(new_task)
        self.tasks[new_task_name] = new_task

    def task_search(self, task_name):
        ...

    def mark_task(self, task_name):
        # Search for task
        # if self.task_search(task_name):
        #   self.tasks[task_name].change_status
        status = self.tasks[task_name].status
        if status:
            self.tasks[task_name].status = False
        else:
            self.tasks[task_name].status = True


if __name__ == "__main__":
    # random_task = Task("Go Clean", "Clean your room", ['home', 'personal'])
    # print(random_task)

    my_list = TaskList('Mr.Fredrickson')
    my_list.add_task('Apply for Jobs', 'Finish applying to jobs', ['personal', 'work'])

    my_list.add_task('Go to School', 'Go back to school', ['personal', 'school'])

    my_list.add_task('Organize closet', 'Finish organizing closet', ['personal', 'home'])

    my_list.mark_task('Apply for Jobs')

    my_list.mark_task('Organize closet')

    print(my_list)
