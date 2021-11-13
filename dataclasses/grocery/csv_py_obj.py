import os
import pandas as pd

from items import GroceryItem, InventoryItem
from inventory import Inventory, InventoryAnalyzer


def read_csv(csv_filepath="grocery_data.csv") -> dict:
    # groc_df = pd.read_csv(csv_filepath, index_col="item_id")
    # print(groc_df.head())

    new_dict = {}

    with open(csv_filepath, 'r') as csv_file:
        fields = csv_file.readline().strip().split(",")

        for line in csv_file:
            row_items = line.strip().split(",")

            key = row_items[0]
            new_dict[key] = dict(zip(fields, row_items))

    return new_dict


if __name__ == "__main__":
    width, height = os.get_terminal_size()

    file_path = "grocery_data.csv"

    data = read_csv(file_path)

    inventory_list = Inventory()

    for key, item in data.items():
        # for key, val in item.items():
        #     print(f"{key}: {val} {type(val)}")
        processed_item = InventoryItem(**item)
        processed_item.validate_types()
        # prepped_item = raw_item.validate_types()
        inventory_list.add_item(processed_item)

    print(inventory_list)

    analyzer = InventoryAnalyzer()
    report = analyzer.summary_bar(inventory_list(), threshold=0.8, console_width=width//3, sep=f"\n")
    report_no_bar = analyzer.summary(inventory_list(), threshold=0.8)

    print(f"Report: \n{width*'-'}\n", report)
    print(f"Report [no bar]: \n{width*'-'}\n", report_no_bar)
