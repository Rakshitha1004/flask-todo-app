todo_list = []

def show_tasks():
    if not todo_list:
        print("No tasks yet.")
    else:
        for i, task in enumerate(todo_list, 1):
            status = "✔️ Done" if task["done"] else "❌ Not Done"
            print(f"{i}. {task['task']} [{status}]")

def add_task(task):
    todo_list.append({"task": task, "done": False})
    print("Task added.")

def delete_task(index):
    if 0 < index <= len(todo_list):
        removed = todo_list.pop(index - 1)
        print(f"Deleted: {removed['task']}")
    else:
        print("Invalid task number.")

def mark_done(index):
    if 0 < index <= len(todo_list):
        todo_list[index - 1]["done"] = True
        print(f"Marked as done: {todo_list[index - 1]['task']}")
    else:
        print("Invalid task number.")

while True:
    print("\n=== To-Do List ===")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Mark Task as Done")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == '1':
        show_tasks()
    elif choice == '2':
        task = input("Enter task: ")
        add_task(task)
    elif choice == '3':
        show_tasks()
        try:
            idx = int(input("Enter task number to delete: "))
            delete_task(idx)
        except ValueError:
            print("Please enter a valid number.")
    elif choice == '4':
        show_tasks()
        try:
            idx = int(input("Enter task number to mark as done: "))
            mark_done(idx)
        except ValueError:
            print("Please enter a valid number.")
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid option.")
