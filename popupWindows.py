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
    window.title("Error")
    window.configure(background="green")     
    txt = Label(window, text=text)
    txt.configure(background="green", fg="white", font="bold")
    txt.pack(padx=50, pady=50)