from tkinter import *
import math

root = Tk()
root.title("Orders And Bills")

Items = ("Pasta, Pizza, Brounie, Cake, Cupcake, Shake, Sandwich, Coffee, Tea, Fries ")

Pasta = 300
Pizza = 350
Brounie = 150
Cake = 700
Cupcake = 70
Shake = 150
Sandwich = 150
Coffee = 250
Tea = 100
Fries = 150

button_Pasta = Button(root, text = "Pasta", pady=15, bg = "black", fg = "white", font=(50))
button_Pizza = Button(root, text = "Pizza", pady=15, bg = "black", fg = "white", font=(50))
button_Brounie = Button(root, text = "Brounie", pady=15, bg = "black", fg = "white", font=(50))
button_Cake = Button(root, text = "Cake", pady=15, bg = "black", fg = "white", font=(50))
button_Cupcake = Button(root, text = "Cupcake", pady=15, bg = "black", fg = "white", font=(50))
button_Shake = Button(root, text = "Shake", pady=15, bg = "black", fg = "white", font=(50))
button_Sandwich = Button(root, text = "Sandwich", pady=15, bg = "black", fg = "white", font=(50))
button_Coffee = Button(root, text = "Coffee", pady=15, bg = "black", fg = "white", font=(50))
button_Tea = Button(root, text = "Tea", pady=15, bg = "black", fg = "white", font=(50))
button_Fries = Button(root, text = "Fries", pady=15, bg = "black", fg = "white", font=(50))

button_Pasta.grid(row = 1, column = 0)
button_Pizza.grid(row = 1, column = 1)
button_Brounie.grid(row = 1, column = 2)

button_Cake.grid(row = 2, column = 0)
button_Cupcake.grid(row = 2, column = 1)
button_Shake.grid(row = 2, column = 2)

button_Sandwich.grid(row = 3, column = 0)
button_Coffee.grid(row = 3, column = 1)
button_Tea.grid(row = 3, column = 2)

button_Fries.grid(row = 3, column = 1)

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

e.insert(0," The order ")

def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.grid(row=0,column=4)

myButton1 = Button(root, text ="Total Bill")
myButton1.grid(row=0,column=3)











#label = Label(root, text = "Total Bill", font=(60) )
#label.grid(row=0, column=0)##

#my_label = Label(root, text = , font=(60))
#my_label.grid(row=0, column=1)

root.mainloop() 