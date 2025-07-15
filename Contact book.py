import tkinter as tk
from tkinter import messagebox
import os

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.root.geometry("400x450")
        self.root.configure(bg="#f0f0f0")

        self.tasks = []
        self.load_tasks()

        # Input Frame
        input_frame = tk.Frame(self.root, bg="#f0f0f0")
        input_frame.pack(pady=10)

        # Task Entry
        self.task_entry = tk.Entry(input_frame, width=35, font=("Helvetica", 12))
        self.task_entry.pack(side=tk.LEFT, padx=(0, 10))
        
        # Add Button
        self.add_button = tk.Button(input_frame, text="Add Task", command=self.add_task, 
                                    bg="#4CAF50", fg="white", font=("Helvetica", 10, "bold"), relief=tk.RAISED)
        self.add_button.pack(side=tk.LEFT)

        # Listbox Frame
        listbox_frame = tk.Frame(self.root)
        listbox_frame.pack(pady=10)

        # To-Do Listbox
        self.tasks_listbox = tk.Listbox(listbox_frame, width=50, height=15, selectmode=tk.SINGLE,
                                        bg="#ffffff", fg="#333333", font=("Helvetica", 10),
                                        selectbackground="#a6a6a6", selectforeground="black")
        self.tasks_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        # Scrollbar for Listbox
        scrollbar = tk.Scrollbar(listbox_frame, orient=tk.VERTICAL, command=self.tasks_listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tasks_listbox.config(yscrollcommand=scrollbar.set)

        # Button Frame for actions (Update, Delete, Save)
        button_frame = tk.Frame(self.root, bg="#f0f0f0")
        button_frame.pack(pady=10)

        # Mark Completed Button
        self.complete_button = tk.Button(button_frame, text="Mark Completed", command=self.mark_completed, 
                                         bg="#2196F3", fg="white", font=("Helvetica", 10, "bold"))
        self.complete_button.pack(side=tk.LEFT, padx=5)

        # Update Task Button
        self.update_button = tk.Button(button_frame, text="Update Task", command=self.update_task, 
                                       bg="#FF9800", fg="white", font=("Helvetica", 10, "bold"))
        self.update_button.pack(side=tk.LEFT, padx=5)

        # Delete Button
        self.delete_button = tk.Button(button_frame, text="Delete Task", command=self.delete_task, 
                                       bg="#F44336", fg="white", font=("Helvetica", 10, "bold"))
        self.delete_button.pack(side=tk.LEFT, padx=5)

        self.update_listbox()

    def load_tasks(self):
        if os.path.exists("tasks_gui.txt"):
            with open("tasks_gui.txt", "r") as file:
                self.tasks = [line.strip() for line in file.readlines()]

    def save_tasks(self):
        with open("tasks_gui.txt", "w") as file:
            for task in self.tasks:
                file.write(task + "\n")

    def update_listbox(self):
        self.tasks_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.tasks_listbox.insert(tk.END, task)

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            # Add new task marked as pending
            self.tasks.append(f"[ ] {task}")
            self.task_entry.delete(0, tk.END)
            self.update_listbox()
            self.save_tasks()
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def delete_task(self):
        try:
            # Get the index of the selected task
            selected_task_index = self.tasks_listbox.curselection()[0]
            # Remove the task from the list
            self.tasks.pop(selected_task_index)
            self.update_listbox()
            self.save_tasks()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to delete.")

    def mark_completed(self):
        try:
            selected_task_index = self.tasks_listbox.curselection()[0]
            task = self.tasks[selected_task_index]
            
            if task.startswith("[ ]"):
                # Replace '[ ]' with '[X]'
                self.tasks[selected_task_index] = task.replace("[ ]", "[X]", 1)
            else:
                # If already completed, unmark it (optional feature)
                self.tasks[selected_task_index] = task.replace("[X]", "[ ]", 1)

            self.update_listbox()
            self.save_tasks()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to mark.")

    def update_task(self):
        try:
            selected_task_index = self.tasks_listbox.curselection()[0]
            current_task = self.tasks[selected_task_index]
            
            # Extract the task description (remove [ ] or [X])
            description_start = current_task.find("] ") + 2
            current_description = current_task[description_start:]
            
            # Update the entry field with the current description
            self.task_entry.delete(0, tk.END)
            self.task_entry.insert(0, current_description)
            
            # Delete the current task from the list
            self.tasks.pop(selected_task_index)
            self.update_listbox()
            self.save_tasks()

            messagebox.showinfo("Update Mode", "Enter the updated task in the entry field and click 'Add Task' to save.")
            
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to update.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
