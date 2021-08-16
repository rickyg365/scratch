import os


def flatten_list(input_list, ref_list=None):
    # Check for reference list, if none, create empty list
    if ref_list is None:
        ref_list = []

    # Check if items are of type list
    for item in input_list:
        # Flatten, if it is [Recursive step]
        if type(item) is list:
            flatten_list(item, ref_list)

        # Add to reference list, if its not
        else:
            ref_list.append(item)

    return ref_list


def flatten_dict(input_dict, ref_dict=None, prefix="", separator="_"):
    # Check for reference list, if none, create empty list
    if ref_dict is None:
        ref_dict = {}

    # Check if items are of type list
    for key, val in input_dict.items():
        # Flatten, if it is [Recursive step]
        if type(val) is dict:
            flatten_dict(val, ref_dict, prefix=f"{key}{separator}", separator=separator)

        # Add to reference list, if its not
        else:
            ref_dict[f"{prefix}{key}"] = val

    return ref_dict


# class Flat:
#     def __init__(self, base_obj):
#         self.base = base_obj
#         self.result = ""
#
#     def flatten_list(self):
#         return
#
#     def flatten_dict(self):
#         return
#
#     def flatten(self):
#         return


if __name__ == "__main__":
    ...
