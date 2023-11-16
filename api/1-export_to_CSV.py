#!/usr/bin/python3
"""
This a basic get request from an API and copy it into a CSV file
"""

import csv
import json
from requests import get
from sys import argv

url = "https://jsonplaceholder.typicode.com/users/"
url1 = "https://jsonplaceholder.typicode.com/todos/"


def get_response():
    """ This is a basic API call function returning a list """

    user_response = get(url, {"id": argv[1]})
    if user_response.status_code == 200:
        user = json.loads(user_response.text)
    print(user[0]["username"])
    todo_response = get(url1, {"userId": argv[1]})
    if todo_response.status_code == 200:
        todo = json.loads(todo_response.text)
    complete_list = []
    for item in todo:
        user_id = str(user[0]["id"])
        user_name = user[0]["username"]
        todo_comp = str(item["completed"])
        todo_title = item["title"]
        new_list = [user_id, user_name, todo_comp, todo_title]
        complete_list.append(new_list)

    return complete_list


def write_to_csv(list_to_write):
    """Write an input list of lists into a csv file"""
    filename = f"{argv[1]}.csv"
    with open(filename, 'w') as file:
        csv_writer = csv.writer(file)
        for item in list_to_write:
            csv_writer.writerow(item)


if __name__ == "__main__":
    response_list = get_response()
    write_to_csv(response_list)
