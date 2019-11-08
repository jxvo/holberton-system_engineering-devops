#!/usr/bin/python3
"""GETS User and Tasks Completed from jsonplaceholder API"""


import requests
from sys import argv


if __name__ == "__main__":
res = requests.get('https://jsonplaceholder.typicode.com/todos')
  res2 = requests.get('https://jsonplaceholder.typicode.com/users')

   for user_dict in res2.json():
        if user_dict.get('id') == int(argv[1]):
            username = user_dict.get('username')

    with open('{}.csv'.format(argv[1]), 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for todo_dict in res.json():
            if todo_dict.get('userId') == int(argv[1]):
                a_list = [argv[1], username,
                          todo_dict.get('completed'), todo_dict.get('title')]
                spamwriter.writerow(a_list)
