
from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Icons, Images and Exit Buttons")
root.iconbitmap('Logo.ico')
root.resizable(width=False, height=False)

# my_img = ImageTk.PhotoImage(Image.open('the_batman_logo.jpg'))
# my_label = Label(image=my_img)
# my_label.pack()

button_quit = Button(root, text='Exit', command=root.quit)
button_quit.pack()

root.mainloop()