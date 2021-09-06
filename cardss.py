import random
import pandas as pd


# encoding_type = 'utf-32'
# raw_msg = '\U0001F0CF'
#
# msg = raw_msg.encode().decode()
#
# print("Raw Message: ", raw_msg)
#
# print("Message: ", msg)


def process_raw_card(raw_string):
    new_obj = raw_string.encode('utf-8')

    return new_obj.decode("unicode-escape")


def build_card_database():
    card_suites = [
        'S',
        'C',
        'H',
        'D'
    ]
    suite_range = [
        'A',
        'B',
        'C',
        'D'
    ]

    card_ranks = [
        'A',
        '1',
        '2',
        '3',
        '4',
        '5',
        '6',
        '7',
        '8',
        '9',
        '10',
        'J',
        'Q',
        'K'
    ]
    card_range = [
        '1',
        '2',
        '3',
        '4',
        '5',
        '6',
        '7',
        '8',
        '9',
        'A',
        'B',
        'C',
        'D',
        'E'
    ]

    built_database = {}

    for i in range(len(card_suites)):
        for j in range(len(card_ranks)):
            key = f"{card_suites[i]}{card_ranks[j]}"
            obj = f"\\U0001F0{suite_range[i]}{card_range[j]}"

            built_database[key] = obj

    return built_database


def save_database(output_file, database):
    # Find extension
    valid_ext = [
        'txt',
        'json',
        'csv'
    ]

    file_name, file_ext = output_file.split('.')

    if file_ext not in valid_ext:
        return False

    # Text File
    if file_ext == 'txt':
        with open(output_file, 'w') as out_file:
            for key, value in database.items():
                new_line = f"{key}: {value}\n"
                out_file.write(new_line)

        return True

    # JSON
    if file_ext == 'json':
        ...

    # CSV
    if file_ext == 'csv':
        ...


def load_database(input_file):
    loaded_database = {}

    # Find extension
    valid_ext = [
        'txt',
        'json',
        'csv'
    ]

    file_name, file_ext = input_file.split('.')

    if file_ext not in valid_ext:
        return False

    # Text File
    if file_ext == 'txt':
        with open(input_file, 'r') as in_file:
            for line in in_file:
                key, obj = line.split(':')

                # clean trailing and leading spaces
                key, obj = key.strip(), obj.strip()

                loaded_database[key] = obj

    # JSON
    if file_ext == 'json':
        ...

    # CSV
    if file_ext == 'csv':
        ...

    return loaded_database


if __name__ == "__main__":
    card_data = build_card_database()

    # True if successful save else False
    save_status = save_database('card_dict.txt', card_data)

    new_deck = load_database('card_dict.txt')

    suites = [
        'S',
        'C',
        'H',
        'D'
    ]
    s = random.randint(0, 3)
    r = random.randint(1, 10)

    random_card = f"{suites[s]}{r}"
    random_1 = f"{suites[s]}Q"
    random_2 = f"{suites[s]}K"

    print(process_raw_card(new_deck.get(random_card)), process_raw_card(new_deck.get(random_1)), process_raw_card(new_deck.get(random_2)))

