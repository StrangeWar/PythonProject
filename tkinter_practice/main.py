from tkinter import *

window = Tk()
window.minsize(500, 300)
window.title('tkinter practice')

# label
label = Label(text="this is a label", font=('Arial', 24))
label.grid(column=0, row=0)


def button_clicked():
    new_text = input.get()
    label.config(text= new_text)


# button
button_1 = Button(text='click me', command=button_clicked)
button_1.grid(column=1, row=1)

button_2 = Button(text='press me')
button_2.grid(column=2, row=0)

# entry
input = Entry(width=20)
input.grid(column=3, row=3)
text = input.get()



window.mainloop()