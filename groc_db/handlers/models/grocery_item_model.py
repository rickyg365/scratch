import os

from typing import List, Optional
from dataclasses import dataclass, field

# Typing is for hints, dataclass does not enforce

# Sqlite3 Type Mapping

grocery_model = {
    "id": "integer",
    "name": "text",
    "description": "text",
    "brand": "text",
    "tags": "text"
}

active_model = {
    "id": "integer",
    "name": "text",
    "description": "text",
    "brand": "text",
    "tags": "text",
    "store": "text",
    "price": "integer",
    "quantity": "integer",
    "quantity_unit": "text"
}

# Python Object

@dataclass
class GroceryItem:
    id: int
    name: str
    description: str
    brand: str = field(default="")
    tags: List[str] = field(default_factory=list)

    def raw_data(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "brand": self.brand,
            "tags": self.tags
        }


@dataclass
class ActiveItem(GroceryItem):
    store: Optional[str] = "???"
    price: float = 0.00
    quantity: int = 1
    quantity_unit: str = "of"

    def raw_data(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "brand": self.brand,
            "tags": self.tags,
            "store": self.store,
            "price": self.price,
            "quantity": self.quantity,
            "quantity_unit": self.quantity_unit
        }

# Table types

ITEMTABLES = {
    "main": {
        "object": GroceryItem, 
        "model": grocery_model, 
        "ref": "id"
    },
    "current": {
        "object": ActiveItem, 
        "model": active_model, 
        "ref": "id"
    }
}


# Sample Data
grocery_data = {
    "id": 0,
    "name": "str",
    "description": "str",
    "brand": "str",
    "tags": ["str1", "str2"]
}

active_data = {
    "id": 0,
    "name": "str",
    "description": "str",
    "brand": "str",
    "tags": ["str1", "str2"],
    "price": 10.00,
    "store": "str",
    "quantity": 1,
    "quantity_unit": "str",
}

def main():
    return 1
    

if __name__ == "__main__":
    main()
