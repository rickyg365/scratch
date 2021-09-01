import os
import time

import requests
from bs4 import BeautifulSoup


"""
Program: Apartment Url List Scraper
Author: Rickyg3
Date: 08/28/21
"""
"""
Creates a list of urls separated by a newline and saved in a txt file

How to use:
    - use build url to get a search url
    - pass the search url into the run_search function to get the expected output.
    
Methods to maintain:
    - build_url: maintain
    - scrape_apartment_list: maintain
    - save_apartment_urls: upgrade, add other save options (json, csv, pickle)
    - page_status_validation: upgrade, add more codes


"""


def validate_city(raw_name):
    city_name = raw_name.strip()
    city_name = city_name.replace(' ', '-')
    city_name = city_name.lower()

    return city_name


def validate_state(raw_state):
    if len(raw_state) > 2:
        # Gonna have to load this from a file if we want to add new states
        state_map = {
            'alaska': 'ak',
            'california': 'ca',
            'colorado': 'co',
            'maine': 'me',
            'montana': 'mo',
            'texas': 'tx',
            'florida': 'fl',
            'new york': 'ny',
            'idaho': 'id'
        }
        if raw_state not in state_map:
            print(f"\n{raw_state} not recognized.\n")

            add_state = input("Would you like to add it to the database?")

            if add_state.lower() == 'n':
                return raw_state

            print(f"adding {raw_state}...")

            # This is based on trust lmaoooooooo
            new_initials = input(f"\nplease input {raw_state} initials: ")
            state_map[raw_state] = new_initials

            return new_initials

    state_initials = raw_state.lower()

    return state_initials


def build_url(city_name, state_initials, price='', beds='', sort='new'):
    """
    base_url: https://www.apartments.com/{city-name}-{state initials}/

    price-filter:
        max: under-2000
        min: over-1500
        min-max: 1500-to-2750

    bed-filter:
        min: min-1-bedrooms
        max: max-1-bedrooms
        min-max: 1-to-3-bedrooms


    sort-by-new: ?so=8

    https://www.apartments.com/long-beach-ca/1-to-3-bedrooms-1500-to-2500/?so=8

    final_url: https://www.apartments.com/{city-name}-{si}/{bed-filter}-{price-filter}/{sort}
    """
    base_url = 'https://www.apartments.com'

    # validate inputs
    # city name
    city_name = validate_city(city_name)

    # state initials
    state_initials = validate_state(state_initials)

    # price
    # price = validate_price(price)

    # beds
    # beds = validate_beds(beds)

    # sort
    # sort = validate_sort(sort)

    # build final url

    final_url = f"{base_url}/{city_name}-{state_initials}/"

    return final_url


def page_status_validation(page_status_code):
    page_status_map = {
        '2': 'Success',
        '3': 'Redirected',
        '4': 'Error'
    }

    key = page_status_code[0]

    print(f"Connection {page_status_map[key]}!\n")

    if key != '2':
        return False

    return True


def run_search(search_url, headers):
    """
    you need to use your user-agent as a header or else it wont work
    """
    print("\n[starting search]\n")
    time.sleep(.25)  # INSURANCE in case I forget to limit rate

    page = requests.get(search_url, headers=headers)

    # print page status
    status_code = str(page.status_code)
    page_status = page_status_validation(status_code)

    if not page_status:
        return None

    # Get soup
    search_soup = BeautifulSoup(page.content, "html.parser")
    search_soup.prettify()

    # get the list
    new_apartment_list = scrape_apartment_list(search_soup)

    save_apartment_urls(new_apartment_list)


def scrape_apartment_list(soup):
    """ """
    if soup is None:
        return

    aprt_urls = []

    soup = soup.find('section', id="placards")

    soup = soup.find('div', id="placardContainer")

    soup = soup.find('ul')

    if soup is not None:
        listings = soup.find_all('li', class_='mortar-wrapper')

        for listing in listings:
            url_element = listing.find('article')
            new_url = url_element['data-url']
            aprt_urls.append(new_url)

    return aprt_urls


def save_apartment_urls(url_list, file_name='apartment_urls.txt'):

    counter = 0

    with open(file_name, 'w') as output_file:
        for url in url_list:
            line = f"{url}\n"
            output_file.write(line)
            counter += 1

    print(f"Apartments Found: {counter}")

    return


if __name__ == "__main__":

    city = input("City: ")
    state = input("State: ")

    # url = input("Search Page URL: ")
    url = build_url(city, state)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
    }

    run_search(url, headers)
