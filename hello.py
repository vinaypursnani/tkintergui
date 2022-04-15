root = Tk()

# creating a label widget
myLabel1 = Label(root, text='Hello World!').grid(row=0, column=0)
myLabel2 = Label(root, text='Hello Grid World!').grid(row=1, column=0)

# Putting label in grid
# myLabel1.grid(row=0, column=0)
# myLabel2.grid(row=1, column=0) # column value 5 will still have this in 2 because then nothing exists in column 1 2 3 

# putting widget on screen
# myLabel.pack()

root.mainloop()