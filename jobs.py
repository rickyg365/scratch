import os
import time

import requests
from bs4 import BeautifulSoup

"""
Download Pages
"""

base_url = "https://www.edjoin.org/"

# Download OMSD Page
omsd_url = base_url + "omsd"
OMSD = requests.get(omsd_url)

# print(OMSD.status_code)
# print(OMSD.content)

# Download CJHUSD Page
cjhusd_url = base_url + "cjhusd"
CJHUSD = requests.get(cjhusd_url)


"""
Parse with bs4
"""
# OMSD
omsd_soup = BeautifulSoup(OMSD.content, 'html.parser')

print(omsd_soup.prettify())

# Find job list container first
joblist_container = omsd_soup.find("article", class_='span7 blue data-block')  # find("div", id='jobListContainer')
print(joblist_container)
# omsd_soup.findAll('div', class_='contain')
# or
# job_listings = joblist_container.find_all('div', class_='edjoin-card')  # omsd_soup.select("div.contain a")

job_listings = joblist_container.select('a')

print(job_listings)

for job in job_listings:
    print(job)


# CJHUSD
cjhusd_soup = BeautifulSoup(CJHUSD.content, 'html.parser')


