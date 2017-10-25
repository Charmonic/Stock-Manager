from tkinter import *
from tkinter import ttk
from popupWindows import *
from generateNumber import *
import os.path

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
    txt1.grid(row=1, column=1, padx=10)
    txt2.grid(row=1, column=2, padx=10)
    txt4.grid(row=2, column=1, padx=40)
    amount.grid(row=2, column=2, padx=10,pady=10)

    #button
    submit = Button(window, text="Purchase", command=lambda: purchase(amount.get(), window, tree))
    submit.grid(row=2, column=4, pady=20)

    def purchase(price, window, tree):
        if amount == "":
            printErrorWindow("empty input")

        elif isNumber(price) == False:
            printErrorWindow("incorrect price")

        else:
            cStock = float(product["values"][3])
            price = float(product["values"][2])
            pStock = float(amount.get())
            nStock = str(float(product["values"][3]) - pStock)
            newStock = cStock - pStock
            profit = pStock*price
            fProfit = 0.0

            #handles profit
            my_file = 'profit.txt'
            if os.path.isfile(my_file):
                with open(my_file,'r+') as f:
                    first_line = f.readline()
                    fProfit = float(first_line) + profit
                    f.seek(0)
                    f.truncate()
                    f.write(str(fProfit))
                    f.close()
            else:
                open(my_file,'w')
                file.write(str(profit + fProfit))
                file.close()

            #handles last transaction
            my_file = 'purchase.txt'
            if os.path.isfile(my_file):
                with open(my_file,'r+') as f:
                    f.seek(0)
                    f.truncate()
                    f.write("You purchased " + str(int(pStock))+ " of " + product["values"][0])
                    f.close()
            else:
                open(my_file,'w')
                file.write("You purchased " + str(int(pStock)) + " of " + product["values"][0])
                file.close()
            
            tree.item(tree.selection()[0], values=(product["values"][0],product["values"][1],product["values"][2],int(newStock),product["values"][4],product["values"][5],product["values"][6]))
            printValidationWindow("You have made a purchase. Press save to Confirm purchase")
    
        window.destroy()
            
