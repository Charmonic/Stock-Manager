from tkinter import *
from tkinter import ttk
from popupWindows import *
from generateNumber import *
import json

def searchWindow(tree):
    window = Tk()
    window.title("Search for a Product")
    product = tree

    #label
    txt1 = Label(window, text="Please enter UPC and/or Name")
    txt2 = Label(window, text="UPC:")
    txt3 = Label(window, text="NAME:")

    #entry
    upc = Entry(window)
    upc.insert(0,"")
    name = Entry(window)
    name.insert(0,"")
    
    #grid
    txt1.grid(row=0, column=0, padx=10)
    txt2.grid(row=1, column=0, padx=10)
    txt3.grid(row=2, column=0, padx=10)
    upc.grid(row=1, column=1, padx=10,pady=10)
    name.grid(row=2, column=1, padx=10,pady=10)

    #button
    submit = Button(window, text="Search", command=lambda: search(name.get(), upc.get(), window, tree))
    submit.grid(row=2, column=4, pady=20)

    def search(name, upc, window, tree):
        jsonfile = "database.json"
        
        if (name == "" and upc == ""):
            printErrorWindow("empty inputs")

        elif (name == ""):
            flag = True
            with open(jsonfile) as json_data:
                data = json.load(json_data)
                for elem in data:
                    if(elem['UPC'] == upc):
                        printSearchWindow("Item: " + elem['name'] + " Category: " + elem['category'] + " Price: " + str(elem['price']) +" Stock: "+ str(elem['stock']) +" Minimum: "+ str(elem['stock_alert']) +" UPC: "+ str(elem['UPC']) +" ID: "+ elem['id'])
                        break
                if(flag == False): printSearchWindow("No Item Found")
                
        elif (upc == ""):
            flag = True
            with open(jsonfile) as json_data:
                data = json.load(json_data)
                for elem in data:
                    if(elem['name'] == name):
                       printSearchWindow("Item: " + elem['name'] + " Category: " + elem['category'] + " Price: " + str(elem['price']) +" Stock: "+ str(elem['stock']) +" Minimum: "+ str(elem['stock_alert']) +" UPC: "+ str(elem['UPC']) +" ID: "+ elem['id'])
                       break
                if(flag == False): printSearchWindow("No Item Found")
        else:
            with open(jsonfile) as json_data:
                flag = True
                data = json.load(json_data)
                for elem in data:
                    if(elem['UPC'] == upc and elem['name'] == name):
                        flag = True
                        printSearchWindow("Item: " + elem['name'] + " Category: " + elem['category'] + " Price: " + str(elem['price']) +" Stock: "+ str(elem['stock']) +" Minimum: "+ str(elem['stock_alert']) +" UPC: "+ str(elem['UPC']) +" ID: "+ elem['id'])
                        break
                if(flag == False): printSearchWindow("No Item Found")

        
