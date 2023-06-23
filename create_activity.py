# Desenvolver um sistema de gerenciamento de tarefas utilizando a linguagem de programação Python, um banco de dados e a biblioteca Tkinter para criação das interfaces gráficas.

from mongo_service import save_task
import tkinter as tk
root = tk.Tk()

def openListTask():
    root.destroy()
    import app

def saveTask():
    title = str(make_title.get())
    description = str(make_description.get())

    save_task({
        "title": title,
        "description": description,
    })

    openListTask()

root.title("Task Manager")

lbl = tk.Label(root, text = "title: ")
lbl.place(x=10, y=30)
make_title = tk.Entry(root)
make_title.place(x=105, y=30)

lbl = tk.Label(root, text = "description: ")
lbl.place(x=10, y=50)
make_description = tk.Entry(root)
make_description.place(x=105, y=50)


bt = tk.Button(root, text="Confirm", command=saveTask)
bt.place(x=105, y=160)

root.geometry("800x400")
root.mainloop()

