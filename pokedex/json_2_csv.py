import csv
import json


def csv_json(csv_file, json_file):
    data = {}

    with open(csv_file, encoding='utf-8') as csvf:
        csvreader = csv.DictReader(csvf)

        for rows in csvreader:
            key = rows['#']
            data[key] = rows

    with open(json_file, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))


if __name__ == "__main__":
    csv_infile = "Pokemon.csv"
    json_infile = 'new_json.json'

    csv_json(csv_infile, json_infile)
