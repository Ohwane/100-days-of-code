from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(500, 500)
window.config(padx=50, pady=200)

# label

my_label = Label(text="I am a label", font=("Arial", 30, "italic"))
my_label.grid(column=0, row= 0)
my_label.config(padx=100, pady=100)

my_label["text"] = "this is a new text"

# Button

def button_clicked():
    print("I got clicked")
    my_label.config(text=f"{input.get()}")


button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row= 1)

second_button = Button(text="Second Button")
second_button.grid(column=2, row= 0)
# Entry

input = Entry()
input.grid(column=3, row= 2)
window.mainloop()

