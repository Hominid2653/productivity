from .validation import validate_task_description, validate_task_title, validate_due_date

# Define tasks list
tasks = []


def create_task(title, description, due_date):
    return {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False,
    }


def add_task(title, description, due_date):
    title = validate_task_title(title)
    description = validate_task_description(description)
    due_date = validate_due_date(due_date)

    task = create_task(title, description, due_date)
    tasks.append(task)
    return task
    

def mark_task_as_complete(index, tasks=tasks):
    if not isinstance(index, int):
        raise ValueError("Task index must be an integer.")
    if index < 0 or index >= len(tasks):
        raise IndexError("Task index is out of range.")

    tasks[index]["completed"] = True
    return tasks[index]
    

def view_pending_tasks(tasks=tasks):
    return [task for task in tasks if not task["completed"]]


def calculate_progress(tasks=tasks):
    if not tasks:
        return 0

    completed_count = sum(1 for task in tasks if task["completed"])
    progress = int(round((completed_count / len(tasks)) * 100))
    return progress