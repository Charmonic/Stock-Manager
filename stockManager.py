from tkinter import *
from tkinter import ttk
from addProductWindow import *
import json

jsonfile = "database.json"

def loadJson():
    with open(jsonfile) as json_data:
        return json.load(json_data)

def refreshResults(window):
    window.destroy()
    mainWindow()


######## Main ########
def mainWindow():
    root = Tk()
    root.title("Stock Manager")

    tree = ttk.Treeview(root)

    #define columns
    tree["columns"]=("category","price","stock","stock_alert","UPC")
    tree.column('category', anchor='center')
    tree.column('price', anchor='center')
    tree.column('stock', anchor='center')
    tree.column('stock_alert', anchor='center')
    tree.column('UPC', anchor='center')

    #define name of the columns headers
    tree.heading("category", text="Category")
    tree.heading("price", text="Price")
    tree.heading("stock", text="Stock")
    tree.heading("stock_alert", text="Stock minimum (alert)")
    tree.heading("UPC", text="UPC")

    #read json file
    with open(jsonfile) as json_data:
        data = json.load(json_data)

    #insert all the products in the tree view
    index = 0
    for product in data:
        tree.insert("" , index, text=product["name"], values=(product["category"], product["price"], product["stock"], product["stock_alert"], product["UPC"]))
        index += 1
        
    tree.pack(side=TOP, padx=10, pady=10)

    #button "Add a new product"
    buttonAdd = Button(root, text="Add a new product", command=addProduct)
    buttonRefresh = Button(root, text="Refresh", command=lambda: refreshResults(root))
    buttonAdd.pack(side=LEFT, padx=10, pady=10)
    buttonRefresh.pack(side=LEFT, padx=10, pady=10)

    root.mainloop()

mainWindow()
