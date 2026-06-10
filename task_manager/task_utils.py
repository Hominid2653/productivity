# Define tasks list
tasks = []

# Implement add_task function
def add_task(title, description, due_date):
    from .validation import validate_task_title, validate_task_description, validate_due_date

    validate_task_title(title)
    validate_task_description(description)
    validate_due_date(due_date)

    task = {
        "title": title.strip(),
        "description": description.strip(),
        "due_date": due_date.strip(),
        "completed": False,
    }
    tasks.append(task)
    return "Task added successfully!"
    
# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
    if not isinstance(index, int):
        raise ValueError("Task index must be an integer.")
    if index < 1 or index > len(tasks):
        raise IndexError("Task number is out of range.")

    tasks[index - 1]["completed"] = True
    return "Task marked as complete!"
    
# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    return [task for task in tasks if not task["completed"]]

# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    total = len(tasks)
    if total == 0:
        return 0.0

    completed = sum(1 for task in tasks if task.get("completed"))
    return round((completed / total) * 100, 1)
