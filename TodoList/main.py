def todolist():
    tasks = []
    
    while True:
        print("\n --------To-Do List-------");
        print("1. Add Your Task")
        print("2. Show Tasks")
        print("3. Mark The Task Which You Complete")
        print("4. Update Task")
        print("5. Exit")
        
        choice = input("Enter the choice number : ")
        
        if choice == '1':
            print()
            num_task = int(input("How many task you want to add : "))
            
            for i in range(num_task):
                task = input("Add a task: ")
                tasks.append({"task": task, "done": False})
                print("Task is added !")
                
        elif choice == '2':
            print("\n Tasks List")
            for index, task in enumerate(tasks):
                status = "Done" if task["done"] else "Not Done"
                print(f"{index + 1}. {task['task']} - {status}")
                
        elif choice == '3':
            task_index = int(input("Enter the task number which you want to mark as done : ")) - 1
            if 0 <= task_index < len(tasks):
                tasks[task_index]["done"] = True
                print("Task marked as done!")
            else:
                print("Invalid task number.")
                
        elif choice == '4':
            task_index = int(input("Enter the task number which you want to update : ")) - 1
            if 0 <= task_index < len(tasks):
                new_task = input("Enter a new task : ")
                tasks[task_index]["task"] = new_task
                print("Task is updated!")
            else:
                print("Invalid task number.")
                
        elif choice == '5':
            print("Exiting the todo list.")
            break
        else:
            print("Invalid choice. Please try again!")
            
__name__ == "__todolist__";
todolist()
                
                
                
            
        
        