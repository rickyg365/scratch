from pprint import pprint
from datetime import datetime
import googlemaps

API_KEY = "get it online"

# Setup client for use with api key
map_client = googlemaps.Client(API_KEY)

# Request directions via public transit
now = datetime.now()
directions_result = map_client.directions("Sydney Town Hall",
                                          "Parramatta, NSW",
                                          mode="transit",
                                          departure_time=now)

# Find an address
location_name = "bubba gump santa monica"
search_response = map_client.places(query=location_name)
search_results = search_response.get('results', "no results found")
first_result = search_results[0]


# def get_place(location_name):
#     try:
#         search_response = map_client.places(query=location_name)
#         search_results = search_response.get('results', "no results found")
#         return search_results
#     except Exception as e:
#         print(e)
#         return None

# geocode an address
my_address = "1 Market st, San Francisco, CA"

# Look up an address with reverse geocoding
reverse_geocode_result = map_client.reverse_geocode((40.714224, -73.961452))

# get data/response from geocode client api
my_address_data = map_client.geocode(my_address)
# pprint(my_address_data[0]['geometry'])
"""
Sample Data

[{'address_components': [{'long_name': '1',
                          'short_name': '1',
                          'types': ['street_number']},
                         {'long_name': 'Market Street',
                          'short_name': 'Market St',
                          'types': ['route']},
                         {'long_name': 'South Beach',
                          'short_name': 'South Beach',
                          'types': ['neighborhood', 'political']},
                         {'long_name': 'San Francisco',
                          'short_name': 'SF',
                          'types': ['locality', 'political']},
                         {'long_name': 'San Francisco County',
                          'short_name': 'San Francisco County',
                          'types': ['administrative_area_level_2',
                                    'political']},
                         {'long_name': 'California',
                          'short_name': 'CA',
                          'types': ['administrative_area_level_1',
                                    'political']},
                         {'long_name': 'United States',
                          'short_name': 'US',
                          'types': ['country', 'political']},
                         {'long_name': '94105',
                          'short_name': '94105',
                          'types': ['postal_code']},
                         {'long_name': '1420',
                          'short_name': '1420',
                          'types': ['postal_code_suffix']}],
  'formatted_address': '1 Market St, San Francisco, CA 94105, USA',
  'geometry': {'location': {'lat': 37.7932183, 'lng': -122.3946979},
               'location_type': 'ROOFTOP',
               'viewport': {'northeast': {'lat': 37.7945672802915,
                                          'lng': -122.3933489197085},
                            'southwest': {'lat': 37.7918693197085,
                                          'lng': -122.3960468802915}}},
  'place_id': 'ChIJkXCsHWSAhYARsGBBQYcj-V0',
  'plus_code': {'compound_code': 'QJV4+74 South Beach, San Francisco, CA, USA',
                'global_code': '849VQJV4+74'},
  'types': ['street_address']}]
"""

# Latitude and Longitude
lat = my_address_data[0]['geometry']['location']['lat']
lon = my_address_data[0]['geometry']['location']['lng']

# Full Address
full_addy = my_address_data[0]['formatted_address']

# Address breakdown, long name
addy_components = my_address_data[0]['address_components']
processed_addy_components = {}

for component in addy_components:
    key = component["types"][0]

    processed_addy_components[key] = component["long_name"]

text = f"""
Full Address: {full_addy}

Coordinates: ( {lat}, {lon} )
"""
print(text)

for k, v in processed_addy_components.items():
    print(f"{k}: {v}\n")
