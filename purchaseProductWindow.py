from tkinter import *
from tkinter import ttk
from popupWindows import *
from generateNumber import *

def purchaseWindow(tree):
    window = Tk()
    window.title("Purchase a product")
    product = tree.item(tree.selection()[0])



    #label
    txt1 = Label(window, text="Product: " + product["values"][0])
    txt2 = Label(window, text="Price: " + product["values"][2])
    txt4 = Label(window, text="Amount")

    #entry
    amount = Entry(window)
    amount.insert(0,product["values"][3])

    #grid
    txt1.grid(row=1, sticky=E, padx=10)
    txt2.grid(row=2, sticky=E, padx=10)
    txt4.grid(row=1, column=3, padx=40)
    amount.grid(row=1, column=4, padx=10,pady=10)

    #button
    submit = Button(window, text="Purchase", command=lambda: purchase(amount.get(), window, tree))
    submit.grid(row=2, column=4, pady=20)

    def purchase(price, window, tree):
        if amount == "":
            printErrorWindow("empty input")

        elif isNumber(price) == False:
            printErrorWindow("incorrect price")

        else:
            cStock = product["values"][3]
            price = product["values"][2]
            pStock = int(amount.get())
            nStock = str(int(product["values"][3]) - pStock)
            profit = (cStock - pStock)*price
            tree.item(tree.selection()[0], values=(product["values"][0],product["values"][1],product["values"][2],nStock,product["values"][4],product["values"][5],product["values"][6]))
            printValidationWindow("You have made a purchase. Press save to Confirm purchase")
    
        window.destroy()
