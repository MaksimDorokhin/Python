from tkinter import *

def getItemsPerLine(dropdownValues, listboxWidget):
    listboxWidget.delete(1.0, END)
    for item in dropdownValues:
       listboxWidget.insert(INSERT, item)