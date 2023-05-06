from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Gestor de clientes')

tree = ttk.Treeview(root)
tree['columns'] = ('Name', 'Phone number', 'Company')

# tree.column('#0')
tree.column('#0', width=0, stretch=NO)
tree.column('Name')
tree.column('Phone number')
tree.column('Company')

# tree.heading('#0', text='id')
tree.heading('#0')
tree.heading('Name', text='Name')
tree.heading('Phone number', text='Phone number')
tree.heading('Company', text='Company')


tree.grid(row=0, column=0)

tree.insert('', END, 'lala', values=(
    'Uno', 'Dos', 'Tres'), text='chanchito feliz')
tree.insert('', END, 'lele', values=(
    'Cuatro', 'Cinco', 'Seis'), text='chanchito triste')
tree.insert('', END, 'lili', values=('4', '5', '6'), text='Hijo')


root.mainloop()
