from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3


root = Tk()
root.title('Client manager')

conn = sqlite3.connect('client_storage.db')
c = conn.cursor()

c.execute("""
    CREATE TABLE if not exists client (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone TEXT NOT NULL,
        company TEXT NOT NULL
    );
""")


def render_client():
    rows = c.execute("SELECT * from client").fetchall()

    tree.delete(*tree.get_children())
    for row in rows:
        tree.insert('', END, row[0], values=(row[1], row[2], row[3]))


def insert(client):
    c.execute("""
        INSERT INTO client (name, phone, company) VALUES (?, ?, ?)
    """, (client['name'], client['phone'], client['company']))
    conn.commit()
    render_client()


def new_client():
    def save():
        if not name.get():
            messagebox.showerror('Error', 'The name is required')
            return
        elif not phone.get():
            messagebox.showerror('Error', 'The phone is required')
            return
        elif not company.get():
            messagebox.showerror('Error', 'The company is required')
            return

        client = {
            "name": name.get(),
            "phone": phone.get(),
            "company": company.get()
        }

        insert(client)
        top.destroy()

    top = Toplevel()
    top.title('New Client')

    # Nombre del cliente
    l_n = Label(top, text='Name')
    name = Entry(top, width=40)
    l_n.grid(row=0, column=0)
    name.grid(row=0, column=1)

    # Telefono del cliente
    l_p = Label(top, text='Phone')
    phone = Entry(top, width=40)
    l_p.grid(row=1, column=0)
    phone.grid(row=1, column=1)

    # Empresa del cliente
    l_c = Label(top, text='Company')
    company = Entry(top, width=40)
    l_c.grid(row=2, column=0)
    company.grid(row=2, column=1)

    btn_save = Button(top, text='Save', command=save)
    btn_save.grid(row=3, column=1)

    top.mainloop()


def delete_client():
    id = tree.selection()[0]

    client = c.execute("SELECT * FROM client WHERE id = ?", (id, )).fetchone()
    res = messagebox.askokcancel(
        'Sure ?', 'Are you sure that you want to delete the client ' + client[1] + ' ?')
    if res:
        c.execute("DELETE FROM client WHERE id = ?", (id, ))
        conn.commit()
        render_client()


b_new = Button(root, text='New Client', command=new_client)
b_new.grid(row=0, column=0)
b_del = Button(root, text='Delete Client', command=delete_client)
b_del.grid(row=0, column=1)


tree = ttk.Treeview(root)
tree['columns'] = ('N', 'P', 'C')
tree.column('#0', width=0, stretch=NO)
tree.column('N')
tree.column('P')
tree.column('C')

tree.heading('N', text='Name')
tree.heading('P', text='Phone')
tree.heading('C', text='Company')

tree.grid(row=1, column=0, columnspan=2)

render_client()

root.mainloop()
