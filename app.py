# Crie um sistema que permita ao usuário adicionar, visualizar, atualizar e excluir tarefas.

from mongo_service import list_tasks, delete_task, save_task
import tkinter as tk
from tkinter import ttk
root = tk.Tk()

def openCreateTask():
    root.destroy()
    import create_activity

def reloadPage():
    root.destroy()
    import app

def deleteTask():
    curItem = tree.focus()
    id = tree.item(curItem)["values"][0]
    delete_task(id)
    selectedItem = tree.selection()[0]
    tree.delete(selectedItem)

def saveTask(title, description):
    save_task({
        "title": title,
        "description": description,
    })

def importTasks():
    with open ("list.txt", 'r') as tasks:
        for task in tasks:
            taskSplitted = task.split(",")
            saveTask(taskSplitted[0], taskSplitted[1])

    reloadPage()

root.title("Task Manager")

tree = ttk.Treeview(root, column=("c1", "c2", "c3", "c4"), show='headings', height=5)

tree.column("# 1", anchor="center")
tree.heading("# 1", text="ID")
tree.column("# 2", anchor="center")
tree.heading("# 2", text="Title")
tree.column("# 3", anchor="center")
tree.heading("# 3", text="Description")

tasks = list_tasks()

index = 1
for item in tasks:
    id = item["_id"]
    title = item["title"]
    description = item["description"]


    tree.insert('', 'end', text=index, values=(id, title, description, ))
    index += 1

tree.pack()

bt = tk.Button(root, text="Create New Task", command=openCreateTask)
bt.place(x=105, y=160)

bt = tk.Button(root, text="Delete Task", command=deleteTask)
bt.place(x=250, y=160)

bt = tk.Button(root, text="Import Task", command=importTasks)
bt.place(x=350, y=160)

root.geometry("800x400")
root.mainloop()
