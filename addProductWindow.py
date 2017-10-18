from tkinter import *
from tkinter import ttk
from generateNumber import *
from popupWindows import *
import json

jsonfile = "database.json"

def loadJson():
    with open(jsonfile) as json_data:
        return json.load(json_data)

def createNewProduct(name, category, price, stock, stock_alert, upc, windowAdd, tree):
    if name == "" or category == "" or price == "" or stock == "" or stock_alert == "" or upc == "":
        printErrorWindow("empty input")
    #TODO need to verify all the input 
    else:
        newProduct = {}
        newProduct["id"] = generateId() #TODO
        newProduct["name"] = name
        newProduct["category"] = category
        newProduct["price"] = price
        newProduct["stock"] = stock
        newProduct["stock_alert"] = stock_alert
        newProduct["UPC"] = upc

        data = loadJson()            
        data.append(newProduct)
        with open(jsonfile, 'w') as json_data:
            json.dump(data, json_data, indent=4)

        windowAdd.destroy()
        printValidationWindow("Your product is now on the database.")
        
        #refresh result automatically
        for product in tree.get_children():
            tree.delete(product)
    
        with open(jsonfile) as json_data:
            data = json.load(json_data)    
        index = 0
        for product in data:
            tree.insert("" , index, text=product["name"], values=(product["name"], product["category"], product["price"], product["stock"], product["stock_alert"], product["UPC"], product["id"]))
            index += 1
        
def fulfillEntryRandom(name, category, price, stock, stock_alert, upc):
    name.delete(0,END)
    category.delete(0,END)
    price.delete(0,END)
    stock.delete(0,END)
    stock_alert.delete(0,END)
    upc.delete(0,END)
    name.insert(0, generateNameProduct())
    category.insert(0, "Vegetables")
    price.insert(0, generatePrice())
    stk = generateStockandStockLimit()
    stock.insert(0, stk[0])
    stock_alert.insert(0, stk[1])
    upc.insert(0, generateUPC())

def addProduct(tree):
    windowAdd = Tk()
    windowAdd.title("Add a new product")

    #label
    txt1 = Label(windowAdd, text="Name:")
    txt2 = Label(windowAdd, text="Category:")
    txt3 = Label(windowAdd, text="Price:")
    txt4 = Label(windowAdd, text="Stock:")
    txt5 = Label(windowAdd, text="Stock minimum:")
    txt6 = Label(windowAdd, text="UPC:")

    #entry
    name = Entry(windowAdd)
    category = Entry(windowAdd)
    price = Entry(windowAdd)
    stock = Entry(windowAdd)
    stock_alert = Entry(windowAdd)
    upc = Entry(windowAdd)

    #grid
    txt1.grid(row=1, sticky=E, padx=10)
    txt2.grid(row=2, sticky=E, padx=10)
    txt3.grid(row=3, sticky=E, padx=10)
    txt4.grid(row=1, column=3, padx=40)
    txt5.grid(row=2, column=3, padx=40)
    txt6.grid(row=3, column=3, padx=40)
    name.grid(row=1, column=2, padx=10,pady=10)
    category.grid(row=2, column=2, padx=10,pady=10)
    price.grid(row=3, column=2, padx=10,pady=10)
    stock.grid(row=1, column=4, padx=10,pady=10)
    stock_alert.grid(row=2, column=4, padx=10,pady=10)
    upc.grid(row=3, column=4, padx=10,pady=10)

    #button
    submit = Button(windowAdd, text="Submit", command=lambda: createNewProduct(name.get(), category.get(), price.get(), stock.get(), stock_alert.get(), upc.get(), windowAdd, tree))
    generate = Button(windowAdd, text="Generate random", command=lambda: fulfillEntryRandom(name, category, price, stock, stock_alert, upc))
    submit.grid(row=4, column=4, pady=20)
    generate.grid(row=4, column=2, padx=10)
