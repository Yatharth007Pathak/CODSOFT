import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except:
        messagebox.showwarning("Warning", "You must select a task to delete.")

def clear_all_tasks():
    listbox.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("To-Do List Application")

# Create widgets
entry = tk.Entry(root, width=50)
add_button = tk.Button(root, text="Add Task", command=add_task)
delete_button = tk.Button(root, text="Delete Task", command=delete_task)
clear_button = tk.Button(root, text="Clear All Tasks", command=clear_all_tasks)
listbox = tk.Listbox(root, width=50, height=10)

# Layout widgets
entry.pack(pady=10)
add_button.pack(pady=5)
delete_button.pack(pady=5)
clear_button.pack(pady=5)
listbox.pack(pady=10)

# Run the application
root.mainloop()
