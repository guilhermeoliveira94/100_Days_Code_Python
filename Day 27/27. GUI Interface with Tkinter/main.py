from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Mile to Km Converter")
window.config(padx=70, pady=20)

#Labels
label_miles = Label(text="Miles")
label_miles.grid(column=3, row=0)

label_km = Label(text="Km")
label_km.grid(column=3, row=1)

label_is_equal_to = Label(text="is equal to")
label_is_equal_to.grid(column=0, row=1)

label_answer = Label(text="0")
label_answer.grid(column=1, row=1)

#Entries
entry = Entry(width=7)
entry.grid(column=1, row=0)

#Buttons
def action():
    miles_entry = float(entry.get())
    km_answer = miles_entry * 1.609
    label_answer.config(text=f"{km_answer}" )

#calls action() when pressed
button = Button(text="Calculate", command=action)
button.grid(column=1, row=2)

window.mainloop()
