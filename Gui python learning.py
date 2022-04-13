from tkinter import *

root = Tk()

# Creating a Label Widget
myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="My naame is jowny")
myLabel3 = Label(root, text="Hey Hi")
# Shoving it onto the screen
myLabel1.grid(row=1,column=3)
myLabel2.grid(row=3,column=4)
myLabel3.grid(row=4,column=5)

root.mainloop()  