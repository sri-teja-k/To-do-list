import os

FILE_NAME = "tasks.txt"


def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        tasks = file.read().splitlines()

    return tasks


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")


def show_tasks(tasks):
    if len(tasks) == 0:
        print("\nNo tasks found.\n")
        return

    print("\nYour Tasks\n")

    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

    print()


def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully.\n")


def remove_task(tasks):
    show_tasks(tasks)

    if len(tasks) == 0:
        return

    try:
        number = int(input("Enter task number to remove: "))

        if 1 <= number <= len(tasks):
            removed = tasks.pop(number - 1)
            save_tasks(tasks)
            print(f'"{removed}" removed successfully.\n')
        else:
            print("Invalid task number.\n")

    except ValueError:
        print("Please enter a valid number.\n")


def main():
    tasks = load_tasks()

    while True:

        print("====== TO-DO LIST ======")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks(tasks)

        elif choice == "2":
            add_task(tasks)

        elif choice == "3":
            remove_task(tasks)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.\n")


main()
