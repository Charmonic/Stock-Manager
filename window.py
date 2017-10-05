from tkinter import *
from tkinter import ttk
import json

root = Tk()
root.title("Stock Manager")

tree = ttk.Treeview(root)

tree["columns"]=("category","price","stock","stock_alert","UPC")
tree.column('category', anchor='center')
tree.column('price', anchor='center')
tree.column('stock', anchor='center')
tree.column('stock_alert', anchor='center')
tree.column('UPC', anchor='center')

tree.heading("category", text="Category")
tree.heading("price", text="Price")
tree.heading("stock", text="Stock")
tree.heading("stock_alert", text="Stock minimum (alert)")
tree.heading("UPC", text="UPC")

with open('database.json') as json_data:
    data = json.load(json_data)

index = 0
for product in data:
    tree.insert("" , index, text=product["name"], values=(product["category"], product["price"], product["stock"], product["stock_alert"], product["UPC"]))
    index += 1
    

tree.pack()
root.mainloop()
