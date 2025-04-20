import customtkinter
from tkinter import Listbox, END, SINGLE, messagebox

app = customtkinter.CTk()
app.title('To-Do List')
app.geometry('350x500')
app.config(bg='#000053')

font1 = ('Times New Roman', 30, 'bold')
font2 = ('Times New Roman', 18, 'bold')
font3 = ('Times New Roman', 17, 'bold')


def add_task():
    task = task_entry.get()
    if task.strip():
        tasks_list.insert(END, task)
        task_entry.delete(0, END)
        save_tasks()
    else:
        messagebox.showerror('Error', 'Enter a task.')

def update_task():
    selected = tasks_list.curselection()
    new_text = task_entry.get().strip()
    if selected and new_text:
        tasks_list.delete(selected[0])
        tasks_list.insert(selected[0], new_text)
        task_entry.delete(0, END)
        save_tasks()
    else:
        messagebox.showerror('Error', 'Select a task and enter updated text.')


def on_task_select(event):
    selected = tasks_list.curselection()
    if selected:
        task_entry.delete(0, END)
        task_entry.insert(0, tasks_list.get(selected[0]))


def remove_task():
    selected = tasks_list.curselection()
    if selected:
        tasks_list.delete(selected[0])
        task_entry.delete(0, END)  # 👈 Clear the input field here
        save_tasks()
    else:
        messagebox.showerror('Error', 'Choose a task to delete.')

def save_tasks():
    with open("tasks.txt", "w") as f:
        tasks = tasks_list.get(0, END)
        for task in tasks:
            f.write(task + "\n")

def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            tasks = f.readlines()
            for task in tasks:
                tasks_list.insert(END, task.strip())
    except FileNotFoundError:
        pass


title_label = customtkinter.CTkLabel(app, font=font1, text='To-Do List', text_color='#fff', bg_color='#09112e')
title_label.place(x=100, y=20)

add_button = customtkinter.CTkButton(app, command=add_task, font=font2, text_color='#fff', text='Add task',
                                     fg_color='#06911f', hover_color='#06911f', bg_color='#09112e',
                                     cursor='hand2', corner_radius=5, width=120)
add_button.place(x=40, y=80)

remove_button = customtkinter.CTkButton(app, command=remove_task, font=font2, text_color='#fff', text='Remove task',
                                        fg_color='#96061c', hover_color='#96061c', bg_color='#09112e',
                                        cursor='hand2', corner_radius=5)
remove_button.place(x=110, y=450)

update_button = customtkinter.CTkButton(app, command=update_task, font=font2, text_color='#fff', text='Update task',
                                        fg_color='#1e90ff', hover_color='#1c86ee', bg_color='#09112e',
                                        cursor='hand2', corner_radius=5)
update_button.place(x=180, y=80)


task_entry = customtkinter.CTkEntry(app, font=font2, text_color='#000', fg_color='#fff',
                                    border_color='#fff', width=280)
task_entry.place(x=40, y=120)

# ✅ Use Listbox (not CTkTextbox!) to allow item selection & deletion
tasks_list = Listbox(app, font=font3, width=35, height=15, selectmode=SINGLE)
tasks_list.place(x=55, y=260)
tasks_list.bind('<<ListboxSelect>>', on_task_select)

load_tasks()

app.mainloop()
