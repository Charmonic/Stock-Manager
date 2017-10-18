from tkinter import *
from tkinter import ttk
from addProductWindow import *
from deleteProductWindow import *
from popupWindows import *
import json

jsonfile = "database.json"

def loadJson():
    with open(jsonfile) as json_data:
        return json.load(json_data)

def refreshResults(tree):
    for product in tree.get_children():
        tree.delete(product)
    
    with open(jsonfile) as json_data:
        data = json.load(json_data)    
    index = 0
    for product in data:
        tree.insert("" , index, text=product["name"], values=(product["name"], product["category"], product["price"], product["stock"], product["stock_alert"], product["UPC"], product["id"]))
        index += 1
    printValidationWindow("List refreshed")

def deleteProduct(tree):
    if(len(tree.selection()) == 0):
        printErrorWindow("No row selected")
    else:
        selected_item = tree.selection()[0] #get selected item
        confirmationDelete(tree)

def saveJson(tree):
    newJson = []
    for product in tree.get_children():

        prod = {}
        prod["name"] = tree.item(product)["values"][0]
        prod["category"] = tree.item(product)["values"][1]
        prod["price"] = tree.item(product)["values"][2]
        prod["stock"] = tree.item(product)["values"][3]
        prod["stock_alert"] = tree.item(product)["values"][4]
        prod["UPC"] = str(tree.item(product)["values"][5])
        prod["id"] = tree.item(product)["values"][6]
        newJson.append(prod)

    with open(jsonfile, "w") as json_data:
        json.dump(newJson, json_data, indent=4)
        printValidationWindow("The database has been saved")

        
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
    
    buttonAdd = Button(frame, text="Add a new product", command=lambda:addProduct(tree), width = buttonWidth)
    buttonDelete = Button(frame, text="Delete selected element", command=lambda: deleteProduct(tree), width = buttonWidth)
    buttonRefresh = Button(frame, text="Refresh", command=lambda: refreshResults(tree), width = buttonWidth)
    buttonSave = Button(frame, text="Save in database", command=lambda: saveJson(tree), width = buttonWidth)
    
    buttonAdd.grid(row=0, column=0)
    buttonDelete.grid(row=0, column=1, padx=20)
    buttonRefresh.grid(row=1, column=0, pady=10)
    buttonSave.grid(row=1, column=1, padx=20)

    root.mainloop()
    

mainWindow()
