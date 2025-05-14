import tkinter
from tkinter import Button

# from tkinter import *

window = tkinter.Tk()
window.title("My First GUI")
window.minsize(width=500, height=500)
window.config(padx=20, pady=20)

#Label
my_label = tkinter.Label(text='Labeling', font=('Roman', 20, 'bold')) # Slant: Italic, Roman                            Weight: Normal, Bold.
# my_label.pack(side='left')
# my_label['text'] = 'Hello World'
my_label.config(text='Hello Ahmad', padx=120, pady=120)
my_label.place(x=100, y=0)


#If you're only placing one widget, it'll still appear top-left, no matter what row or column you use - unless other widgets help fill out the grid.
my_label.grid(column=0, row=0)

button = tkinter.Button(text='Click Me')
button.grid(column=0, row=1)

button = tkinter.Button(text='Heyyyyyy')
button.grid(column=2, row=2)







window.mainloop()