#!/usr/bin/python3
"""Function to return API"""

import requests


def number_of_subscribers(subreddit):
    """number of subscribers api"""

    api = requests.get("https://www.reddit.com/r/{}/about.json"
                       .format(subreddit), headers={'User-agent': 'stonks'})
    if not api:
        return 0
    else:
        return(api.json().get('data').get('subscribers'))
