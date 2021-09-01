"""
Program: Flatten nested list/dict for printing
Author: Rickyg3
Date: 08/28/21
"""


def flatten_print(raw_obj, tab_index=0, text_to_print=""):

    """   Flattens a bunch of nested lists and dicts into a nice printable string   """

    # Variables
    obj_type = type(raw_obj)
    tab_space = tab_index * '    '

    # Conditions
    is_dict = obj_type is dict
    is_list = obj_type is list

    # Handle Dictionaries
    if is_dict:
        # iterate through dict
        for k, v in raw_obj.items():
            # flatten item if list or dict
            if type(v) is list or type(v) is dict:
                text_to_print += f"\n\n{tab_space}{k}: "
                text_to_print += flatten_print(v, tab_index+1)
            # add to string if not
            else:
                text_to_print += f"\n{tab_space}{k}: {v}"

    # Handle Lists
    if is_list:
        # iterate through list
        for item in raw_obj:
            # flatten item if list or dict
            if type(item) is list or type(item) is dict:
                text_to_print += '\n'
                text_to_print += flatten_print(item, tab_index+1)
            # add to string if not
            else:
                text_to_print += f"\n{tab_space}{item}"

    # Everything Else
    if not is_dict and not is_list:
        # add to string
        text_to_print += f"\n{tab_space}{raw_obj}"

    return text_to_print


def flatten_list(input_list):
    output_list = []
    for item in input_list:
        if type(item) is list:
            output_list.append(flatten_list(item))
        else:
            output_list.append(item)

    return output_list


def flatten_dict(input_dictionary, prefix=''):
    output_dictionary = {}

    for k, v in input_dictionary.items():
        new_key = f"{prefix}_{k}"
        if prefix == '':
            new_key = k
        if type(v) is dict:
            output_dictionary[new_key] = flatten_dict(v, prefix=new_key)

        else:
            output_dictionary[new_key] = v

    return output_dictionary


def flatten_list_dict(input_list, key_prefix=''):
    output_dict = {}
    for index, item in enumerate(input_list):
        output_dict[f"{key_prefix}{index+1:02.0f}"] = item

    return output_dict


def flatten_dict_list(input_dict):
    output_list = []

    for key, value in input_dict.items():
        new_item = (key, value)
        output_list.append(new_item)

    return output_list


def flatten_data(raw_obj, database_obj=None, cycles=5):
    """   Flattens a bunch of nested lists and dicts into a nice flat list   """

    # Variables
    obj_type = type(raw_obj)

    # Conditions
    is_dict = obj_type is dict
    is_list = obj_type is list

    # Handle Dictionaries
    if is_dict:
        if database_obj is None:
            database_obj = []
        # iterate through dict
        new_dict = flatten_dict(raw_obj)
        for item in new_dict.values():
            database_obj.append(item)

        # for k, v in raw_obj.items():
        #     # flatten item if list or dict
        #     if type(v) is list:
        #         new_list = flatten_list(v)
        #         raw_obj[k] = new_list
        #     if type(v) is dict:
        #         new_dict = flatten_dict(v)
        #         raw_obj[k] = new_dict
        #     # add to string if not
        #     else:
        #         raw_obj[k] = v

    if is_list:
        if database_obj is None:
            database_obj = []
        # iterate through list
        database_obj = flatten_list(raw_obj)
        # for item in raw_obj:
        #     # flatten item if list or dict
        #     if type(item) is list or type(item) is dict:
        #         text_to_print += '\n'
        #         text_to_print += flatten_print(item, tab_index + 1)
        #     # add to string if not
        #     else:
        #         text_to_print += f"\n{tab_space}{item}"

    # Everything Else
    if not is_dict and not is_list:
        return database_obj

    return database_obj


if __name__ == "__main__":
    # dictionaries for testing
    sample_dict = {
        'Community Amenities': [
            ['Laundry Facilities', 'Gated', '24 Hour Availability', 'Property Manager on Site'],
            ['Dishwasher', 'High Speed Internet Access', 'Fireplace', 'Ceiling Fans'],
            ['Laundry Facilities', 'Maintenance on site', 'Property Manager on Site', '24 Hour Availability', 'Gated'],
            ['High Speed Internet Access', 'Ceiling Fans', 'Smoke Free', 'Fireplace', 'Dishwasher', 'Dining Room', 'Vaulted Ceiling', 'Wet Bar', 'Balcony']
        ],
        'Apartment Features': [
            ['Laundry Facilities', 'Gated', '24 Hour Availability', 'Property Manager on Site'],
            ['Dishwasher', 'High Speed Internet Access', 'Fireplace', 'Ceiling Fans'],
            ['Laundry Facilities', 'Maintenance on site', 'Property Manager on Site', '24 Hour Availability', 'Gated'],
            ['High Speed Internet Access', 'Ceiling Fans', 'Smoke Free', 'Fireplace', 'Dishwasher', 'Dining Room', 'Vaulted Ceiling', 'Wet Bar', 'Balcony']
        ]
    }
    hand_made = {
        'id': 1,
        'name': 'bulbasaur',
        'type': 'grass',
        'moves': [
            'tackle',
            'growl',
            'leech seed',
            'razor leaf',
        ],
        'stats': {
            'hp': 30,
            'atk': 10,
            'def': 11,
            'sp atk': 9,
            'sp def': 10,
            'speed': 8
        },
        'shiny': False

    }

    # sample use case
    flattened = flatten_print(hand_made)

    print(flattened)
