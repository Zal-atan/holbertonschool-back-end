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

    user_response = get(url, {"id": argv[1]})
    if user_response.status_code == 200:
        user = json.loads(user_response.text)
    todo_response = get(url1, {"userId": argv[1]})
    if todo_response.status_code == 200:
        todo = json.loads(todo_response.text)
    complete_list = []
    for item in todo:
        user_name = user[0]["username"]
        todo_comp = item["completed"]
        todo_title = item["title"]
        new_dic = {"task": todo_title, "completed": todo_comp,
                   "username": user_name}
        complete_list.append(new_dic)

    user_dic = {str(argv[1]): complete_list}

    return user_dic


def write_to_json(dict_to_write):
    """Write an input list of lists into a json file"""
    filename = f"{argv[1]}.json"
    with open(filename, 'w') as file:
        json.dump(dict_to_write, file)


if __name__ == "__main__":
    response_dict = get_response()
    write_to_json(response_dict)
