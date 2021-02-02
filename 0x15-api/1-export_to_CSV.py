#!/usr/bin/python3
''' Get user todo list progress. '''
from csv import writer, QUOTE_ALL
from sys import argv
from requests import get

if __name__ == '__main__':
    user = get('https://jsonplaceholder.typicode.com/users/{:s}'.format(
        argv[1]))
    todo = get('http://jsonplaceholder.typicode.com/todos?userId={:s}'.format(
        argv[1]))
    user_dict = user.json()
    todo_list = todo.json()

    for u_name in users_dict:
        USERNAME = u_name.get('name')
        USER_ID = u_name.get('id')

    with open("USER_ID" + ".csv", mode='w') as f:
        csv = csv.writer(f, delimiter=',', quoting=csv.QUOTE_ALL)
        for tasks in todos_list:
            TASK_STATUS = tasks.get("completed")
            TASK_TITLE = tasks.get("title")
            csv.writerow([USER_ID, USERNAME, TASK_STATUS, TASK_TITLE])
