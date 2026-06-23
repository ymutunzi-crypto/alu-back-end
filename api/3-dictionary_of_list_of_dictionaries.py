#!/usr/bin/python3
"""
This script exports TODO list data for ALL employees from a REST API
and combines it into a single JSON file structured by user ID.
"""

import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    # 1. Fetch all users to create a dictionary mapping user ID to username
    users_res = requests.get(url + "users")
    users_data = users_res.json()
    user_map = {user.get("id"): user.get("username") for user in users_data}

    # 2. Fetch all tasks from the endpoint
    todos_res = requests.get(url + "todos")
    todos_data = todos_res.json()

    # 3. Build the primary dictionary tracking all users
    all_employees_data = {}

    # Initialize empty lists for every valid user ID first
    for user_id in user_map.keys():
        all_employees_data[str(user_id)] = []

    # 4. Populate each user's task list matching the exact key sequence required
    for task in todos_data:
        u_id = task.get("userId")
        if u_id in user_map:
            all_employees_data[str(u_id)].append({
                "username": user_map.get(u_id),
                "task": task.get("title"),
                "completed": task.get("completed")
            })

    # 5. Save the compiled dictionary to the required file name
    file_name = "todo_all_employees.json"
    with open(file_name, mode="w") as json_file:
        json.dump(all_employees_data, json_file)
