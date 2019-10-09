import time
import tkinter as tk
from tkinter.font import Font


def printString(string):
    for char in string:
        Label.configure(text=Label.cget('text') + char)
        Label.update()
        time.sleep(.1)


root = tk.Tk()
root.geometry("500x100")  # Width x Height
text = "Hello world! I am raav and you will bow down to me"
text = tk.Text(root)
Label = tk.Label(root)
myFont = Font(family="Courier New", size=12)
text.configure(font=myFont)
Label.pack()
printString(text)
root.mainloop()
