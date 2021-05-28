import os
import time
import datetime


def my_timer(random_func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        random_func(*args, **kwargs)
        elapsed_time = time.perf_counter() - start_time
        print(f"{elapsed_time} sec")
    return wrapper


@my_timer
def my_func():
    time.sleep(3)


def title_box(random_func):
    def wrapper(*args, **kwargs):
        text = random_func(*args, **kwargs)
        length = len(text)
        print(f",-{length*'-'}-.")
        print(f"| {text} |")
        print(f"'-{length*'-'}-'")
    return wrapper


def star_box(random_func):
    def wrapper(*args, **kwargs):
        text = random_func(*args, **kwargs)
        length = len(text)
        print(f"**{length*'*'}**")
        print(f"| {text} |")
        print(f"**{length*'*'}**")
    return wrapper


@my_timer
@title_box
def insert_title(title_text=""):
    return title_text.title()


@my_timer
@star_box
def dialogue(dialogue_text: str) -> str:
    return dialogue_text.capitalize()


if __name__ == "__main__":
    insert_title("pokemon")
    dialogue("hi pokemon")

