#!/usr/bin/python3
"""GETS User and Tasks Completed from jsonplaceholder API"""


import json
import requests


if __name__ == "__main__":
    res = requests.get('https://jsonplaceholder.typicode.com/todos')
    res2 = requests.get('https://jsonplaceholder.typicode.com/users')

    a_dict = {}
    for user in res2.json():
        username = user.get('username')
        a_list = []
        for todo_dict in res.json():
            if todo_dict.get('userId') == user.get('id'):
                task_dict = {}
                task_dict['task'] = todo_dict.get('title')
                task_dict.update({'username': username})
                task_dict['completed'] = todo_dict.get('completed')
                a_list.append(task_dict)
        a_dict['{}'.format(user.get('id'))] = a_list

    with open('todo_all_employees.json', 'w', newline='') as csvfile:
        json.dump(a_dict, csvfile)
