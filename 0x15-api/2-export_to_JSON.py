#!/usr/bin/python3
''' Get user todo list progress. '''
import json
import requests
from sys import argv

if __name__ == '__main__':
    userId = argv[1]
    users = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                         .format(userId))
    todos_list = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos_list = todos_list.json()

    newDict = {}
    newList = []

    for task in todos_list:
        if task.get('userId') == int(userId):
            taskDict = {"task": task.get('title'),
                        "completed": task.get('completed'),
                        "username": users.json().get('username')}
            newList.append(taskDict)
    newDict[userId] = newList

    with open('{:s}.json'.format(userId), mode='w') as task_file:
        json.dump(newDict, task_file)
