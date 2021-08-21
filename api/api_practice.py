import os
import json
import requests
from flatten import *

"""
Program: practice api
Author: rickyg3
Date: 08/06/2021
"""

"""
200	OK	
    The requested action was successful.
201	Created	
    A new resource was created.
202	Accepted	
    The request was received, but no modification has been made yet.
204	No Content	
    The request was successful, but the response has no content.
400	Bad Request	
    The request was malformed.
401	Unauthorized	
    The client is not authorized to perform the requested action.
404	Not Found	
    The requested resource was not found.
415	Unsupported Media Type	
    The request data format is not supported by the server.
422	Unprocessable Entity	
    The request data was properly formatted but contained invalid or missing data.
500	Internal Server Error	
    The server threw an error when processing the request.


Code range	Category
2xx	Successful operation
3xx	Redirection
4xx	Client error
5xx	Server error

"""


base_url = f"https://pokeapi.co/api/v2/"

# for pokemon
pokemon_name_id = "charmander"
pokemon_url = f"{base_url}/pokemon/{pokemon_name_id}"

# for berry
berry_name_id = "oran"
berry_url = f"{base_url}/berry/{berry_name_id}"


pokemon_response = requests.get(pokemon_url)
berry_response = requests.get(berry_url)

print(pokemon_response.status_code)  # 200
# print(pokemon_response)  # <response [200]>

# Lets you see the first level of keys
# for k, v in pokemon_response.json().items():
#     print(f"{k}: {v}\n")
#
# for k, v in berry_response.json().items():
#     print(f"{k}: {v}\n")

# prettify the json
# print(json.dumps(pokemon_response.json(), indent=4))

attr_names = [
    'name',
    'abilities',
    'height',
    'weight',
    'types',
    'stats'
    # 'moves'
]

# for attr, is_list in attr_keys.items():
#     if is_list:
#         for item in pokemon_response.json()[attr]:
#             if type(item) is list:
#                 new_list = []
#                 for x in item:
#                     new_list.append(flatten_dict(x))
#                 print(f"{attr}: {new_list}")
#                 continue
#             print(f"{attr}: {flatten_dict(item)}")
#         continue
#     print(f"{attr}:", pokemon_response.json()[attr])

simplified = {}
for attr in attr_names:
    current_val = pokemon_response.json()[attr]
    if type(current_val) is list:
        new_list = []
        for item in current_val:
            flat_item = flatten_dict(item)
            print(f"{attr}: {flat_item}")
            new_list.append(flat_item)
        simplified[attr] = new_list
        continue
    print(f"{attr}:", current_val)
    simplified[attr] = current_val

print(simplified)


if __name__ == "__main__":
    ...
