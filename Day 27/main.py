from tkinter import *

window = Tk()
window.title("My First(not really) Gui program")
window.minsize(width=500, height=300)

#label

my_label = Label(text="I am a label", font=("Bauhaus 93", 24, "bold"))
my_label.pack()

my_label["text"] = "This is a new text"


def button_clicked():
    my_label.config(text=f"{input.get()}")
    print("i got clicked")


button = Button(text="CLick Me", command=button_clicked)

button.pack()

input = Entry(width=50)
input.pack()

window.mainloop()