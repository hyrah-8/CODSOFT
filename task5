import tkinter as tk
from tkinder import messagebox

root =tk.Tk()
root.title("contact book")

contacts=[]

def add_contact():
    name=name_entry.get()
    phone=phone_entry.get()
    email=email_entry.get()
    address=address_entry.get()
    if name and phone:
        contact.append(("Name":name,"Phone":phone, "Email": email, "Address": address))
        clear_entries()
        update_contact_list()
    else:
        messagebox.showerror("Error","name and phone feild are required")


def update_contact_list():
    contact_list.delete(0,tk.END)
    for contact in contact:
        contact_list.insert(tk.END,f"{contact['name']} - {contact ['phone']}")

def search_contact():
    search_tern = search_entry.get()
    contact_list.delete(0,tk.END)
    for contact in contacts:
        if searh_tern.lower() in contact['name'].lower() or search_tern in contact ['phone']:
            contact_list.insert(tk.END,f"{contact['name']} - {contact['phone']}")


def update_selected_contact():
    selected_index = contact_list.curselection()
    if selected_index:
        selected_index = selected_index[0]
        name=name_entry.get()
        phone=phone_entry.get()
        email=email_entry.get()
        address=address_entry.get()
         if name and phone:
              contact.append(("Nmae":name,"Phone":phone, "Email": email, "Address": address))
              clear_entries()
               update_contact_list()
         else:
                messagebox.showerror("Error","name and phone feild are required")
        
def delete_selected_contact():
     selected_index = contact_list.curselection()
     if selected_index:
        selected_list = selected_index[0]
        del contact [selected_index]
        clear_entries()
        update_contact_list()

def clear_entries ():
    name_entry.delete(0,tk.END)
    phone_entry.delete(0,tk.END)
    email_entry.delete(0,tk.END)
    address_entry.delete(0,tk.END)


name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

phone_label = tk.Label(root, text="Phone:")
phone_label.grid(row=1, column=0)
phone_entry = tk.Entry(root)
phone_entry.grid(row=1, column=1)

email_label = tk.Label(root, text="Email:")
email_label.grid(row=0, column=0)
email_entry = tk.Entry(root)
email_entry.grid(row=0, column=1)

address_label = tk.Label(root, text="Address:")
address_label.grid(row=0, column=0)
address_entry = tk.Entry(root)
address_entry.grid(row=0, column=1)

add_button =tk.Button(root,text="Add Button",comand=add_contact)
add_button.grid(row=0,column=2)

update_button =tk.Button(root,text="Update Button",comand=update_selected_contact)
update_button.grid(row=1,column=2)

delete_button =tk.Button(root,text="Delete Button",comand=delete_selected_contact)
delete_button.grid(row=2,column=2)


search_label = tk.Label(root, text="Search:")
search_label.grid(row=4, column=0)
search_entry = tk.Entry(root)
search_entry.grid(row=4, column=1)
search_button =tk.Button(root,text="Search",comand=search_contact)
search_button.grid(row=4,column=2)

contact_list = tk.listbox(root,width=40)
contact_list.grid(row=5, column=0,columnspan=3)

root.mainloop()





        



