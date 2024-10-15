tasks = []

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Added task!")

def show_tasks():
    if not tasks:
        print("Task list is empty.")
    else:
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")



def mark_task_as_done():
    """Mark a specific task as done."""
    if not tasks:
        print("No tasks to mark as done.")
        return

def sort_tasks():
    """Sort tasks alphabetically."""
    if not tasks:
        print("No tasks to sort.")
    else:
        tasks.sort()  # Sort the tasks list alphabetically
        print("Tasks sorted alphabetically.")


while True:
    print("\nPick a task: ")
    print("1. Display the tasks")
    print("2.Add a task")
    print("3. Mark a task as done")
    print("4. Sort tasks alphabetically")
    print("5. DONE!")
        
    choice = input(">")

    if choice == '1':
        show_tasks()

    elif choice == '2':
        add_task()

    elif choice == '3':
        mark_task_as_done()

    elif choice == '4':
        sort_tasks()

    elif choice == '5':
        break

    else:
        print("Invalide choice.")
