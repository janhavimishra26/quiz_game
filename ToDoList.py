tasks = []

while True:
    print("\n---- To-Do List Menu ----")
    print("1. Add Tasks")
    print("2. View Tasks")
    print("3. Remove Tasks")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        task = input("Enter the task: ")
        tasks.append(task)
        print(f'"{task}" has been added to your to-do list.')

    elif choice == '2':
        if not tasks:
            print("Your to-do list is empty.")
        else:
            print("Your tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == '3':
        if not tasks:
            print("Your to-do list is empty.")
        else:
            print("Your tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            
            try:
                task_num = int(input("Enter the task number to remove: "))
                if 1 <= task_num <= len(tasks):
                    removed = tasks.pop(task_num - 1)
                    print(f'"{removed}" has been removed from your to-do list.')
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == '4':
        print("Exiting to-do list. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 4.")
