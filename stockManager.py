from tkinter import *
from tkinter import ttk
from addProductWindow import *
from popupWindows import *
import json

jsonfile = "database.json"

def loadJson():
    with open(jsonfile) as json_data:
        return json.load(json_data)

def refreshResults(window):
    window.destroy()
    mainWindow()

def deleteProduct(tree):
    if(len(tree.selection()) == 0):
        printErrorWindow("No row selected")
    else:
        selected_item = tree.selection()[0] #get selected item    
        tree.delete(selected_item)
    

def saveJson(tree):
    print()

######## Main ########
def mainWindow():
    root = Tk()
    root.title("Stock Manager")

    tree = ttk.Treeview(root)
    tree["show"] = "headings"

    #define columns
    tree["columns"]=("name","category","price","stock","stock_alert","UPC", "id")
    tree.column('category', anchor='center')
    tree.column('price', anchor='center')
    tree.column('stock', anchor='center')
    tree.column('stock_alert', anchor='center')
    tree.column('UPC', anchor='center')
    tree.column('id', anchor='center')

    #define name of the columns headers
    tree.heading("name", text="Name")
    tree.heading("category", text="Category")
    tree.heading("price", text="Price")
    tree.heading("stock", text="Stock")
    tree.heading("stock_alert", text="Stock minimum (alert)")
    tree.heading("UPC", text="UPC")
    tree.heading("id", text="id")

    #read json file
    with open(jsonfile) as json_data:
        data = json.load(json_data)

    #insert all the products in the tree view
    index = 0
    for product in data:
        tree.insert("" , index, text=product["name"], values=(product["name"], product["category"], product["price"], product["stock"], product["stock_alert"], product["UPC"], product["id"]))
        index += 1
        
    tree.pack(side=TOP, padx=10, pady=10)

    #buttons
    frame = Frame(root)
    frame.pack(side=LEFT, padx=10, pady=10)
    buttonWidth = 25
    
    buttonAdd = Button(frame, text="Add a new product", command=addProduct, width = buttonWidth)
    buttonDelete = Button(frame, text="Delete selected element", command=lambda: deleteProduct(tree), width = buttonWidth)
    buttonRefresh = Button(frame, text="Refresh", command=lambda: refreshResults(root), width = buttonWidth)
    buttonSave = Button(frame, text="Save in database", command=lambda: saveJson(tree), width = buttonWidth)
    
    buttonAdd.grid(row=0, column=0)
    buttonDelete.grid(row=0, column=1, padx=20)
    buttonRefresh.grid(row=1, column=0, pady=10)
    buttonSave.grid(row=1, column=1, padx=20)

    root.mainloop()

mainWindow()
