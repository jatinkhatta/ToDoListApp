import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List with Priority")

        # Task entry
        self.task_label = tk.Label(root, text="Task:")
        self.task_label.pack(pady=5)
        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.pack(pady=5)

        # Priority entry
        self.priority_label = tk.Label(root, text="Priority (1=High, 2=Medium, 3=Low):")
        self.priority_label.pack(pady=5)
        self.priority_var = tk.IntVar(value=2)
        self.priority_entry = tk.Entry(root, textvariable=self.priority_var, width=5)
        self.priority_entry.pack(pady=5)

        # Add task button
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        # Task listbox
        self.task_listbox = tk.Listbox(root, width=60, height=15)
        self.task_listbox.pack(pady=10)

        # Remove task button
        self.remove_button = tk.Button(root, text="Remove Selected Task", command=self.remove_task)
        self.remove_button.pack(pady=5)

        # List to store tasks
        self.tasks = []

    def add_task(self):
        task = self.task_entry.get()
        priority = self.priority_var.get()
        
        if not task:
            messagebox.showwarning("Input Error", "Task cannot be empty.")
            return
        
        if priority not in [1, 2, 3]:
            messagebox.showwarning("Input Error", "Priority must be 1, 2, or 3.")
            return

        self.tasks.append((priority, task))
        self.tasks.sort()  # Sort tasks by priority
        self.update_task_listbox()

    def remove_task(self):
        selected_task_index = self.task_listbox.curselection()
        if not selected_task_index:
            messagebox.showwarning("Selection Error", "No task selected.")
            return

        self.tasks.pop(selected_task_index[0])
        self.update_task_listbox()

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for priority, task in self.tasks:
            priority_text = {1: "High", 2: "Medium", 3: "Low"}[priority]
            self.task_listbox.insert(tk.END, f"[{priority_text}] {task}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
