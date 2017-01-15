from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog

window = Tk()

window.title("Hello GUI world!")
window.geometry("600x300")

messagebox.showinfo("Message Box", "Hello GUI world")

name = simpledialog.askstring("Name", "What is your name?")
age = simpledialog.askinteger("Age", "How old are you?")
payment = simpledialog.askfloat("Payment", "What is the payment value?")

data = "Name = {0}\nAge = {1}\nPayment = {2}".format(name, age, payment)
messagebox.showinfo("Data", data)

window.mainloop()  # keep the application running






