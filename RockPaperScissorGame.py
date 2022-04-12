import random
import tkinter as tk
from PIL import ImageTk,Image
window = tk.Tk()
window.geometry("300x300")
window.title("Rock Paper Scissors")

USER_SCORE = 0
COMP_SCORE = 0
USER_CHOICE = ""
COMP_CHOICE = "" 

def choice_to_number(choice):
    rps = {'rock':0,'paper':1,'scissor':2}
    return rps[choice]

def number_to_choice(number):
    rps={0:'rock',1:'paper',2:'scissor'}
    return rps[number]

def random_computer_choice():
    return random.choice(['rock','paper','scissor']) 

def result(human_choice,comp_choice):
    global USER_SCORE
    global COMP_SCORE
    user=choice_to_number(human_choice)
    comp=choice_to_number(comp_choice)
    if(user==comp):
        print("Tie")
    elif((user-comp)%3==1):
        print("You win")
        USER_SCORE+=1
    else:
        print("Computer wins")
        COMP_SCORE+=1
    text_area = tk.Text(master=window,height=30,width=30,bg="red")
    text_area.grid(column=0,row=4)
    answer = "Your Choice: {uc} \nComputer's Choice : {cc} \n Your Score : {u} \n Computer Score : {c} ".format(uc=USER_CHOICE,cc=COMP_CHOICE,u=USER_SCORE,c=COMP_SCORE)    
    text_area.insert(tk.END,answer)

def rock():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE='rock'
    COMP_CHOICE=random_computer_choice()
    result(USER_CHOICE,COMP_CHOICE)

def paper():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE='paper'
    COMP_CHOICE=random_computer_choice()
    result(USER_CHOICE,COMP_CHOICE)

def scissor():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE='scissor'
    COMP_CHOICE=random_computer_choice() 
    result(USER_CHOICE,COMP_CHOICE)

#rock_btn = tk.PhotoImage(file="C:/Users/Shreyas/Documents/youtube/python/Stone.png")
#paper_btn = tk.PhotoImage(file="C:/Users/Shreyas/Documents/youtube/python/Paper.png")
#scissor_btn = tk.PhotoImage(file="C:/Users/Shreyas/Documents/youtube/python/Scissors.png")

#button1 = tk.Button(image = rock_btn, bg="darkblue", padx=10, pady=10, command=rock)
#button3 = tk.Button(image = scissor_btn, bg="red", padx=10, pady=10, command=scissor)
#button2 = tk.Button(image = paper_btn, bg="green", padx=10, pady=10, command=paper)


#button1.grid(column=0,row=1)
#button3.grid(column=2,row=1)
#button2.grid(column=1,row=1)


button1 = tk.Button(text="      Rock        ",bg="darkblue", padx=32, pady=10, command=rock)
button2 = tk.Button(text="       paper      ",bg="red", padx=32, pady=10, command=paper)   
button3 = tk.Button(text="      Scissor       ",bg="green", padx=30, pady=10, command=scissor)

button1.grid(column=0,row=1)
button2.grid(column=0,row=2)
button3.grid(column=0,row=3)


window.mainloop()
