#!/usr/bin/python3
"""
This a basic get request from an API and copy it into a json file
"""

import json
from requests import get
from sys import argv

url = "https://jsonplaceholder.typicode.com/users/"
url1 = "https://jsonplaceholder.typicode.com/todos/"


def get_response():
    """ This is a basic API call function returning a dic """

    user_response = get(url)
    if user_response.status_code == 200:
        users = json.loads(user_response.text)
    todo_response = get(url1)
    if todo_response.status_code == 200:
        todo = json.loads(todo_response.text)
    user_dic = {}
    for user in users:
        username = user["name"]
        id = user["id"]
        complete_list = []
        for item in todo:
            if id == item["userId"]:
                todo_task = item["title"]
                todo_compl = item["completed"]
                task_dict = {
                    "username": username,
                    "task": todo_task,
                    "completed": todo_compl}
                complete_list.append(task_dict)
        user_dic[str(id)] = complete_list

    return user_dic


def write_to_json(dict_to_write):
    """Write an input list of lists into a json file"""
    filename = "todo_all_employees.json"
    with open(filename, 'w') as file:
        json.dump(dict_to_write, file)


if __name__ == "__main__":
    response_dict = get_response()
    write_to_json(response_dict)
