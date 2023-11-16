#!/usr/bin/python3
""" This a basic get request from an API """
import json
from requests import get
from sys import argv
url = "https://jsonplaceholder.typicode.com/users/"
url1 = "https://jsonplaceholder.typicode.com/todos/"


if __name__ == "__main__":

    response = get(url1, {"userId": argv[1]})  # , {"id": argv[1]})
    if response.status_code == 200:
        info = json.loads(response.text)
    # print(info)
    tasks = 0
    completed = 0
    completed_list = []
    for item in info:
        if item["completed"]:
            completed += 1
            completed_list.append(item["title"])
        tasks += 1
    response = get(url, {"id": argv[1]})
    if response.status_code == 200:
        info = json.loads(response.text)
        name = info[0]["name"]
    # print(name)
    # print(f"{completed}/{tasks}")

    print(f"Employee {name} is done with tasks({completed}/{tasks})")
    for item in completed_list:
        print(f"\t {item}")
