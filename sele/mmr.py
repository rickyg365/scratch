import os
import time

# Data imports
import json
from datetime import datetime
import pandas as pd

# Web imports
import requests
from bs4 import BeautifulSoup

"""
To Do:
    - actually think about how the api should be implemented maybe make a sample use case first

"""


# api = requests.get("https://na.whatismymmr.com/api/v1/summoner?name=rickyg3")
# data = json.loads(api.content)
# aram_data = data["ARAM"]
# # print(aram_data)
#
# final_data = parse_aram_data(aram_data)
# # print(final_data)
#
# print(nice_text(final_data))


class MMRData:
    """ <platform>:<app ID>:<version string> """
    """ <Windows>:<MMRApi>:<version 1.0> """
    def __init__(self, username):
        self.time_format = "%m-%d-%Y, %I:%M"

        self.username = username
        self.api_url = ""
        self.update_url()

        # Initialize variables to hold unparsed json
        self.raw_ranked_data = None
        self.raw_aram_data = None

        # Collect data
        self.get_data()

        # Clean up data
        self.ranked_data = None
        self.aram_data = self.parse_aram_data(self.raw_aram_data)

    def __str__(self):
        text = ""
        # aram_text = self.nice_text(self.aram_data)
        return text

    def update_url(self):
        self.api_url = f"https://na.whatismymmr.com/api/v1/summoner?name={self.username}"

    def update_user(self, new_username):
        """ Update Username """
        self.username = new_username

    def get_data(self):
        """ Gets raw data from url and returns a json object """
        raw_data = requests.get(self.api_url)
        json_data = json.loads(raw_data.content)

        self.raw_ranked_data = json_data['ranked']
        self.raw_aram_data = json_data["ARAM"]

    def parse_aram_data(self, raw_data=None):
        if raw_data is None:
            raw_data = self.aram_data

        mmr = raw_data['avg']
        error = raw_data['err']

        timeclock = datetime.fromtimestamp(raw_data['timestamp'])
        formatted_time = timeclock.strftime(self.time_format)

        new_data = {
            "mmr": mmr,
            "error": error,
            "timestamp": formatted_time
        }

        historical_list = raw_data.get('historical', None)
        if historical_list is not None:
            new_list = []
            for _, item in enumerate(historical_list):
                new_obj = self.parse_aram_data(item)
                new_list.append(new_obj)

            new_data['historical'] = new_list
            new_data['rank'] = raw_data['closestRank']
            new_data['percentile'] = raw_data['percentile']

        return new_data

    def nice_text(self, data, title=True):
        top = ""
        if title:
            top += "\nAram Stats: \n"
            top += f"<{data['rank']}>  {data['percentile']}%\n"
        top += f"  MMR: {data['mmr']} ±{data['error']} \t({data['timestamp']})"
        # print(top)

        formatted_list = []
        historical_list = data.get('historical', None)
        if historical_list is not None:
            top += "\n \nHistorical Stats: "
            # print("\nHistorical: \n")
            for item in historical_list:
                # print("+")
                new_text = self.nice_text(item, False)
                top += f"\n  {new_text}"

        return top

    def save_cache_data(self, filename="output.csv"):
        pass


class MmrScraper:
    def __init__(self, username):
        self.username = username
        self.current_mmr = None
        self.base_url = "https://na.whatismymmr.com/"
        self.url = self.build_url()

        self.stats = {
            "name": username,
            "mmr": 0,
            "rank": ""
        }

    def __str__(self):
        text = ""
        return text

    def build_url(self):
        return f"{self.base_url}{self.username}"

    def update_user(self, new_username):
        self.username = new_username

        # rebuild url
        self.url = self.build_url()

    def get_mmr(self):
        base_page = requests.get(self.url)
        # print(base_page.content)

        soup = BeautifulSoup(base_page.content, "html.parser")

        # print(soup.prettify())
        main_container = soup.find('container', id="container--main")

        # print(main_container)
        aram_wrapper = main_container. find('wrapper', id="stats--aram")
        # soup.find('div', class_="text--stats--hero")
        aram_box = aram_wrapper.select("div.text--stats--hero > span.text--main--display")

        aram_stat = aram_box[0].get_text()
        aram_stat_text = aram_wrapper.find('div', class_="text--stats--summary").get_text()

        self.stats["mmr"] = aram_stat
        self.stats["rank"] = aram_stat_text
        print(f"MMR: {aram_stat}")
        print(f"{aram_stat_text}")
        print(self.stats)
        print(self.url)


def main():
    # my_scraper = MmrScraper("rickyg3")
    #
    # my_scraper.get_mmr()

    mmr_obj = MMRData('rickyg3')

    aram_data = mmr_obj.aram_data

    print(mmr_obj.nice_text(aram_data))


if __name__ == "__main__":
    main()
