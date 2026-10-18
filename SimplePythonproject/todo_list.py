
# Python To-Do List Project
# This program allows users to add, view, complete, and delete tasks.

# Create an empty list to store all tasks.
# Each task will be stored as a dictionary.
tasks = []


def add_task():
    # Ask the user to enter a task description.
    task_name = input("Enter your task: ").strip()

    # Do not allow an empty task.
    if not task_name:
        print("Task cannot be empty!")
        return

    # Create a dictionary for the new task.
    # Every new task starts as incomplete.
    task = {
        "name": task_name,
        "completed": False
    }

    # Add the new task to the tasks list.
    tasks.append(task)

    print("Task added successfully!")


def view_tasks():
    # Check whether the task list is empty.
    if not tasks:
        print("No tasks available.")
        return

    print("\n--- Your To-Do List ---")

    # Display every task with its number and status.
    for index, task in enumerate(tasks, start=1):
        # Show Completed or Pending based on the task status.
        if task["completed"]:
            status = "Completed"
        else:
            status = "Pending"

        print(f"{index}. {task['name']} - {status}")


def complete_task():
    # Show all tasks before asking which one to complete.
    view_tasks()

    # Stop if there are no tasks.
    if not tasks:
        return

    try:
        # Ask the user for the task number.
        task_number = int(input("Enter the task number to complete: "))

        # Check whether the task number is valid.
        if task_number < 1 or task_number > len(tasks):
            print("Invalid task number!")
            return

        # Convert the task number to a list index.
        # User task numbers start at 1, but indexes start at 0.
        task = tasks[task_number - 1]

        # Mark the selected task as completed.
        task["completed"] = True

        print("Task marked as completed!")

    except ValueError:
        # Handle input that is not a whole number.
        print("Please enter a valid whole number.")


def delete_task():
    # Show all tasks before asking which one to delete.
    view_tasks()

    # Stop if there are no tasks.
    if not tasks:
        return

    try:
        # Ask the user for the task number to delete.
        task_number = int(input("Enter the task number to delete: "))

        # Validate the task number.
        if task_number < 1 or task_number > len(tasks):
            print("Invalid task number!")
            return

        # Remove the selected task from the list.
        # Subtract 1 because list indexes start at 0.
        removed_task = tasks.pop(task_number - 1)

        print(f"Deleted task: {removed_task['name']}")

    except ValueError:
        # Handle invalid input such as letters or decimals.
        print("Please enter a valid whole number.")


# Main program: keep showing the menu until the user exits.
while True:
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    # Read the user's menu choice.
    choice = input("Enter your choice (1-5): ").strip()

    # Call the function selected by the user.
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Thank you for using the To-Do List!")
        break
    else:
        # Handle an invalid menu choice.
        print("Invalid choice! Please select a number from 1 to 5.")
