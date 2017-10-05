from tkinter import *
from tkinter import ttk
import json

jsonfile = "database.json"

def printErrorWindow(error_text):
    alertWindow = Tk()
    alertWindow.title("Error")
    alertWindow.configure(background="red")     
    txt = Label(alertWindow, text=("Error:", error_text))
    txt.configure(background="red", fg="white", font="bold")
    txt.pack(padx=50, pady=50)

def printValidationWindow(text):
    window = Tk()
    window.title("Error")
    window.configure(background="green")     
    txt = Label(window, text=text)
    txt.configure(background="green", fg="white", font="bold")
    txt.pack(padx=50, pady=50)

def loadJson():
    with open(jsonfile) as json_data:
        return json.load(json_data)


#TODO
def generateId():
    return "0"

    
def createNewProduct(name, category, price, stock, stock_alert, upc, windowAdd):
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
        printValidationWindow("Your product is now on the database.\nPlease click on the refresh button") 
    

def addProduct():
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
    submit = Button(windowAdd, text="Submit", command=lambda: createNewProduct(name.get(), category.get(), price.get(), stock.get(), stock_alert.get(), upc.get(), windowAdd))
    submit.grid(row=4, column=4, pady=20)
    
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
