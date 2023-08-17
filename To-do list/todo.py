from tkinter import *
from tkinter import messagebox
import pickle

root = Tk()
root.title("To-Do List")

def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(END, task)
        entry_task.delete(0, END)
    else:
        messagebox.showwarning(title="Warning!", message="Enter a task.")

def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        messagebox.showwarning(title="Warning!", message="Select a task.")

def load_tasks():
    try:
        tasks = pickle.load(open("tasks.dat", "rb"))
        listbox_tasks.delete(0, END)
        for task in tasks:
            listbox_tasks.insert(END, task)
    except:
        messagebox.showwarning(title="Warning!", message="Cannot find tasks")

def save_tasks():
    tasks = listbox_tasks.get(0, listbox_tasks.size())
    pickle.dump(tasks, open("tasks.dat", "wb"))


frame_tasks = Frame(root)
frame_tasks.grid()

# listbox_tasks = Listbox(frame_tasks, height=10, width=50)
listbox_tasks = Listbox(frame_tasks, height=10, width=50)

listbox_tasks.grid(row=0, column=0, rowspan=5)

scrollbar_tasks = Scrollbar(frame_tasks)
scrollbar_tasks.grid(row=0, column=1, rowspan=10,sticky=N+S+W)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = Entry(root, width=50)
entry_task.insert(0, "Enter your task here")

entry_task.grid(row=0, column=1)

button_add_task = Button(root, text="Add task", width=48, command=add_task)
button_add_task.grid(row=1, column=0)

button_delete_task = Button(root, text="Delete task", width=48, command=delete_task)
button_delete_task.grid(row=2, column=0)

button_load_tasks = Button(root, text="Load tasks", width=48, command=load_tasks)
button_load_tasks.grid(row=1, column=1)

button_save_tasks = Button(root, text="Save tasks", width=48, command=save_tasks)
button_save_tasks.grid(row=2, column=1)

root.mainloop()