#!/usr/bin/python3
"""
This script gathers data from a REST API for a given employee ID
and returns information about their TODO list progress.
"""

import requests
import sys

if __name__ == "__main__":
    # Base URL for the REST API
    url = "https://jsonplaceholder.typicode.com/"
    
    # 1. Grab the employee ID passed as an argument in the terminal
    employee_id = sys.argv[1]
    
    # 2. Fetch the user's specific data to get their name
    user_response = requests.get(url + "users/{}".format(employee_id))
    user_data = user_response.json()
    employee_name = user_data.get("name")
    
    # 3. Fetch all tasks associated with this specific user ID
    todos_response = requests.get(url + "todos", params={"userId": employee_id})
    todos_data = todos_response.json()
    
    # 4. Filter out only the completed tasks
    completed_tasks = []
    for task in todos_data:
        if task.get("completed") is True:
            completed_tasks.append(task)
            
    # 5. Print the first line formatted exactly as requested
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(completed_tasks), len(todos_data)))
        
    # 6. Print the title of each completed task with a tab (\t) and a space
    for task in completed_tasks:
        print("\t {}".format(task.get("title")))
