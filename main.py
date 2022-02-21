from tkinter import *


def addingFunction():
    x = float(entry1.get())
    y = float(entry2.get())
    z = x + y
    label3.configure(text=str(z))


root = Tk()
root.geometry("200x100")
root.title("Add")

label1 = Label(root, text="First Number: ")
label1.grid(row=0, column=0)

entry1 = Entry(root, width=10)
entry1.grid(row=0, column=1)

label2 = Label(root, text="Second Number: ")
label2.grid(row=1, column=0)

entry2 = Entry(root, width=10)
entry2.grid(row=1, column=1)

btn1 = Button(root, text="Add!", command=addingFunction)
btn1.grid(row=2, column=0)

label3 = Label(root, text="")
label3.grid(row=2, column=1)

root.mainloop()

quit()