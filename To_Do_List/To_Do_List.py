import json
import os

class TodoList:
    def __init__(self, filename='tasks.txt'):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        """Load tasks from the file."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                self.tasks = json.load(file)

    def save_tasks(self):
        """Save tasks to the file."""
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file)

    def add_task(self, task_description):
        """Add a new task to the list."""
        task_id = len(self.tasks) + 1
        task = {'id': task_id, 'description': task_description}
        self.tasks.append(task)
        self.save_tasks()
        print(f'Task added: {task_description}')

    def view_tasks(self):
        """View all tasks in the list."""
        if not self.tasks:
            print("No tasks available.")
            return
        for task in self.tasks:
            print(f"{task['id']}: {task['description']}")

    def delete_task(self, task_id):
        """Delete a task from the list."""
        self.tasks = [task for task in self.tasks if task['id'] != task_id]
        self.save_tasks()
        print(f'Task {task_id} deleted.')

def main():
    todo_list = TodoList()

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            task_description = input("Enter task description: ")
            todo_list.add_task(task_description)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            task_id = int(input("Enter task ID to delete: "))
            todo_list.delete_task(task_id)
        elif choice == '4':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()

