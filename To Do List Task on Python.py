class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """Adds a task to the to-do list."""
        self.tasks.append(task)
        print(f"Task '{task}' added.")

    def remove_task(self, task):
        """Removes a task from the to-do list."""
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Task '{task}' removed.")
        else:
            print(f"Task '{task}' not found.")

    def view_tasks(self):
        """Displays all tasks in the to-do list."""
        if self.tasks:
            print("Your To-Do List:")
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task}")
        else:
            print("Your to-do list is empty.")

def display_menu():
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit")

def main():
    todo_list = TodoList()
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            task = input("Enter a task to add: ")
            todo_list.add_task(task)
        elif choice == "2":
            task = input("Enter a task to remove: ")
            todo_list.remove_task(task)
        elif choice == "3":
            todo_list.view_tasks()
        elif choice == "4":
            print("Exiting the To-Do list program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
