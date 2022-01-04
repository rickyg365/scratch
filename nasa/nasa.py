import os

import requests
from bs4 import BeautifulSoup

from dotenv import load_dotenv


"""
Base URL: https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY
TOKEN: 
"""


def get_apod_data(api_key, date=None):
    apod_data = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={api_key}")

    return apod_data.json()


def parse_apod(apod_data: dict):
    """ Convert strings from returned dict into appropriate datatypes """
    title = apod_data["title"]
    media_type = apod_data["media_type"]
    hdurl = apod_data["hdurl"]
    url = apod_data["url"]
    explanation = apod_data["explanation"]
    date = apod_data["date"]
    copyright = apod_data.get("copyright", "Uknown Author")

    # key_name: (display_type, display_data)
    new_dict = {
        "title": ("str", title),
        "media_type": ("str", media_type),
        "hdurl": ("img", hdurl),
        "url": ("img", url),
        "explanation": ("str", explanation),
        "date": ("date", date),
        "copyright": ("str", copyright)
    }

    return new_dict


def main():
    # Load Token
    load_dotenv()

    NASA_TOKEN = os.getenv('NASA_TOKEN')

    apod = get_apod_data(NASA_TOKEN)

    print(type(apod))
    print(apod)

    for k, v in apod.items():
        print(type(v))
        print(f"{k}: {v}")

    new = parse_apod(apod)

    print(new)

    return 1


if __name__ == "__main__":
    main()

