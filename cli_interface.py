def run_cli(task_manager):
    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. Get Next Task")
        print("3. List Tasks")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter task description: ")
            priority = int(input("Enter priority (lower number = higher priority): "))
            task_manager.add_task(description, priority)
        elif choice == '2':
            next_task = task_manager.get_next_task()
            if next_task:
                print(f"Next task: {next_task.description} (Priority: {next_task.priority})")
            else:
                print("No tasks in the queue.")
        elif choice == '3':
          tasks = task_manager.list_tasks()
          if tasks:
            for description, priority in tasks:
              print(f"- {description} (Priority: {priority})")
          else:
            print("No tasks in the queue.")
        elif choice == '4':
            break
        else:
            print("Invalid choice.")