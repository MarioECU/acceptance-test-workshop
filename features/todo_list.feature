Feature: To-Do List Manager

  # Scenarios given in the instructions
  Scenario: Add a task to the to-do list
    Given the to-do list is empty
    When the user adds a task "Buy groceries"
    Then the to-do list should contain "Buy groceries"

  Scenario: List all tasks in the to-do list
    Given the to-do list contains tasks:
      | Task        |
      | Buy groceries |
      | Pay bills    |
    When the user lists all tasks
    Then the output should contain:
      """
      Tasks:
      - Buy groceries
      - Pay bills
      """

  Scenario: Mark a task as completed
    Given the to-do list contains tasks:
      | Task          | Status   |
      | Buy groceries | Pending  |
    When the user marks task "Buy groceries" as completed
    Then the to-do list should show task "Buy groceries" as completed

  Scenario: Clear the entire to-do list
    Given the to-do list contains tasks:
      | Task        |
      | Buy groceries |
      | Pay bills    |
    When the user clears the to-do list
    Then the to-do list should be empty

  # 2 new Scenarios
  Scenario: Update the priority of a task
    Given the to-do list contains tasks:
        | Task          | Description | Due Date   | Priority | Status   |
        | Buy groceries | Food items  | 2025-01-15 | Low      | Pending  |
    When the user updates the priority of task "Buy groceries" to "High"
    Then the to-do list should show task "Buy groceries" with priority "High"

  Scenario: Delete a specific task from the to-do list
    Given the to-do list contains tasks:
        | Task          | Description | Due Date   | Priority | Status   |
        | Buy groceries | Food items  | 2025-01-15 | Low      | Pending  |
        | Pay bills     | Electricity | 2025-01-20 | Medium   | Pending  |
    When the user deletes task "Pay bills"
    Then the to-do list should not contain "Pay bills"

