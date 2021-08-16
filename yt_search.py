import os
from bs4 import BeautifulSoup
import requests


def process_search(raw_search_query):
    processed_query = ""
    search_words = raw_search_query.split()

    for index, word in enumerate(search_words):
        if index != 0:
            processed_query += f"+{word}"
            continue
        processed_query += f"{word}"

    return processed_query


base_url = "https://www.youtube.com/results?search_query="


search_query = input("Search: ")
print(search_query)

processed_search = process_search(search_query)
print(processed_search)

final_url = f"{base_url}{processed_search}"
# req = requests.get(final_url)
# soup = BeautifulSoup(req.content, "html.parser")

# No webscraperino youtube
# print(soup.title)
# main_content = soup.find(id="contents")
#
# print(main_content)
#
# video_containers = main_content.find_all("ytd-video-renderer")
#
# print(video_containers)
