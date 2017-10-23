from tkinter import *
from tkinter import ttk
from popupWindows import *
from generateNumber import *

def modificationWindow(tree):
    window = Tk()
    window.title("Modify a product")
    product = tree.item(tree.selection()[0])
    
    #label
    txt1 = Label(window, text="Name:")
    txt2 = Label(window, text="Price:")
    txt4 = Label(window, text="Stock:")
    txt5 = Label(window, text="Stock minimum:")

    #entry
    name = Entry(window)
    price = Entry(window)    
    stock = Entry(window)
    stock_alert = Entry(window)
    upc = Entry(window) 
    name.insert(0,product["values"][0])
    price.insert(0,product["values"][2])
    stock.insert(0,product["values"][3])
    stock_alert.insert(0,product["values"][4])
    
    #grid
    txt1.grid(row=1, sticky=E, padx=10)
    txt2.grid(row=2, sticky=E, padx=10)
    txt4.grid(row=1, column=3, padx=40)
    txt5.grid(row=2, column=3, padx=40)
    name.grid(row=1, column=2, padx=10,pady=10)
    price.grid(row=2, column=2, padx=10,pady=10)
    stock.grid(row=1, column=4, padx=10,pady=10)
    stock_alert.grid(row=2, column=4, padx=10,pady=10)

    #button
    submit = Button(window, text="Apply modifications", command=lambda: modify(product, name.get(), price.get(), stock.get(), stock_alert.get(), window, tree))
    submit.grid(row=4, column=4, pady=20)

def modify(product, name, price, stock, stock_alert, window, tree):
    if name == "" or price == "" or stock == "" or stock_alert == "":
        printErrorWindow("empty input")
        
    elif isNumber(price) == False or isNumber(stock) == False or isNumber(stock_alert) == False:
        printErrorWindow("incorrect input: 'price', 'stock' and 'stock minimum' must be numbers")

    elif isNumber(name) == True:
        printErrorWindow("name must not be a number")

    else:
        tree.item(tree.selection()[0], values=(name, product["values"][1], price, stock, stock_alert, product["values"][5], product["values"][6]))
        printValidationWindow("The product has been temporary modified.\nClick on save to push the modifications to the database")

    window.destroy()
