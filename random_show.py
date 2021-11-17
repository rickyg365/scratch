

bts_members = {
    "RM": "Kim Namjoon",
    "Jin": "Kim Seokjin",
    "Suga": "Min Yoongi",
    "J-Hope": "Jung Hoseok",
    "Jimin": "Park Jimin",
    "V": "Kim Taehyung",
    "JK": "Jung Jungkook"
}

print(bts_members["RM"])


class Dog:
    # This is a function that runs the first time you create and object
    def __init__(self, input_name, input_type):
        self.name = input_name
        self.type = input_type

    # This function returns a value whenever the str()
    def __str__(self):
        text = f"{self.name} {self.type}]"
        return text


# Creating
dog1 = Dog("Lala", "German shepard")

dog2 = Dog("Olive", "Cuban Havanese")

dog3 = Dog("Planet", "Pug")

print(dog1)
# print(dog2)
# print(dog3)
