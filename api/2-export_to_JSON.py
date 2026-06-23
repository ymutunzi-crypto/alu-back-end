#!/usr/bin/python3
"""
This script exports employee TODO list data from a REST API
and saves it into a JSON file format.
"""

import json
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    emp_id = sys.argv[1]

    # Fetch user data to extract the 'username'
    user_res = requests.get(url + "users/{}".format(emp_id))
    user_data = user_res.json()
    username = user_data.get("username")

    # Fetch all tasks owned by this employee
    todos_res = requests.get(url + "todos", params={"userId": emp_id})
    todos_data = todos_res.json()

    # Build the list of task dictionaries formatted as required
    tasks_list = []
    for task in todos_data:
        tasks_list.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    # Wrap the list in the final dictionary format mapping to the employee ID
    json_data = {str(emp_id): tasks_list}

    # Define the output file name dynamically
    file_name = "{}.json".format(emp_id)

    # Write the formatted data into the JSON file
    with open(file_name, mode="w") as json_file:
        json.dump(json_data, json_file)
