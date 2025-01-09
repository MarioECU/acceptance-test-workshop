import os
import json
from behave import given, when, then

TASK_FILE = "tasks.json"

# Helper functions
def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Given Steps
@given('the to-do list is empty')
def step_given_to_do_list_empty(context):
    save_tasks([])

@given('the to-do list contains tasks')
def step_given_to_do_list_contains_tasks(context):
    tasks = []
    for row in context.table:
        tasks.append({
            "title": row["Task"],
            "description": row.get("Description", "Default description"),
            "due_date": row.get("Due Date", "2025-01-01"),
            "priority": row.get("Priority", "Medium"),
            "status": row.get("Status", "Pending")
        })
    save_tasks(tasks)

# When Steps
@when('the user adds a task "{task_title}"')
def step_when_user_adds_task(context, task_title):
    tasks = load_tasks()
    task = {
        "title": task_title,
        "description": "Default description",
        "due_date": "2025-01-01",
        "priority": "Medium",
        "status": "Pending"
    }
    tasks.append(task)
    save_tasks(tasks)

@when('the user lists all tasks')
def step_when_user_lists_all_tasks(context):
    tasks = load_tasks()
    context.task_output = tasks

@when('the user marks task "{task_title}" as completed')
def step_when_user_marks_task_completed(context, task_title):
    tasks = load_tasks()
    for task in tasks:
        if task["title"] == task_title:
            task["status"] = "Completed"
            break
    save_tasks(tasks)

@when('the user clears the to-do list')
def step_when_user_clears_to_do_list(context):
    save_tasks([])

# Then Steps
@then('the to-do list should contain "{task_title}"')
def step_then_to_do_list_should_contain_task(context, task_title):
    tasks = load_tasks()
    assert any(task["title"] == task_title for task in tasks), f"Task '{task_title}' not found in the to-do list."

@then('the output should contain')
def step_then_output_should_contain(context):
    # TODO
    assert False

@then('the to-do list should show task "{task_title}" as completed')
def step_then_task_should_be_completed(context, task_title):
    tasks = load_tasks()
    task = next((task for task in tasks if task["title"] == task_title), None)
    assert task is not None, f"Task '{task_title}' not found in the to-do list."
    assert task["status"] == "Completed", f"Task '{task_title}' is not marked as completed."

@then('the to-do list should be empty')
def step_then_to_do_list_should_be_empty(context):
    tasks = load_tasks()
    assert len(tasks) == 0, "The to-do list is not empty."

# 2 new scenarios
# When Steps
@when('the user updates the priority of task "{task_title}" to "{new_priority}"')
def step_when_user_updates_task_priority(context, task_title, new_priority):
    tasks = load_tasks()
    for task in tasks:
        if task["title"] == task_title:
            task["priority"] = new_priority
            break
    save_tasks(tasks)

@when('the user deletes task "{task_title}"')
def step_when_user_deletes_task(context, task_title):
    tasks = load_tasks()
    tasks = [task for task in tasks if task["title"] != task_title]
    save_tasks(tasks)

# Then Steps
@then('the to-do list should show task "{task_title}" with priority "{expected_priority}"')
def step_then_task_should_have_priority(context, task_title, expected_priority):
    tasks = load_tasks()
    task = next((task for task in tasks if task["title"] == task_title), None)
    assert task is not None, f"Task '{task_title}' not found in the to-do list."
    assert task["priority"] == expected_priority, f"Expected priority '{expected_priority}', but got '{task['priority']}'."

@then('the to-do list should not contain "{task_title}"')
def step_then_task_should_not_be_in_list(context, task_title):
    tasks = load_tasks()
    assert not any(task["title"] == task_title for task in tasks), f"Task '{task_title}' was found in the to-do list."

