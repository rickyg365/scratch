import os
from time import sleep

from rich import inspect
from rich.table import Table
from rich.progress import track
from rich.console import Console


# process_data

def func1():
    sleep(1)


def func2():
    sleep(1)


def func3():
    sleep(1)


def func4():
    sleep(1)


if __name__ == "__main__":
    list_of_func = [
        func1,
        func2,
        func3,
        func4
    ]
    tasks = [*list_of_func]

    console = Console()

    with console.status("[bold green]Performing tasks...") as status:
        for _, func in enumerate(list_of_func):
            func()
            console.log(f"task {_} complete")



