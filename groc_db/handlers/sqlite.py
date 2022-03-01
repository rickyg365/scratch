import os
import sqlite3

from typing import List, Dict

from models.grocery_item_model import ActiveItem, GroceryItem, ITEMTABLES

"""

"""

# Helping Functions

def model_text(data_model:Dict[str, str]) -> str:
    """ Convert Data Model Template into Sqlite3 Language """ 
    # Split tuple into sqlite format
    parsing_function = lambda x: f"            {x[0]} {x[1]}"

    # Apply format to every key, val pair and Join with seperater
    return ",\n".join(map(parsing_function, data_model.items()))

def parse_insert_data(data_object, data_model:Dict[str, str]):
    final_key = []
    final_obj = {}

    # data_object = data_object.raw_data()

    for data_key, data_type in data_model.items():
        # Get current value
        data_value = data_object.get(data_key)

        # Create Insert Key
        final_key.append(f":{data_key}")

        # This is for general parsing but maybe define specific parsing files and move them into the Object Model File
        if data_type == 'integer':
            final_obj[data_key] = int(data_value)
        else:
            final_obj[data_key] = f"{data_value}"

    return ", ".join(final_key), final_obj


# Objects 

class Sqlite3Database:
    def __init__(self, table_data=None, database_path="data/new_sqlite_db.db"):
        self.conn = sqlite3.connect(database_path)
        self.cur = self.conn.cursor()

        self.tables = table_data

        self.main_table = self.create_table("main")
        self.current_table = self.create_table("current")
    
    def __str__(self) -> str:
        txt = ""
        return txt
    
    def create_table(self, table_name="main"):
        data_model = self.tables[table_name]['model']
        
        self.cur.execute(f"""CREATE TABLE IF NOT EXISTS {table_name} (
{model_text(data_model)}
)""")

    def insert_data(self, data_object, table_name):
        # Raw Data vs python obj
        data_model = self.tables[table_name]['model'] 
        data_insert_key, data_insert_obj = parse_insert_data(data_object.raw_data(), data_model)
        
        with self.conn:
            self.cur.execute(f"INSERT INTO {table_name} VALUES ({data_insert_key})",
            data_insert_obj)

    def get_all(self, table_name) -> List[object]:
        data_obj_name = self.tables[table_name]['object']
        # Connect to table, and select all
        self.cur.execute(f'select * from {table_name}')
        results = self.cur.fetchall()

        # iterate and add to object list
        objects = []
        for result in results:
            objects.append(data_obj_name(*result))

        return objects
    
    def delete_data_point(self, key, table_name):
        """ """
        ref_attr = self.tables[table_name]["ref"]
        with self.conn:
            self.cur.execute(f'DELETE from {table_name} WHERE {ref_attr}=:key', {'key': key})


if __name__ == "__main__":
    new_db = Sqlite3Database(ITEMTABLES)

    # 2 Tables by Default, Main and Current

    new_db.insert_data(GroceryItem(0, "name1", "desc"), "main")
    new_db.insert_data(ActiveItem(0, "name2", "desc"), "current")

    all_items = new_db.get_all("main")
    curr_items = new_db.get_all("current")

    print(f"All: \n{all_items}")
    print(f"Current: \n{curr_items}")

    new_db.delete_data_point(0, "main")
    new_db.delete_data_point(0, "current")

