#!/usr/bin/python3

import requests
import sys


def main():
    if len(sys.argv) != 2:
        return

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        return

    # API endpoints
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    # Fetch data
    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    if user_response.status_code != 200:
        return

    user = user_response.json() # json() pares a json string into a python directory
    todos = todos_response.json()

    employee_name = user.get("name")
    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed") is True]
    number_done = len(done_tasks)

    # Print required format
    print(f"Employee {employee_name} is done with tasks({number_done}/{total_tasks}):")

    for task in done_tasks:
        print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    main()