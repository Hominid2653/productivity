from datetime import datetime

def validate_task_title(title):
    if not isinstance(title, str) or not title.strip():
        return False, "Title cannot be empty."
    if len(title.strip()) < 3:
        return False, "Title must be at least 3 characters long."
    return True, ""
    
def validate_task_description(description):
    if not isinstance(description, str) or not description.strip():
        return False, "Description cannot be empty."
    if len(description.strip()) < 5:
        return False, "Description must be at least 5 characters long."
    return True, ""
    
def validate_due_date(due_date):
    if not isinstance(due_date, str) or not due_date.strip():
        return False, "Due date cannot be empty."
    try:
        datetime.strptime(due_date.strip(), "%Y-%m-%d")
        return True, ""
    except ValueError:
        return False, "Due date must use YYYY-MM-DD format."
