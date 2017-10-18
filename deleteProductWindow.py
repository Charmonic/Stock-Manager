from tkinter import *
from tkinter import ttk
from popupWindows import *

def confirmationDelete(tree):
    window = Tk()
    window.title("Confirmation")
    frame = Frame(window)
    txt = Label(window, text="Are you sure you want to delete the selected product?")
    txt.configure(font="bold")
    yes = Button(frame, text="Yes", width=15, command=lambda: delete(tree, window))
    cancel = Button(frame, text="Cancel", width=15, command=lambda: window.destroy())
    txt.pack(padx=50, pady=50)
    frame.pack()
    yes.grid(row=0, column=0, padx=50)
    cancel.grid(row=0, column=1, padx=50, pady=20)

def delete(tree, window):
    tree.delete(tree.selection()[0])
    window.destroy()
    printValidationWindow("The product has been temporary deleted.\nClick on save to push the modifications to the database")
