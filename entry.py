from tkinter import *

# lst = []
root = Tk()

e = Entry(root, width=50, bg='blue', fg='white', borderwidth=5)
e.pack()
e.insert(0, 'Employee Name')

def myClick():
    hello = 'Hello ' + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()
    # lst.append(hello)
    # print(lst)

myButton = Button(root, text='Enter Your Name', command=myClick)
myButton.pack()

root.mainloop()