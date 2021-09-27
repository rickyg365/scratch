import os

import json
import random
import datetime

import copy
"""
Program: Date randomizer [ version 1.0 ]
Author: Rickyg3
Date: 09/12/21
"""

""" 
Game Plan:
    
    THis file can be like the api and we can build an actual program that uses these functions in a separate file
    
    Write one were it is a class and another where it is just a file
    
    add date ideas to a data structure,
    2 parts, 
    1. the key to identify the date activity 
    2. the other part that stores any info for that activity {name/key, location, schedule, transport, cost, itinerary}
    
    save this to a file (json)
    
To Do:
    add a check completed func, so that we don't end up repeating all of the same activities
    update the load procedure to reflect the new saving of completed data
    
"""

"""
Sample Json

[
    {
        name: "",
        location: "",
        schedule: "",
        transport: "",
        cost: "",
        itinerary: ""
    },
    {
        name: "",
        location: "",
        schedule: "",
        transport: "",
        cost: "",
        itinerary: ""
    },
    {
        name: "",
        location: "",
        schedule: "",
        transport: "",
        cost: "",
        itinerary: ""
    },
    {
        name: "",
        location: "",
        schedule: "",
        transport: "",
        cost: "",
        itinerary: ""
    }
]

"""


# Classes
class DateManager:
    def __init__(self, file_path="dates.json", completed_file_path="visited_dates.json"):
        # Attributes
        self.current_index = 0
        self.total_size = 0
        self.current_size = 0

        # Files
        self.file_path = file_path
        self.completed_path = completed_file_path

        # Data
        self.keys = []
        self.current_keys = []
        self.data = {}
        self.new_dates = {}
        self.completed_data = {}

        # Get Running
        self.load_dates()
        self.check_completed()

        self.set_total_size()
        self.set_current_size()

    def __str__(self):
        if self.is_empty():
            return f"{self.file_path} is empty"

        text = f"Dates: {self.total_size} \nNew: {self.current_size} \nCompleted:{len(self.completed_data)}"
        return text

    def load_dates(self):
        try:
            with open(self.file_path, 'r') as input_file:
                read_data = json.load(input_file)  # list of dict

                # Loop through data and set up data
                for obj in read_data:
                    key = obj['name']

                    self.keys.append(key)
                    self.data[key] = obj

        except FileNotFoundError:
            print(f"\nFile not found: {self.file_path} created!\n")

            # with open(self.file_path, 'w') as write_file:
            #     print("\n[ file created ]")
            self.save_dates()

        except json.decoder.JSONDecodeError:
            print("\n[ no data found ]\n")

    def save_dates(self):
        # check if main list is empty
        if self.is_empty():
            return

        # Save main data
        json_list = []
        for item in self.data.values():
            json_list.append(item)

        with open(self.file_path, 'w') as out_file:
            json.dump(json_list, out_file, indent=4)

        # save completed to json

        if self.current_size != 0:
            done_json_list = []

            for item in self.completed_data.values():
                done_json_list.append(item)

            with open(self.completed_path, 'w') as complete_file:
                json.dump(done_json_list, complete_file, indent=4)

    def set_total_size(self):
        self.total_size = len(self.data)

    def set_current_size(self):
        """ Returns number of new date activities """
        self.current_size = len(self.new_dates)

    def update_keys(self):
        return

    def is_empty(self):
        # Update size
        self.set_total_size()
        self.set_current_size()

        if self.total_size == 0:
            return True

        return False

    def add_activity(self, date_data):
        new_key = date_data['name']

        self.data[new_key] = date_data

    def edit_activity(self, date_name, date_attr, new_value):
        if self.is_empty():
            return

        try:
            self.data[date_name][date_attr] = new_value

        except Exception as e:
            print(e)

    def complete_activity(self, date_name):
        """
        completed data dict is almost identical except it has a list of date time objs,
        that mark when that activity was done
        """
        if self.is_empty():
            return

        ''' 
        was gonna make a copy of the dict but honestly its kind of better if they do point to the same obj 
        that way one edit can fix both, especially since if I edit the date I would want to update both 
        '''
        # new_copy = copy.deepcopy(self.data[date_name])

        self.completed_data[date_name] = self.data[date_name]

        # Format time
        current_time = datetime.datetime.now()
        current_time.strftime("%b %d %Y %H:%M:%S")

        self.completed_data[date_name]['date'] = str(current_time)

        self.new_dates.pop(date_name, 'No Key found')

    def check_completed(self):
        if self.is_empty():
            return

        self.current_keys = []
        for k, v in self.data.items():
            # Need first condition to be true in order for the second not to give error so we leave it like this
            if k in self.completed_data.keys() and v == self.completed_data[k]:
                continue

            # if (k, v) in self.completed_data.items():
            #     continue
            self.current_keys.append(k)
            self.new_dates[k] = v

        return

    def select_random(self):
        # Make sure variables are updated
        self.check_completed()
        self.set_current_size()

        random_index = random.randint(0, self.current_size - 1)

        random_key = self.keys[random_index]

        return self.new_dates[random_key]


if __name__ == "__main__":
    date_selector = DateManager('sample_dates.json')

    # sample_data = {
    #     "movie theater": {
    #         "name": "movie theater",
    #         "location": "berkeley",
    #         "schedule": "NaN",
    #         "transport": "NaN",
    #         "cost": 15,
    #         "itinerary": "NaN"
    #     },
    #     "tail gate": {
    #         "name": "tail gate",
    #         "location": "Oklahoma",
    #         "schedule": "NaN",
    #         "transport": "NaN",
    #         "cost": 20,
    #         "itinerary": "NaN"
    #     },
    #     "museum": {
    #         "name": "museum",
    #         "location": "seattle",
    #         "schedule": "NaN",
    #         "transport": "NaN",
    #         "cost": 0,
    #         "itinerary": "NaN"
    #     }
    # }
    #
    # date_idea = {
    #     "name": "new restaurant",
    #     "location": "tokyo",
    #     "schedule": "NaN",
    #     "transport": "NaN",
    #     "cost": 80,
    #     "itinerary": "NaN"
    # }
    #
    # date_selector.data = sample_data
    # date_selector.add_activity(date_idea)
    #
    # date_selector.save_dates()

    print(date_selector)

    chosen_activity = date_selector.select_random()
    print(chosen_activity)
    # print(date_selector.data)
    # print(f"{date_selector.file_path}")

    date_selector.complete_activity(chosen_activity['name'])
    date_selector.save_dates()

    print(date_selector)

    # print(date_selector.completed_data)
    # print(date_selector.new_dates)
