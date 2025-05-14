from tkinter import *

window = Tk()
window.title("My First GUI")
window.minsize(width=500, height=500)
window.config(padx=0, pady=10)



button1 = Button(text='Cool')
button1.grid(row=0, column=1)
button1.config(padx=10, pady=0)


button2 = Button(text='Hello World')
button2.grid(row=3, column=0)
button2.config(padx=10, pady=0)

button3 = Button(text='Come here')
button3.grid(row=3, column=2)
button3.config(padx=10, pady=0)

button4 = Button(text='Click Me')
button4.grid(row=4, column=0)
button4.config(padx=10, pady=0)

button5 = Button(text='Heyyyyy')
button5.grid(row=5, column=2)
button5.config(padx=10, pady=0)

button6 = Button(text='WOW')
button6.grid(row=5, column=4)
button6.config(padx=10, pady=0)




window.mainloop()