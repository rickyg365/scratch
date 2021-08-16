import os
import random
import time


def clear_screen():
    os.system("cls")


def process_time(raw_seconds):
    minutes = raw_seconds // 60
    seconds = (raw_seconds - 60 * minutes)

    return minutes, seconds


def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        elapsed_time = end_time - start_time
        print(f"{elapsed_time:.2f} seconds")
        # Process raw Time
        minute, sec = process_time(elapsed_time)

        if minute < 1:
            print(f"{sec:02.2f} seconds")
        else:
            print(f"{minute:.0f} minutes {sec:02.2f} seconds")

        return result
    return wrapper


@time_it
class EmailTemplate:
    # Sample Database
    GREETING = [
        "Good Morning",
        "Hello",
        "Dear",
        "Hey!"
    ]

    OPENER = [
        "I hope you're having a wonderful day!",
        "I hope this email finds you well"
    ]

    CLOSER = [
        "I look forward to hearing from you soon.",
        "I hope to hear from you soon.",
        "Thank you, for your time."
    ]

    SIGNATURE = [
        "Best Wishes,",
        "Yours Sincerely,",
        "Best,",
        "Cheers!",
        "Wishing you the best,"
    ]

    # List Sizes
    GREETING_MAX = len(GREETING)
    OPENER_MAX = len(OPENER)
    CLOSER_MAX = len(CLOSER)
    SIGNATURE_MAX = len(SIGNATURE)

    def __init__(self, recipient_name, sign_name, recipient_title="Mx", body_text="", relation=""):
        self.name = recipient_name
        self.title = recipient_title
        self.sign_name = sign_name
        self.body = body_text
        self.relation = relation

        self.greeting = ""
        self.opener = ""
        # Add self.introduction   i.e. My name is ____ im in your ____ class.
        self.closer = ""
        self.signature = ""

        self.randomize()

    def __str__(self):
        text = f"""
{self.greeting} {self.title}.{self.name},

    {self.opener} {self.body}
    {self.closer}
                                        {self.signature} {self.sign_name}
"""

        return text

    def select_greeting(self, restriction=0):
        r = random.randint(0, self.GREETING_MAX - 1)
        self.greeting = self.GREETING[r]

    def select_opener(self):
        r = random.randint(0, self.OPENER_MAX - 1)
        self.opener = self.OPENER[r]

    def select_closer(self):
        r = random.randint(0, self.CLOSER_MAX - 1)
        self.closer = self.CLOSER[r]

    def select_signature(self):
        r = random.randint(0, self.SIGNATURE_MAX - 1)
        self.signature = self.SIGNATURE[r]

    def randomize(self):
        self.select_greeting()
        self.select_opener()
        self.select_closer()
        self.select_signature()


if __name__ == "__main__":

    my_body = ""  # input("Type your body here:\n")
    clear_screen()
    time.sleep(95)

    my_email = EmailTemplate(recipient_name="Prof_name",
                             sign_name="RG",
                             recipient_title="Dr",
                             body_text=my_body)

    print(my_email)