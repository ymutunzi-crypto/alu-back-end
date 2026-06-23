#!/usr/bin/python3
"""
This script exports TODO list data for ALL employees from a REST API
and combines it into a single JSON file structured by user ID.
"""

import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch users
    users_res = requests.get(url + "users")
    users_data = users_res.json()
    
    # Broken down user_map
    user_map = {}
    for user in users_data:
        u_id = user.get("id")
        user_map[u_id] = user.get("username")

    # Fetch tasks
    todos_res = requests.get(url + "todos")
    todos_data = todos_res.json()

    # Build primary dictionary
    all_employees_data = {}

    # Initialize keys safely across short lines
    for user_id in user_map.keys():
        str_id = str(user_id)
        all_employees_data[str_id] = []

    # Populate tasks with strict line-length safety
    for task in todos_data:
        u_id = task.get("userId")
        if u_id in user_map:
            str_id = str(u_id)
            task_dict = {
                "username": user_map.get(u_id),
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            all_employees_data[str_id].append(task_dict)

    # Save to file
    file_name = "todo_all_employees.json"
    with open(file_name, mode="w") as json_file:
        json.dump(all_employees_data, json_file)
