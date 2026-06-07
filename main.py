from task_manager.task_utils import add_task, mark_task_as_complete, view_pending_tasks, calculate_progress, tasks

# Define the main function
def main():
    while True:
        print("Task Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Enter task title: ").strip()
            description = input("Enter task description: ").strip()
            due_date = input("Enter due date (YYYY-MM-DD): ").strip()
            try:
                print(add_task(title, description, due_date))
            except ValueError as error:
                print(error)
        elif choice == "2":
            if not tasks:
                print("No tasks available.")
                continue
            for index, task in enumerate(tasks, start=1):
                status = "Done" if task["completed"] else "Pending"
                print(f"{index}. {task['title']} ({status})")
            task_number = input("Enter the task number to mark as complete: ").strip()
            if not task_number.isdigit():
                print("Please enter a valid task number.")
                continue
            try:
                print(mark_task_as_complete(int(task_number)))
            except (ValueError, IndexError) as error:
                print(error)
        elif choice == "3":
            pending_tasks = view_pending_tasks()
            if not pending_tasks:
                print("No pending tasks.")
            else:
                for task in pending_tasks:
                    print(f"- {task['title']} (Due: {task['due_date']}) - {task['description']}")
        elif choice == "4":
            print(calculate_progress())
        elif choice == "5":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")
        
if __name__ == "__main__":
    main()
