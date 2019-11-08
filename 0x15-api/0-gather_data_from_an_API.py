#!/usr/bin/python3
"""GETS User and Tasks Completed from jsonplaceholder API"""


import requests
from sys import argv

if __name__ == "__main__":
    tasks_completed = 0
    res = requests.get('https://jsonplaceholder.typicode.com/todos')
    res2 = requests.get('https://jsonplaceholder.typicode.com/users')
    for todo_dict in res.json():
        if todo_dict.get('userId') == int(argv[1]) and \
           todo_dict.get('completed') is True:
            tasks_completed += 1

    for user_dict in res2.json():
        if user_dict.get('id') == int(argv[1]):
            user = user_dict.get('name')

    print("Employee {} is done with tasks({}/20):".format(user,
                                                          tasks_completed))
    for todo_dict in res.json():
        if todo_dict.get('userId') == int(argv[1]) and \
           todo_dict.get('completed') is True:
            print("\t {}".format(todo_dict.get('title')))
