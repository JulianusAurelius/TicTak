import tkinter
from tkinter.constants import *

process = tkinter.Tk()
process.title("GUI")
windowframe = tkinter.Frame(process, borderwidth=100)
sumtxt = tkinter.Label(windowframe, text="GUI")
windowframe.pack()
sumtxt.pack()
process.mainloop()
# Can we drink the Rosé now?
