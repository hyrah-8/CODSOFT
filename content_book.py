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
        contact.append(("Nmae":name,"Phone":phone, "Email": email, "Address": address))
        clear_entries()
        update_contact_list()
    else:
        messagebox.showerror("Error","name and phone feild are required")


def update_contact_list():
    contact_list.delete(0,tk.END)
    for contact in contact:
        contact_list.insert(tk.END,f"{contact['name]} - {contact ['phone']}")