from tkinter import *


def convert():
    mile = float(mile_entered.get())
    km = mile * 1.609
    mile_to_km_label.config(text=f"{round(km, 3)}")


window = Tk()
window.config(padx=20, pady=20)
window.title("Mile to Km convertor")

equal_to_label = Label(text='is equal to ')
equal_to_label.grid(column=1, row=2)

miles_label = Label(text='Miles')
miles_label.grid(column=3, row=1)

km_label = Label(text='Km')
km_label.grid(column=3, row=2)

mile_to_km_label = Label(text="0")
mile_to_km_label.grid(column=2, row=2)

mile_entered = Entry(width=10)
mile_entered.grid(column=2, row=1)

button = Button(text="calculate", command=convert)
button.grid(column=2, row=3)


window.mainloop()
