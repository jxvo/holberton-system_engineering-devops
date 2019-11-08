#!/usr/bin/python3
"""GETS User and Tasks Completed from jsonplaceholder API"""


import json
import requests
from sys import argv


if __name__ == "__main__":
    res = requests.get('https://jsonplaceholder.typicode.com/todos')
    res2 = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(
        argv[1]))

    username = res2.json()['username']

    with open('{}.json'.format(argv[1]), 'w', newline='') as csvfile:
        a_dict = {}
        a_list = []
        for todo_dict in res.json():
            if todo_dict.get('userId') == int(argv[1]):
                task_dict = {}
                task_dict['task'] = todo_dict.get('title')
                task_dict.update({'username': username})
                task_dict['completed'] = todo_dict.get('completed')
                a_list.append(task_dict)
        a_dict['{}'.format(argv[1])] = a_list
        json.dump(a_dict, csvfile)
