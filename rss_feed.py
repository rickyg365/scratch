import os
import feedparser
from bs4 import BeautifulSoup

"""
Program: RSS Feed
Author: Rickyg3
Date: 07/13/2021
"""

'''
Notes:

* Front page:  http://www.reddit.com/.rss
* A subreddit:  http://www.reddit.com/r/news/.rss
* A user:  http://www.reddit.com/u/unidan.rss  
* A multireddit:  http://www.reddit.com/r/news+wtf.rss (note that the slash is optional).
* The comments on a specific reddit post:  http://www.reddit.com/r/technology/comments/1uc9ro/wearing_a_mind_controlled_exoskeleton_a_paralyzed/.rss
* Submissions from a domain:  http://www.reddit.com/domain/microsoft.com/.rss


1. we should have a class to get the feed
2. 
'''

base_url = "https://www.reddit.com/"

subreddit_name = "news"
subreddit = f"r/{subreddit_name}/"

user_name = "unidan"
user = f"u/{user_name}"

multi_names = ["news", "wtf"]
multi = "+".join(multi_names)

rss_url = base_url + ".rss"

parser = feedparser.parse(rss_url)

soup = BeautifulSoup(parser['entries'][0]['description'], 'html.parser')
print(soup.div.get_text())


if __name__ == "__main__":
    os.system('cls')
    print(f"Num of Entries: {len(parser.entries)}")
    for entry in parser.entries:
        print(f"{entry.title}:  {entry.link}")
        # print(entry.links)
        print(entry.links[0].href)
        # print(entry.content)
        print('content', entry.content[0].value)
        print('-'*50)
