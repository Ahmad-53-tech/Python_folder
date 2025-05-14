import tkinter

#from tkinter import *

window = tkinter.Tk()
window.title("Ahmad's GUI") # Graphical User Interface
window.minsize(width=500, height=500)


# Label
my_label = tkinter.Label(text='Labeling', font=('Roman', 20, 'bold')) # Slant: Italic, Roman                            Weight: Normal, Bold.
# my_label.pack(side='left')
# my_label['text'] = 'Hello World'
my_label.config(text='Hello Ahmad')
my_label.pack() # centered automatically


# Button
def button_clicked(event=None):
    print("I just got clicked!")
    new_text = inputBar.get() # gets the input
    my_label['text'] = new_text

button = tkinter.Button(text='Click Me', command=button_clicked)
button.pack()

# Entry (input)
inputBar = tkinter.Entry(width=50)
inputBar.bind('<Return>', button_clicked) # Bind Enter key to run show_input
# Add some text to begin with
inputBar.insert(tkinter.END, string='Some text to begin with')
inputBar.pack()


# Text
text = tkinter.Text(height=5, width=30)
#Puts cursor in textbox
text.focus()
#Adds some text to begin with
text.insert(tkinter.END, "Example of multi-line text entry.")
# Gets current value in textbox at line 1, character 0
print(text.get("1.0", tkinter.END))
text.pack()


# Spinbox
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
spinbox = tkinter.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()




# Scale
# Called with current scale value.
def scale_used(value):
    print(value)
scale=tkinter.Scale(from_=0, to=100, command=scale_used)
scale.pack()



# Check Button
def checkbutton_used():
    # Prints 1 if the button is checked, otherwise 0
    print(checked_state.get())

# Variable to hold onto the checked state, 0 is off, 1 is on.
checked_state = tkinter.IntVar() # Automatically assigned an initial value of 0. Tracks the state of the widget.
# Create the checkbutton widget and link it to the IntVar (checked_state)
checkbutton = tkinter.Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checkbutton.pack()

#RadioButton
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked
radio_state = tkinter.IntVar()
radiobutton1 = tkinter.Radiobutton(text='Option1', value=1, variable=radio_state, command=radio_used)
radiobutton2 = tkinter.Radiobutton(text='Option2', value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


#ListBox
def listbox_used(event):
    # returns the index/position of the selected item in the list. the get method prints the actual fruit name instead of the index only.
    print(listbox.get(listbox.curselection()))

# means it can show 4 items at once before needing to scroll (a scrollable list)
listbox = tkinter.Listbox(height=4)
fruits = ['Apple', 'Pear', 'Orange', 'Banana']
for item in fruits:
    listbox.insert(fruits.index(item), item) #Puts Apple at position 0, etc.
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()



window.mainloop()
# Common Keys Used in tkinter.
# 1. If you want to run a function when a button is clicked, use the command argument.
# 2. If you want to react when a user selects from a list box, use <<ListBoxSelect>>.
# 3. If you want to react when the enter key is pressed/clicked, use <Return>.
# 4. If you want to react when a key is pressed, use <Key>.
# 5. If you want to react when a mouse is clicked, use <Button-1>.
# 6. If you want to react when a user types in a text area, use <<Modify>>.
