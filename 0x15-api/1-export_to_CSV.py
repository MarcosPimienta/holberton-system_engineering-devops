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
    with open('{:s}.csv'.format(argv[1]), mode='w') as task_file:
        task_writer = writer(task_file, delimiter=',', quotechar='"',
                             quoting=QUOTE_ALL)
        for item in todo_list:
            task_writer.writerow([user_dict['id'], user_dict['username'],
                                 item['completed'], item['title']])
