# raw_item_data = {
#     "id": "int",
#     "name": "str",
#     "description": "str",
#     "brand": "str",
#     "tags": "str",
# }


# raw_active_item = {
#     "id": "int",
#     "name": "str",
#     "description": "str",
#     "brand": "str",
#     "tags": "str",
#     "price": "float",
#     "store": "str",
#     "quantity": "int",
#     "quantity_unit": "str",
# }

grocery_item = {
    "item_id": "key",
    "name": "key",
    "description": "key",
    "brand": "key",
    "tags": "tag1 tag2 tag3"
}

active_item = {
    **grocery_item,
    "store": "key",
    "price": "key",
    "quantity": "key",
    "quantity_unit": "key"
}

recipe = {
    "recipe_id": "key",
    "name": "key",
    "description": "key",
    "ingredients": "item_id item_id",
    "estimated_time": "key",
    "instructions": "key"
}