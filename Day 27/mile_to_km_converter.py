from tkinter import *

window = Tk()
window.minsize(500, 500)

def calculate():
    km_value.config(text= int(input.get()) * 1.609)


mile_label = Label(text=" Miles", font=("Arial", 15, "bold"))
mile_label.grid(column=2, row=0)

is_equal = Label(text="is equal to ", font=("Arial", 15, "bold"))
is_equal.grid(column=0, row=1)

km_label = Label(text=" KM", font=("Arial", 15, "bold"))
km_label.grid(column=2, row=1)

km_value = Label(text="0", font=("Arial", 15, "bold"))
km_value.grid(column=1, row=1)

button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

input = Entry()
input.grid(column=1, row=0)

window.mainloop()