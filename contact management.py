import tkinter as tk

FILE = "contacts.txt"

def load():
    try:
        with open(FILE) as f:
            return [line.strip().split(",") for line in f]
    except:
        return []

contacts = load()

def save():
    with open(FILE, "w") as f:
        for c in contacts:
            f.write(",".join(c) + "\n")

def add():
    contacts.append([name.get(), phone.get(), email.get()])
    save()
    refresh()

def delete():
    contacts.pop(listbox.curselection()[0])
    save()
    refresh()

def refresh():
    listbox.delete(0, tk.END)
    for c in contacts:
        listbox.insert(tk.END, f"{c[0]} | {c[1]} | {c[2]}")

root = tk.Tk()
root.title("Contact Manager")

name = tk.Entry(root); name.pack()
phone = tk.Entry(root); phone.pack()
email = tk.Entry(root); email.pack()

tk.Button(root, text="Add", command=add).pack()
tk.Button(root, text="Delete", command=delete).pack()

listbox = tk.Listbox(root, width=50)
listbox.pack()

refresh()
root.mainloop()
