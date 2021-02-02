#!/usr/bin/python3
''' Get user todo list progress. '''
import json
import requests
from sys import argv

if __name__ == '__main__':
    users = requests.get('https://jsonplaceholder.typicode.com/users',
                         params={"id": argv[1]})
    todos = requests.get('https://jsonplaceholder.typicode.com/todos',
                         params={"userId": argv[1]})
    user_dict = users.json()
    todo_list = todos.json()

    for i in todo_list:
        i.pop('userId')
        i.pop('id')
        i['task'] = i.pop('title')
        i['username'] = user_dict[0].get('name')
    megaDict = {str(argv[1]): todo_list}
    with open('{:s}.json'.format(str(argv[1])), mode='w') as task_file:
        json.dump(megaDict, task_file)
