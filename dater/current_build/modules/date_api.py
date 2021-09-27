import random
import json
import datetime


def dictionary_print_format(dict_obj, depth=1):
    output_str = ""
    tab = '    '
    for k, v in dict_obj.items():
        if type(v) is dict:
            v = dictionary_print_format(v, depth+1)
        output_str += f"\n{tab*depth}{k}: {v}"

    return output_str


class DateHandler:
    # should we use "./data/dates.json" or "data/dates.json"
    def __init__(self, database_file_path='data/dates.json'):
        # Files
        self.path = database_file_path

        # Attributes
        self.current_index = 0
        self.total_size = 0
        self.total_new_dates = 0

        # Data
        # Keep track of all date keys and new unvisited dates
        self.all_keys = []
        self.new_date_keys = []

        # Keep track of all dates
        self.data = {}
        # For searching by name, like when using the update date method
        self.name_key_dict = {}

        # Get Running
        self.load_data()

        self.get_size()

    def __str__(self):
        text = f"""
\nAll keys: {self.total_size}\n{self.all_keys}
\nNew keys: {self.total_new_dates}\n{self.new_date_keys}
\nAll data {dictionary_print_format(self.data)}
\nName-Key dict {dictionary_print_format(self.name_key_dict)}
\n
"""
        return text

    @staticmethod
    def check_visited(object_to_check):
        if object_to_check['visited'] == 0:
            return False

        return True

    def load_data(self, new_file_path=None):
        """ loads data to working memory """

        if new_file_path is not None:
            self.path = new_file_path

        # Load using self.path
        try:
            with open(self.path, 'r') as input_file:
                read_data = json.load(input_file)  # list of dict

                # Loop through data and set up data
                for index, obj in enumerate(read_data):
                    # choose key for date obj, in this case name, but should I add a unique date identifier?
                    key = f"{index:03.0f}"
                    obj['id'] = key

                    self.all_keys.append(key)
                    self.data[key] = obj

                    # check if visited
                    if not self.check_visited(obj):
                        self.new_date_keys.append(key)

                    # For searching by name, like when using the update date method
                    self.name_key_dict[obj['name']] = key

        except FileNotFoundError:
            # with open(self.path, 'w') as write_file:
            #     print(f"\nFile not found: {self.path} created!\n")
            self.save_data()

        except json.decoder.JSONDecodeError:
            print("\n[ no data found ]\n")

    def save_data(self, new_file_path=None):
        """ saves data in json format """

        if new_file_path is not None:
            self.path = new_file_path

        # check if main list is empty
        if len(self.data.values()) == 0:
            return

        # Save main data
        json_list = []
        for item in self.data.values():
            json_list.append(item)

        with open(self.path, 'w') as out_file:
            json.dump(json_list, out_file, indent=4)

    def sync_data(self):
        """ Reflects any changes to the main data on all secondary data structures """
        self.all_keys.clear()
        self.new_date_keys.clear()
        self.name_key_dict = {}

        for key, obj in self.data.items():
            # choose key for date obj, in this case name, but should I add a unique date identifier?
            self.all_keys.append(key)

            # check if visited
            if not self.check_visited(obj):
                self.new_date_keys.append(key)

            # For searching by name, like when using the update date method
            self.name_key_dict[obj['name']] = key

        self.get_size()

    def get_size(self):
        """ get size of data list """
        self.total_size = len(self.all_keys)
        self.total_new_dates = len(self.new_date_keys)

    def reset_all(self):
        self.all_keys.clear()
        self.new_date_keys.clear()
        # Loop through data and set up data
        for key, obj in self.data.items():
            # choose key for date obj, in this case name, but should I add a unique date identifier?
            self.data[key]['visited'] = 0
            self.all_keys.append(key)
            self.new_date_keys.append(key)

        self.get_size()

    def select_random(self):
        self.get_size()

        try:
            r = random.randint(0, self.total_new_dates-1)

            random_key = self.new_date_keys[r]
            self.data[random_key]['visited'] = 1

            return self.data[random_key]

        except ValueError:
            reset_choice = input("Reset all (y/n): ")

            if reset_choice == 'y':
                self.reset_all()
            else:
                return

    def search_by_name(self, name_to_search):
        """ Add some regex so that we don't need to type the exact name out or something """
        return self.name_key_dict.get(name_to_search, "name error")

    def add_date(self):
        """
        How do we handle date adding?
        1. Custom Date Object

        2. Date data as a dictionary (kinda related to above)

        3. Pass in individual parameters
        add_date(name, cost, location, ...)

        """
        ...

    def edit_date(self, date_key="", attribute_name="", new_value=""):
        # check if attribute is in dict
        if attribute_name in self.data[date_key].keys():
            self.data[date_key][attribute_name] = new_value
        else:
            # this is the case of adding a new attribute for now lets it make it possible
            print("[ Currently unable to add new attributes ]")

        self.sync_data()

    def remove_date(self, date_key):
        del self.data[date_key]

        self.sync_data()


if __name__ == "__main__":
    # Write test here
    data_path = '../data/dates.json'
    dater = DateHandler(data_path)
    print(dater)

    random_date_data = dater.select_random()
    random_date_key = random_date_data['id']
    print(random_date_data)

    dater.edit_date(random_date_key, 'choco', 'The Great Gatsby')
    print(random_date_data)

    # dater.remove_date(random_date_key)

    print(dater)

    # dater.save_data()
