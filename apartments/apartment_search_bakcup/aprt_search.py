import os
import time
import re

import requests
from bs4 import BeautifulSoup

from flatten import *


"""
Huge shout out to: https://github.com/adinutzyc21/apartments-scraper/blob/master/parse_apartments.py
"""


def search_aprt(search_url, headers):
    """
    you need to use your user-agent as a header or else it wont work
    """
    print("\n[starting search]\n")
    time.sleep(.25)  # INSURANCE in case I forget to limit rate

    page = requests.get(search_url, headers=headers)

    # print page status
    page_status_map = {
        '2': 'Success',
        '3': 'Redirected',
        '4': 'Error'
    }
    status_code = str(page.status_code)

    print(f"Connection {page_status_map[status_code[0]]}!\n")
    if status_code[0] != '2':
        return None

    # Get soup
    search_soup = BeautifulSoup(page.content, "html.parser")
    search_soup.prettify()

    # the information we need to return as a dict
    fields = {}

    # get the phone number
    get_phone_number(search_soup, fields)

    # get the name of the property
    get_property_name(search_soup, fields)

    # get the address of the property
    get_property_address(search_soup, fields)

    # get the listed info of the property (rent, beds, baths, size)
    get_listed_info(search_soup, fields)

    # get the listed features
    get_features(search_soup, fields)

    # get the one time and monthly fees and parking
    get_lease_fees_pets(search_soup, fields)

    # get the images as a list
    get_images(search_soup, fields)

    # get the description section
    get_description(search_soup, fields)

    # get the amenities description
    get_amenities(search_soup, fields)

    # get the 'interior information'

    # get the 'outdoor information'

    # get the 'gym information'

    # get the 'kitchen information'

    # get the 'services information'

    # get the 'living space information'

    # get the 'property information'

    return fields


def get_images(soup, fields):
    # NOT OG
    """Get the images of the apartment"""

    fields['img'] = ''

    if soup is None:
        return

    # find ul with id fullCarouselCollection
    soup = soup.find('section', id='carouselSection')

    if soup is None:
        return

    soup = soup.find('ul')

    if soup is not None:
        imgs = []
        for img in soup.find_all('img'):
            fields['img'] += f"![{img['alt']}]({img['src']}) \n"  # '![' + img['alt'] + '](' + img['src'] + ') '
            imgs.append(f"![{img['alt']}]({img['src']})")

        fields['img-data'] = imgs


def get_phone_number(soup, fields):
    """
    Not all listings have an aside,, some have a contact box under their description
    """
    fields['phone'] = ''

    if soup is None:
        print("[phone soup]: FAILED")
        return

    start = soup.find('div', id="profilePaid")

    # Contact Info
    if start is None:
        print("[phone soup]: FAILED")
        return
    contact_card = start.find('aside', id='contactLead')
    cta = contact_card.find('div', class_="ctaContainer")
    phone_label = cta.find('p', class_="phoneLabel")
    phone = phone_label.find('span', class_="phoneNumber")
    phone_number = phone.get_text()

    # print(phone_number)
    fields['phone'] = phone_number


def get_description(soup, fields):
    """Get the description for the apartment"""

    fields['description'] = ''

    if soup is None:
        return

    soup = soup.find('section', id="descriptionSection")

    # find first p
    obj = soup.find('p')

    if obj is not None:
        # could use strip = true instead of this custom function I borrowed
        fields['description'] = obj.getText(strip=True)


def get_listed_info(soup, fields):
    """Get the description for the apartment"""

    fields['rent'] = ''
    fields['beds'] = ''
    fields['bath'] = ''
    fields['size'] = ''

    if soup is None:
        return

    soup = soup.find('div', class_="priceBedRangeInfoContainer")

    if soup is None:
        return

    soup = soup.find_all('li')

    if soup is not None:
        # could use strip = true instead of this custom function I borrowed
        list_info = []
        for element in soup:
            new_detail = element.find('p', class_="rentInfoDetail")
            new_detail = new_detail.get_text()
            list_info.append(new_detail)

        fields['rent'] = list_info[0]
        fields['beds'] = list_info[1]
        fields['bath'] = list_info[2]
        fields['size'] = list_info[3]


def get_features(soup, fields):
    """Get the description for the apartment"""

    fields['features'] = ''

    if soup is None:
        print("[feature soup]: FAILED")
        return

    soup = soup.find('section', id="descriptionSection")

    soup = soup.find('div', class_="subSpec")

    if soup is None:
        print("[feature soup]: NO FEATURES")
        return

    soup = soup.find('ul')

    obj = soup.find_all('li')

    if obj is not None:
        features = ''
        features_data = []
        for element in obj:
            raw_text = element.find('span').get_text()
            features_data.append(raw_text)
            text = f" - {raw_text}\n"
            features += text

        # could use strip = true instead of this custom function I borrowed
        fields['features'] = features
        fields['features-data'] = features_data


