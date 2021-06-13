from tkinter import *

window = Tk()
window.title("My first GUI Program")
window.wm_minsize(width=500, height=300)
window.config(padx=20, pady=20)


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

#Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

#Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=0, row=1)

#Entry
input = Entry(width=10)
input.grid(column=0, row=2)

#NewButton
new_button = Button(text="New")
new_button.grid(row=0, column=2)











window.mainloop()
