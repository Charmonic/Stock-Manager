from tkinter import *
from tkinter import ttk

def printErrorWindow(error_text):
    alertWindow = Tk()
    alertWindow.title("Error")
    alertWindow.configure(background="red")     
    txt = Label(alertWindow, text=("Error:", error_text))
    txt.configure(background="red", fg="white", font="bold")
    txt.pack(padx=50, pady=50)

def printValidationWindow(text):
    window = Tk()
    window.title("Success")
    window.configure(background="green")     
    txt = Label(window, text=("Success:", text))
    txt.configure(background="green", fg="white", font="bold")
    txt.pack(padx=50, pady=50)

def printProfitWindow(text):
    window = Tk()
    window.title("Profit this session")
    window.configure(background="green")     
    txt = Label(window, text=(text))
    txt.configure(background="green", fg="white", font="bold")
    txt.pack(padx=50, pady=50)

def printSearchWindow(text):
    window = Tk()
    window.title("Search Results")

    #label
    txt1 = Label(window, text=("The First Result Matching Your Query is: "))
    txt2 = Label(window, text=(text))
    
    #grid
    txt2.grid(row=1, column=1, padx=10)
    txt2.grid(row=0, column=1, padx=10)
