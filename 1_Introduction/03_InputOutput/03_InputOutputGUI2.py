from tkinter import *

window = Tk()

window.title("Hello GUI World!")
window.geometry("300x80")

nameLabel = Label(window, text="Name")
nameEntry = Entry(window)
ageLabel = Label(window, text="Age")
ageEntry = Entry(window)
paymentLabel = Label(window, text="Payment")
paymentEntry = Entry(window)

nameLabel.grid(row=0, column=0)
nameEntry.grid(row=0, column=1)
ageLabel.grid(row=1, column=0)
ageEntry.grid(row=1, column=1)
paymentLabel.grid(row=2, column=0)
paymentEntry.grid(row=2, column=1)

window.mainloop()  # keep the application running

