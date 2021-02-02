#!/usr/bin/python3
"""Exports All data in the JSON format"""
import requests
import json


if __name__ == "__main__":

    users = requests.get("https://jsonplaceholder.typicode.com/users")
    users = users.json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = todos.json()
    todoAll = {}

    for i in users:
        taskList = []
        for task in todos:
            if task.get('userId') == i.get('id'):
                taskDict = {"username": i.get('username'),
                            "task": task.get('title'),
                            "completed": task.get('completed')}
                taskList.append(taskDict)
        todoAll[i.get('id')] = taskList

    with open('todo_all_employees.json', mode='w') as f:
        json.dump(todoAll, f)
