#!/usr/bin/python3
"""Function to print top10Hotspots API"""

import requests


def top_ten(subreddit):
    """number of hotspots api"""

    i = 0
    api = requests.get("https://www.reddit.com/r/{}/hot.json"
                       .format(subreddit), headers={'User-agent': 'stonks'})
    if not api:
        print("None")
    else:
        while i < 10:
            print(api.json().get('data').get('children')[i]
                  .get('title'))
            i += 1
