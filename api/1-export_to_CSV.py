#!/usr/bin/python3
"""
This script exports employee TODO list data from a REST API
and saves it into a CSV file format.
"""

import csv
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

    # Define the output file name dynamically
    file_name = "{}.csv".format(emp_id)

    # Open the file in write mode
    with open(file_name, mode="w", newline="") as csv_file:
        # csv.QUOTE_ALL ensures every string, int, and bool gets wrapped in ""
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        # Write each task row to the CSV file
        for task in todos_data:
            writer.writerow([
                emp_id,
                username,
                task.get("completed"),
                task.get("title")
            ])
