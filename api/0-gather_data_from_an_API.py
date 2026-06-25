#!/usr/bin/python3
"""
This script gathers data from a REST API for a given employee ID
and returns information about their TODO list progress.
"""

import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    emp_id = sys.argv[1]

    user_res = requests.get(url + "users/{}".format(emp_id))
    user_data = user_res.json()
    employee_name = user_data.get("name")

    todos_res = requests.get(url + "todos", params={"userId": emp_id})
    todos_data = todos_res.json()

    completed_tasks = []
    for task in todos_data:
        if task.get("completed") is True:
            completed_tasks.append(task)

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(completed_tasks), len(todos_data)))

    for task in completed_tasks:
        print("\t {}".format(task.get("title")))
