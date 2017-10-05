from tkinter import *
import ttk

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

tree.insert("" , 0, text="Strawberry", values=("Fruits",1.25, 100, 20, "123456789012"))

tree.pack()
root.mainloop()
