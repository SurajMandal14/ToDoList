import tkinter as tk
from tkinter import messagebox


def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)


def remove_task():
    try:
        index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(index)
    except IndexError:
        pass


def save_tasks():
    tasks = listbox_tasks.get(0, tk.END)
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")


def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            for task in tasks:
                listbox_tasks.insert(tk.END, task.strip())
    except FileNotFoundError:
        messagebox.showwarning("Warning", "No saved tasks found.")


root = tk.Tk()
root.title("To-Do List")

frame_tasks = tk.Frame(root)
frame_tasks.pack()

listbox_tasks = tk.Listbox(frame_tasks, height=10, width=50)
listbox_tasks.pack(side=tk.LEFT)

scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tk.Entry(root, width=50)
entry_task.pack()

button_add_task = tk.Button(root, text="Add Task", width=48, command=add_task)
button_add_task.pack()

button_remove_task = tk.Button(
    root, text="Remove Task", width=48, command=remove_task)
button_remove_task.pack()

button_save = tk.Button(root, text="Save Tasks", width=48, command=save_tasks)
button_save.pack()

button_load = tk.Button(root, text="Load Tasks", width=48, command=load_tasks)
button_load.pack()

load_tasks()  # Load tasks on application start if there are any saved tasks

root.mainloop()
