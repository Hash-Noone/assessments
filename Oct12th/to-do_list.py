def view_tasks(tasks):
    count = 0
    for task in tasks:
        count += 1
        print(f"{count}. {task}")
    
tasks = []
while True:
    print("\n===== To-do List =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Quit")

    choice = input("Choose between 1,2,3,4: ").strip()

    match choice:
        case "1":#add task
            task = input("Enter task you want to do: ").strip()
            if task:
                tasks.append(task)
                print(f"Task {task} added successfully")
            else:
                print("Enter a valid task")
        case "2":#view tasks
            if tasks:
                view_tasks(tasks)
            else:
                print("No tasks avaiable yet")
        case "3": #delete tasks
            if tasks:
                view_tasks(tasks)
                while True:    
                    try:
                        inde = int(input("Enter the index of the task you want to delete: "))
                        break
                    except ValueError:
                        print("Enter a number")
                if int(inde) <= len(tasks) and int(inde) > 0:
                    deleted = tasks.pop(int(inde)-1)
                    print(f"Task {deleted} removed successfully")
                else:
                    print("Enter a valid index")
            else:
                print("No tasks avaiable yet")
        case "4": #Quit
            break