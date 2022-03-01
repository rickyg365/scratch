import os


def flatten_list(raw_list, data_list=None):
    if data_list is None:
         data_list = []

    for item in raw_list:
        if type(item) is list:
            flatten_list(item, data_list)
            continue
        data_list.append(item)
    
    return data_list
    

def flatten_dict(raw_dict, data_dict=None, prefix=""):
    if data_dict is None:
        data_dict = {}
    
    for k, v in raw_dict.items():
        if type(v) is dict:
            flatten_dict(v, data_dict, f"{k}")
            continue
        space_char = "" if prefix == "" else "_"
        data_dict[f"{prefix}{space_char}{k}"] = v

    return data_dict





def main():
    sample_list = [
        1,
        2,
        [3,[4,5], 6],
        7,
        [[8, 9], 10]
    ]

    sample_dict = {
        "a": 1,
        "b": {
            "c": 3,
            "d": 4
        },
        "e": 5
    }

    fixed_list = flatten_list(sample_list)
    fixed_dict = flatten_dict(sample_dict)


    print(sample_list)
    print(fixed_list)

    print(sample_dict)
    print(fixed_dict)


if __name__ == "__main__":
    main()
