from task_manager.task_utils import add_task, mark_task_as_complete, view_pending_tasks, calculate_progress, tasks


def display_tasks(task_list):
    if not task_list:
        print("No tasks to display.")
        return

    for index, task in enumerate(task_list, start=1):
        status = "Done" if task["completed"] else "Pending"
        print(f"{index}. {task['title']} (Due: {task['due_date']}) - {status}")
        print(f"   Description: {task['description']}")


def prompt_new_task():
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    return title, description, due_date


def main():
    while True:
        print("\nTask Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title, description, due_date = prompt_new_task()
            try:
                add_task(title, description, due_date)
                print("Task added successfully!")
            except ValueError as error:
                print(f"Error: {error}")
        elif choice == "2":
            pending = view_pending_tasks(tasks)
            if not pending:
                print("There are no pending tasks to complete.")
                continue

            print("Pending tasks:")
            display_tasks(pending)
            try:
                selected = int(input("Enter the number of the task to mark complete: "))
                if selected < 1 or selected > len(pending):
                    raise ValueError("Selection is out of range.")

                task_index = tasks.index(pending[selected - 1])
                mark_task_as_complete(task_index)
                print("Task marked as complete.")
            except (ValueError, IndexError) as error:
                print(f"Error: {error}")
        elif choice == "3":
            pending = view_pending_tasks(tasks)
            if not pending:
                print("There are no pending tasks.")
            else:
                print("Pending tasks:")
                display_tasks(pending)
        elif choice == "4":
            progress = calculate_progress(tasks)
            print(f"Progress: {progress}% complete")
        elif choice == "5":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
