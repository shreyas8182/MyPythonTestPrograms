from tkinter import *
from PIL import ImageTk,Image


root = Tk()
root.title("Calculator")
root.iconbitmap("C:/Users/Shreyas/Documents/python/Martz90-Circle-Calculator.ico")
my_img = ImageTk.PhotoImage(Image.open("C:/Users/Shreyas/Documents/python/calculator image.png"))
my_label = Label(image=my_img)
my_label.pack()
















button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()






root.mainloop()