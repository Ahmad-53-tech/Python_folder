#You are tasked with creating a feedback form using tkinter
#Requirements:
# 1. Display the title "Feedback Form"
# 2. Include a text input field where users can input their name and submit it by pressing the enter key, after submitting, display a label that shows the entered name.
# 3. Add a spinbox that allows users to select a rating between one and ten. Display the selected rating below the spinbox.
# 4. Add a check button to ask if the user would like to receive notifications, below the check, display whether the user is subscribed to notifications.
# 5. Include a list box, where users can select a category for their feedback, the listbox should contain "Feedback", "Suggestion", "complaint", display the selected
#category below the listbox
# 6. Create a 'submit' button, that when clicked displays a summary of all the entered information.
from tkinter import *

window = Tk()
window.title("Feedback Form")
window.minsize(width=500, height=500)
window.config(padx=10, pady=10)

my_label = Label(text="FEEDBACK FORM", font=("Italic", 20, "bold"))
my_label.grid(column=0, row=0, pady=10, columnspan=2)

def button_clicked(event=None):
    new_text = inputBar.get()
    user_name["text"] = f"Hello {new_text}!"


user_name = Label(text="Your Name Will Appear Here!", font=("Arial", 18))
user_name.grid(column=1, row=1)

inputBar = Entry(width=25)
inputBar.bind("<Return>", button_clicked)
inputBar.insert(END, string="Enter Your Name Here!")
inputBar.grid(column=0, row=1, padx=(0, 20))


def spinbox_changed(event=None):
    spinbox_rating["text"] = f"Rate our Services! (Current Rating: {spinbox.get()})"


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_changed)
spinbox.grid(column=0, row=2, padx=(0, 10))

spinbox_rating = Label(text="Rate our Services!", font=("Arial", 18))
spinbox_rating.grid(column=1, row=2)

notifications = Label(text="You are not Subscribed to our Notifications.", font=("Arial", 18, "bold"))
notifications.grid(column=1, row=3)


def checked_button(event=None):
    if checked_state.get() == 1:
        notifications["text"] = "Thank you for Subscribing to our Notifications!"
    else:
        notifications["text"] = "You are not Subscribed to our Notifications."


checked_state = IntVar()
checkbutton = Checkbutton(text="Would you Like to Subscribe to Notifications?", variable=checked_state,
                          command=checked_button)
checkbutton.grid(column=0, row=3)

feedback = Label(text="You Have Chosen the Feedback Type: ", font=("Arial", 18, "bold"))
feedback.grid(column=1, row=4)


def listbox_used(event=None):
    selected_feedback = listbox.get(listbox.curselection())
    feedback["text"] = f"You Have Chosen the Feedback Type: {selected_feedback}"


listbox = Listbox(height=3)
feedback_type = ["Feedback", "Suggestions", "Complaints"]
for items in feedback_type:
    listbox.insert(feedback_type.index(items), items)

listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.grid(column=0, row=4, padx=(0, 10))


def submit():
    summary_label[
        "text"] = f"Name: {inputBar.get()}\nRating: {spinbox.get()}\nFeedback Type: {listbox.get(listbox.curselection())}\n" + \
                  ("Subscribed to Notifications" if checked_state.get() == 1 else "Not Subscribed to Notifications")


submit_button = Button(text="Submit", command=submit)
submit_button.grid(column=0, row=5, pady=(10, 0), columnspan=2)

summary_label = Label(text="", font=("Arial", 16), justify=LEFT)
summary_label.grid(column=0, row=6, columnspan=2, pady=(10, 0))

window.mainloop()