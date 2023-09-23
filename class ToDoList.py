class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def view_tasks(self):
        if self.tasks:
            print("To-Do List:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")
        else:
            print("No tasks in the list.")

    def update_task(self, index, new_task):
        if 1 <= index <= len(self.tasks):
            self.tasks[index - 1] = new_task
            print(f"Task {index} updated.")
        else:
            print("Invalid task index.")


todo_list = ToDoList()

while True:
    print("\nMenu:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Update Task")
    print("5. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter the task: ")
        todo_list.add_task(task)
    elif choice == "2":
        todo_list.view_tasks()
        index = int(input("Enter the task number to remove: "))
        todo_list.remove_task(todo_list.tasks[index - 1])
    elif choice == "3":
        todo_list.view_tasks()
    elif choice == "4":
        todo_list.view_tasks()
        index = int(input("Enter the task number to update: "))
        new_task = input("Enter the new task: ")
        todo_list.update_task(index, new_task)
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")
