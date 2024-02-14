import os
import re

# Help function
def help():
    print("Help:\n"
          "add <task>: Add a new task\n"
          "print: Print the todo list\n"
          "complete <task_number>: Complete a task\n"
          "report: Statistics of the todo list\n"
          "delete <task_number>: Delete a task\n"
          "exit: Quit the application\n")

# Add function
def add(tasks, new_task):
    tasks.append(new_task)

# Print function
def print_tasks(tasks):
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

# Complete function
def complete(tasks, task_number, completed_tasks):
    try:
        task = tasks[int(task_number) - 1]
        tasks.remove(task)
        completed_tasks.append(task)
        print(f"Task {task_number} '{task}' completed.")
    except (IndexError, ValueError):
        print("Invalid task number.")

# Report function
def report(tasks, completed_tasks):
    total_tasks = len(tasks) + len(completed_tasks)
    completed_count = len(completed_tasks)
    print(f"Total tasks: {total_tasks}\n"
          f"Completed tasks: {completed_count}\n"
          f"Pending tasks: {total_tasks - completed_count}")

# Delete function
def delete(tasks, task_number):
    try:
        tasks.pop(int(task_number) - 1)
    except (IndexError, ValueError):
        print("Invalid task number.")

# Main function
def main():
    tasks = []
    completed_tasks = []

    if os.path.exists("todo.txt"):
        with open("todo.txt", "r") as file:
            for line in file:
                tasks.append(line.strip())

    while True:
        user_input = input("> ").split()
        command = user_input[0].lower()

        if command == "help":
            help()
        elif command == "add":
            if len(user_input) > 1:
                add(tasks, ' '.join(user_input[1:]))
                with open("todo.txt", "a") as file:
                    file.write(f"{' '.join(user_input[1:])}\n")
            else:
                print("Please provide a task to add.")
        elif command == "print":
            print_tasks(tasks)
        elif command == "complete":
            if len(user_input) > 1:
                complete(tasks, user_input[1], completed_tasks)
            else:
                print("Please provide a task number to complete.")
        elif command == "report":
            report(tasks, completed_tasks)
        elif command == "delete":
            if len(user_input) > 1:
                delete(tasks, user_input[1])
            else:
                print("Please provide a task number to delete.")
        elif command == "exit":
            break
        else:
            print("Unknown command.")

help()
main()