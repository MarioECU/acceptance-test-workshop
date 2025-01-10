import json

# File to save tasks
TASK_FILE = "tasks.json"


# Load tasks from file
def load_tasks():
    try:
        with open(TASK_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


# Save tasks to file
def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


# Add a new task
def add_task(tasks):
    title = input("Enter task title: ").strip()
    description = input("Enter task description: ").strip()
    due_date = input("Enter due date (e.g., YYYY-MM-DD): ").strip()
    priority = input("Enter task priority (Low, Medium, High): ").strip()
    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "priority": priority,
        "status": "Pending",
    }
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!\n")


# List all tasks
def list_tasks(tasks):
    if not tasks:
        print("No tasks found!\n")
        return

    print("\nTasks:")
    # print only title
    for t in tasks:
        print(f"- {t['title']}")


# Mark a task as completed
def mark_task_completed(tasks):
    list_tasks(tasks)
    if not tasks:
        return

    try:
        task_num = int(input("Enter the task number to mark as completed: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["status"] = "Completed"
            save_tasks(tasks)
            print("Task marked as completed!\n")
        else:
            print("Invalid task number!\n")
    except ValueError:
        print("Please enter a valid number!\n")


# Clear all tasks
def clear_tasks():
    confirm = (
        input("Are you sure you want to clear all tasks? (yes/no): ")
        .strip().lower()
    )
    if confirm == "yes":
        save_tasks([])
        print("All tasks cleared!\n")
    else:
        print("Action canceled.\n")


# Main menu
def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Manager")
        print("1. Add a new task")
        print("2. List all tasks")
        print("3. Mark a task as completed")
        print("4. Clear the entire to-do list")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            mark_task_completed(tasks)
        elif choice == "4":
            clear_tasks()
            tasks = []
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.\n")


if __name__ == "__main__":
    main()