def get_amenities(soup, fields):
    """Get the description for the apartment"""

    fields['amenities'] = ''

    if soup is None:
        print("[amenity soup]: failed")
        return

    soup = soup.find('section', id="amenitiesSection")

    if soup is None:
        print("[amenity soup]: failed")
        return

    # Get title list
    raw_titles = soup.find_all('h2', class_="sectionTitle")

    # Process list
    titles = []
    for title in raw_titles:
        titles.append(f"{title.get_text()}")

    # Get main amenity list
    raw_card_sections = soup.find_all('div', class_="amenitiesIconGridContainer mortar-wrapper fourColumnGrid")

    # Process list
    card_sections = []
    card_sections_data = []

    for section in raw_card_sections:
        cards = section.find_all('p', class_="amenityLabel")
        section_data = ''
        indv_section = []

        # Get all the cards from each section
        for card in cards:
            indv_section.append(card.get_text())
            section_data += f" - [{card.get_text()}]\n"
        card_sections.append(section_data)
        card_sections_data.append(indv_section)

    # Get other amenity list
    raw_other = soup.find_all('div', class_="spec")

    # Process list
    other = []
    other_data = []

    for section in raw_other:
        groups = section.find_all('ul')

        group_text = ''
        indv_group = []
        for group in groups:
            elements = group.find_all('li', class_="specInfo")
            for element in elements:
                sp = element.find('span')
                text = sp.get_text()
                indv_group.append(text)
                group_text += f" - {text}\n"

        other.append(group_text)
        other_data.append(indv_group)

    # Combine data list
    total_amenity_sections = len(titles)
    new_data = ''

    try:
        final_data = {}
        for i in range(total_amenity_sections):
            current_title = titles[i]
            current_card_section = card_sections[i]
            current_other = other[i]

            new_data += f"{current_title}:\n \n{current_card_section}\n{current_other}\n"

            data_key = f"{current_title}"
            group_data = card_sections_data + other_data
            final_data[data_key] = group_data

        fields['amenities'] = new_data
        fields['amenities_data'] = final_data

    except IndexError:
        print("something went wrong with the card index, maybe there are none")


def get_lease_fees_pets(soup, fields):
    """Get the description for the apartment"""

    fields['lease'] = ''
    # fields['fees'] = ''
    # fields['pets'] = ''

    if soup is None:
        print(f"[lease soup]: FAILED")
        return

    soup = soup.find('div', id="profileV2FeesWrapper")
    # soup.find('section', id="feesSection")
    if soup is None:
        print(f"[lease soup]: FAILED")
        return

    objs = soup.find_all('li')

    if objs is not None:
        text = ''
        section_objs = []
        for obj in objs:
            text += f" - {obj.get_text(strip=True)}\n"
            # print(text)
            section_objs.append(obj.get_text(strip=True))

        fields['lease'] = text
        fields['lease_data'] = section_objs


def get_property_name(soup, fields):
    """Get the description for the apartment"""

    fields['name'] = ''

    if soup is None:
        return

    obj = soup.find('h1', id="propertyName")

    if obj is not None:
        # could use strip = true instead of this custom function I borrowed
        property_name = obj.get_text()
        fields['name'] = property_name.strip()


def get_property_address(soup, fields):
    """Get the description for the apartment"""

    fields['address'] = ''
    fields['neighborhood'] = ''

    if soup is None:
        return

    soup = soup.find('div', class_="propertyAddressContainer")

    if soup is None:
        return

    obj = soup.find('h2')

    if obj is not None:
        # Address
        street_city = obj.find_all('span', class_=None)

        street, city = street_city[0], street_city[1]
        street_name, city_name = street.get_text(), city.get_text()

        # State and Zip
        state_zip = obj.find('span', class_="stateZipContainer")

        state_zip = state_zip.find_all('span')
        state, zip_co = state_zip

        state_initials, zip_code = state.get_text(), zip_co.get_text()

        # Neighborhood
        neighborhood_element = obj.find('span', class_="neighborhoodAddress")

        neighborhood = neighborhood_element.find('a', class_="neighborhood").get_text()

        final_address = f"{street_name}, {city_name}, {state_initials}, {zip_code}"

        fields['address'] = final_address
        fields['neighborhood'] = neighborhood


def display_data(fields, feat=False, lease=False, amenity=False):
    flattend_data = flatten_print(fields)
    print(flattend_data)
    # for key, value in fields.items():
    #     space_value = len(key) + 2
    #
    #     # if type(value) is dict:
    #     #     for k, v in value.items():
    #     #         print(f"{k}: \n{v}")
    #     #     continue
    #     #
    #     # if type(value) is list:
    #     #     for item in value:
    #     #         print(item)
    #     #     continue
    #
    #     if key == 'img':
    #         continue
    #
    #     if key == 'features' and feat is False:
    #         continue
    #
    #     if key == 'lease' and lease is False:
    #         continue
    #
    #     if key == 'amenities' and amenity is False:
    #         continue
    #
    #     if key == 'description':
    #         print(f"\n[{key.title():^{space_value}}]: \n \n{value}\n")
    #         continue
    #
    #     print(f"\n[{key.title():^{space_value}}]: {value}")

    return


if __name__ == "__main__":

    while True:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
        }
        url = input("Apartment URL: ")

        if url.lower() == 'q':
            break

        data = search_aprt(url, headers)

        display_data(data)

        time.sleep(1)
