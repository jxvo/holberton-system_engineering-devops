#!/usr/bin/python3
"""
Queries Reddit API 
return number of suscribers to a subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """ returns number of subscribers """
    head = {'User-Agent': 'jank'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    resp = requests.get(url, allow_redirects=False, headers=head)
    if resp.status_code >= 300:
        return 0
    return resp.json().get('data').get('subscribers')
