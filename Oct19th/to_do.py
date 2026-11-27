
def view_tasks(tasks):
    count = 0

    for task in tasks:
        count += 1

        name = list(task.keys())[0]
        status = list(task.values())[0]

        if status:
            print(f"{count}. [x] {name}")
        else:
            print(f"{count}. [ ] {name}")


tasks = []

while True:
    print("\n===== To-do List =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Done with Task")
    print("5. Quit")

    choice = input("Choose between 1,2,3,4,5: ").strip()

    match choice:
        case "1":
            task = input("Enter task you want to do: ").strip()

            if task:
                tasks.append({task: False})
                print(f"Task {task} added successfully")
            else:
                print("Enter a valid task")

        case "2":
            if tasks:
                view_tasks(tasks)
            else:
                print("No tasks available yet")

        case "3":
            if tasks:
                view_tasks(tasks)

                try:
                    index = int(input("Enter the index to delete: "))

                    if 1 <= index <= len(tasks):
                        deleted = tasks.pop(index - 1)
                        print(f"Task {list(deleted.keys())[0]} removed successfully")
                    else:
                        print("Enter a valid index")

                except ValueError:
                    print("Enter a number")

            else:
                print("No tasks available yet")

        case "4":
            if tasks:
                view_tasks(tasks)

                try:
                    index = int(input("Enter the index of the task you completed: "))

                    if 1 <= index <= len(tasks):
                        task = tasks[index - 1]
                        name = list(task.keys())[0]
                        task[name] = True

                        print(f"Task '{name}' done!")

                    else:
                        print("Enter a valid index")

                except ValueError:
                    print("Enter a number")

            else:
                print("No tasks available yet")

        case "5":
            print("Goodbye")
            break

        case _:
            print("Invalid choice")
