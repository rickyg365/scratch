import os
import random


class BaseHandler:
    def __init__(self, filename="blank.txt", valid_items=None, defaults=None) -> None:
        if defaults is None:
            defaults = [
                "1",
                "2",
                "3"
            ]
        self.items = []
        self.defaults = defaults

        self.valid_triggers = valid_items

        self.file = filename

    def __str__(self) -> str:
        txt = f"{self.items}"
        return txt

    def read_file(self):
        try:
            with open(self.file, 'r+') as innie:
                for line in innie:
                    parsed_line = line.strip()
                    if parsed_line in self.items:
                        continue
                    self.items.append(parsed_line)
        except FileNotFoundError:
            with open(self.file, 'a+') as outtie:
                default_file = ""
                for item in self.defaults:
                    default_file += f"{item}\n"    
                
                outtie.write(default_file)
            self.read_file()
    
    def update_list(self):
        with open(self.file, 'r') as innie:
            for line in innie:
                parsed_line = line.strip()
                if parsed_line in self.items:
                    continue
                self.items.append(parsed_line)

    def add_item(self, new_item):
        if new_item in self.items:
            print("Already added")
            return False

        self.items.append(new_item)
        return True

    def remove_item(self, chosen_item):
        if chosen_item in self.items:
            self.items.remove(chosen_item)
            return True
        print("Item not in items...")
        return False

    def save(self):
        """ Save current state of greetings """
        with open(self.file, 'w') as outtie:
            output_file=""
            for item in self.items:
                output_file += f"{item}\n"
            outtie.write(output_file)
        
        # Update objects state
        self.update_list()
        

    def random(self):
        r = random.randint(0, len(self.items)-1)
        return self.items[r]

    
class FarewellHandler(BaseHandler):
    DEFAULT_FAREWELLS = [
        "Bye",
        "Farewell",
        "Adios",
        "Fuck off"
    ]
    VALID = [
        "bye",
        "later",
        "see ya"
    ]
    def __init__(self, filename="farewells.txt") -> None:
        super().__init__(filename=filename, valid_items=self.VALID, defaults=self.DEFAULT_FAREWELLS)
        self.read_file()


class GreetingHandler(BaseHandler):
    DEFAULT_GREETINGS = [
        "Hello",
        "Salutations",
        "Greetings",
        "What's up"
    ]
    VALID = [
        "hi",
        "hey",
        "hello",
        "whats up"
    ]
    def __init__(self, filename="greetings.txt") -> None:
        super().__init__(filename=filename, valid_items=self.VALID, defaults=self.DEFAULT_GREETINGS)
        self.read_file()


def main():
    greeter = GreetingHandler()
    print(greeter)

    byer = FarewellHandler()
    print(byer)


if __name__ == "__main__":
    main()


# class BaseHandler:
#     def __init__(self, filename="blank.txt", defaults=None) -> None:
#         if defaults is None:
#             defaults = [
#                 "1",
#                 "2",
#                 "3"
#             ]
#         self.items = []
#         self.defaults = defaults

#         self.file = filename

#     def __str__(self) -> str:
#         txt = f"{self.items}"
#         return txt

#     def read_file(self):
#         try:
#             with open(self.file, 'r+') as innie:
#                 for line in innie:
#                     parsed_line = line.strip()
#                     if parsed_line in self.items:
#                         continue
#                     self.items.append(parsed_line)
#         except FileNotFoundError:
#             with open(self.file, 'a+') as outtie:
#                 default_file = ""
#                 for item in self.defaults:
#                     default_file += f"{item}\n"    
                
#                 outtie.write(default_file)
#             self.read_file()
    
#     def update_list(self):
#         with open(self.file, 'r') as innie:
#             for line in innie:
#                 parsed_line = line.strip()
#                 if parsed_line in self.items:
#                     continue
#                 self.items.append(parsed_line)

#     def add_item(self, new_item, error_msg):
#         if new_item in self.items:
#             print("Already added")
#             return False

#         self.items.append(new_item)
#         return True

#     def remove_item(self, chosen_item, error_msg):
#         if chosen_item in self.items:
#             self.items.remove(chosen_item)
#             return True
#         print("Item not in items...")
#         return False

#     def save(self):
#         """ Save current state of greetings """
#         with open(self.file, 'w') as outtie:
#             output_file=""
#             for item in self.items:
#                 output_file += f"{item}\n"
#             outtie.write(output_file)
        
#         # Update objects state
#         self.update_list()

#     def random(self):
#         r = random.randint(0, len(self.items)-1)
#         return self.items[r]

  
# class GreetingHandler:
#     DEFAULT_GREETINGS = [
#         "Hi",
#         "Hello",
#         "Greetings",
#         "Salutations"
#     ]

#     def __init__(self, filename="greetings.txt") -> None:
#         self.greetings = []
#         self.file = filename
#         self.read_file()

#     def __str__(self) -> str:
#         txt = f"{self.greetings}"
#         return txt

#     def read_file(self):
#         try:
#             with open(self.file, 'r+') as innie:
#                 for line in innie:
#                     parsed_line = line.strip()
#                     if parsed_line in self.greetings:
#                         continue
#                     self.greetings.append(parsed_line)
#         except FileNotFoundError:
#             with open(self.file, 'a+') as outtie:
#                 default_file = ""
#                 for item in self.DEFAULT_GREETINGS:
#                     default_file += f"{item}\n"    
                
#                 outtie.write(default_file)
#             self.read_file()
    
#     def update_list(self):
#         with open(self.file, 'r') as innie:
#             for line in innie:
#                 parsed_line = line.strip()
#                 if parsed_line in self.greetings:
#                     continue
#                 self.greetings.append(parsed_line)

#     def add_greeting(self, new_greeting):
#         if new_greeting in self.greetings:
#             print("Already greeting")
#             return False

#         self.greetings.append(new_greeting)
#         return True

#     def remove_greeting(self, chosen_greeting):
#         if chosen_greeting in self.greetings:
#             self.greetings.remove(chosen_greeting)
#             return True
#         print("Greeting not in greetings...")
#         return False

#     def save(self):
#         """ Save current state of greetings """
#         with open(self.file, 'w') as outtie:
#             output_file=""
#             for greeting in self.greetings:
#                 output_file += f"{greeting}\n"
#             outtie.write(output_file)
        
#         # Update objects state
#         self.update_list()

#     def random(self):
#         r = random.randint(0, len(self.greetings)-1)
#         return self.greetings[r]

