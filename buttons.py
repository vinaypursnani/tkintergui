from tkinter import *

from numpy import pad

root = Tk()

def myClick():
    myLabel = Label(root, text = 'Button Clicked')
    myLabel.pack()


mybutton = Button(root, text='Submit', padx = 100, pady=100, command=myClick, fg='teal', bg='black') # if command is assigned with function paranthesis it automatically calls the function not on click.
# mybutton = Button(root, text='Submit Disabled', state=DISABLED).grid(row=2, column=1)
mybutton.pack()

root.mainloop()