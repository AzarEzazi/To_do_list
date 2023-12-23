import tkinter
import tkinter.messagebox

root = tkinter.Tk()
root.title('TO do list')

frame_tasks = tkinter.Frame(root)
frame_tasks.pack()


# created functions
def add_tasks():
    task = entry_tasks.get()
    if task != "":
        listbox_tasks.insert(tkinter.END, task)
        entry_tasks.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showinfo("warning!", "please enter  the task")


def delete_tasks():
    try:
        index_task = listbox_tasks.curselection()[0]
        selected_task = listbox_tasks.get(index_task)
        listbox_tasks.delete(index_task)
        with open("test.txt", "r") as file:
            lines = file.readlines()

        with open("test.txt", "w") as file:
            for line in lines:
                if line.strip() != selected_task:
                    file.write(line)
    except IndexError:
        tkinter.messagebox.showinfo("warning!", "please select  the task")


def edit_tasks():
    try:
        task_index = listbox_tasks.curselection()[0]
        task_text = listbox_tasks.get(task_index)
        entry_tasks.delete(0, tkinter.END)
        entry_tasks.insert(0, task_text)
        listbox_tasks.delete(task_index)
    except:
        tkinter.messagebox.showinfo("warning!", "please select  the task to edit")


def load_tasks():
    try:
        with open("test.txt", "r") as file:
            tasks = file.readlines()

            listbox_tasks.delete(0, tkinter.END)
            for task in tasks:
                task = task.strip()
                listbox_tasks.insert(tkinter.END, task)
    except:
        tkinter.messagebox.showinfo("warning!", "please create  the task")


def exit_root():
    exit_root = tkinter.messagebox.askyesno("Exit", "Do you want to exit ?")
    if exit_root > 0:
        root.destroy()
        return


listbox_tasks = tkinter.Listbox(frame_tasks, height=30, width=90)
listbox_tasks.pack(side=tkinter.LEFT)

scrollbar = tkinter.Scrollbar(frame_tasks)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

listbox_tasks.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox_tasks.yview)

entry_tasks = tkinter.Entry(root, width=92)
entry_tasks.pack()

# created button
button_add_tasks = tkinter.Button(root, text="Add task", width=78, command=lambda: add_tasks())
button_add_tasks.pack()

button_delete_tasks = tkinter.Button(root, text="Delete task", width=78, command=lambda: delete_tasks())
button_delete_tasks.pack()

button_edit_tasks = tkinter.Button(root, text="Edit task", width=78, command=lambda: edit_tasks())
button_edit_tasks.pack()

button_load_task = tkinter.Button(root, text="load root", width=78, command=lambda: load_tasks())
button_load_task.pack()

button_exit_root = tkinter.Button(root, text="Exit root", width=78, command=lambda: exit_root())
button_exit_root.pack()

root.mainloop()
