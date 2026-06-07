from datetime import datetime

MAX_TITLE_LENGTH = 100
MAX_DESCRIPTION_LENGTH = 300
DATE_FORMAT = "%Y-%m-%d"


def validate_task_title(title):
    if not isinstance(title, str):
        raise ValueError("Task title must be a string.")

    title = title.strip()
    if not title:
        raise ValueError("Task title cannot be empty.")
    if len(title) > MAX_TITLE_LENGTH:
        raise ValueError(f"Task title must be at most {MAX_TITLE_LENGTH} characters.")

    return title


def validate_task_description(description):
    if not isinstance(description, str):
        raise ValueError("Task description must be a string.")

    description = description.strip()
    if not description:
        raise ValueError("Task description cannot be empty.")
    if len(description) > MAX_DESCRIPTION_LENGTH:
        raise ValueError(f"Task description must be at most {MAX_DESCRIPTION_LENGTH} characters.")

    return description
    

def validate_due_date(due_date):
    if not isinstance(due_date, str):
        raise ValueError("Due date must be a string in YYYY-MM-DD format.")

    due_date = due_date.strip()
    try:
        parsed_date = datetime.strptime(due_date, DATE_FORMAT).date()
    except ValueError:
        raise ValueError("Due date must be formatted as YYYY-MM-DD.")

    if parsed_date < datetime.now().date():
        raise ValueError("Due date cannot be in the past.")

    return due_date
