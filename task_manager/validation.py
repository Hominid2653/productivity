from datetime import datetime


def validate_task_title(title):
    if not isinstance(title, str) or not title.strip():
        raise ValueError("Title cannot be empty.")
    if len(title.strip()) < 3:
        raise ValueError("Title must be at least 3 characters long.")
    return True
    
def validate_task_description(description):
    if not isinstance(description, str) or not description.strip():
        raise ValueError("Description cannot be empty.")
    if len(description.strip()) < 5:
        raise ValueError("Description must be at least 5 characters long.")
    if len(description) > 500:
        raise ValueError("Description cannot be longer than 500 characters.")
    return True
    
def validate_due_date(due_date):
    if not isinstance(due_date, str) or not due_date.strip():
        raise ValueError("Due date cannot be empty.")
    try:
        datetime.strptime(due_date.strip(), "%Y-%m-%d")
        return True
    except ValueError:
        raise ValueError("Due date must use YYYY-MM-DD format.")
