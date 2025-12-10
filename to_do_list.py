tasks = []
while True:
    print("\n---To-Do List---")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        task = input("Enter your task: ")
        tasks.append(task)
        print("Task added!")
    elif choice == "2":
        print("\nYour Tasks:")
        for i, t in enumerate(tasks):
            print(f"{i+1}.{t}")
    elif choice == "3":
        task_num = int(input("Enter task number to remove: "))
        if 1 <= task_num <= len(tasks):
            tasks.pop(task_num-1)
            print("Task removed!")
        else:
            print("Invalid task number!")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
