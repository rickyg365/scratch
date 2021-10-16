import os


"""
This one handels extracting the data from ecxel/csv and making it into data structures and python object
also does export 
"""


class Good:
    def __init__(self, name="", price="", brand="", flavor="",
                 unit_name="", unit_size=0, date_purchased="", date_finished=""):
        self.name = name
        self.price = price
        self.brand = brand
        self.flavor = flavor

        self.unit_name = unit_name
        self.unit_size = unit_size
        self.date_purchased = date_purchased
        self.date_finished = date_finished

    def __str__(self):
        text = f"[{self.name}]  ${self.price}"
        text += f""
        return text


class GroceryManager:
    def __init__(self):
        ...

    def __str__(self):
        text = f""
        return text

    def load_goods(self, filepath):
        """ load goods from csv or excel file"""
        ...

    def save_goods(self, filepath):
        """ saves goods to csv or excel file"""
        ...

    def export_goods(self, filetype):
        """ saves goods to specified filetype """
        ...



if __name__ == "__main__":
    ...
