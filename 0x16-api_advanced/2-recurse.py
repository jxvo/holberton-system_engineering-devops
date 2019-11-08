#!/usr/bin/python3
"""
recusively queries reddit api for all hot articles
returns titles of articles or None if no results are found
"""


import requests


def recurse(subreddit, hot_list=[], after='', count=0):
    head = {'User-Agent': 'jank'}
    url = 'https://www.reddit.com/r/{}/hot.json?after={}&count={}'.format(
        subreddit,
        after,
        count
    )
    resp = requests.get(url, allow_redirects=False, headers=head)
    if resp.status_code >= 300:
        return(None)

    respj = resp.json()
    after = respj.get('data').get('after')
    count += respj.get('data').get('dist')

    if count == 0:
        return(None)
    for r in respj.get('data').get('children'):
        hot_list.append(r.get('data').get('title'))
    if after is None:
        return hot_list
    return recurse(subreddit, hot_list=hot_list, after=after, count=count)
