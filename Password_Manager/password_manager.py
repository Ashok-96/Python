from tkinter import *
from tkinter import messagebox
import random



DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']
UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']

def genpass():
    COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS
    temp_password=''
    for i in range(13):
        temp_password+=random.choice(COMBINED_LIST)
    messagebox.showinfo("",'Password generated successfully!')
    password.configure(text=f' hi {txtName.get()}, the password is {temp_password}')
    
root=Tk()
formFrame=Frame(root, border='3')
lblNme=Label(formFrame,text='Name :')
txtName=Entry(formFrame)
txtName.grid(row=0,column=1)
lblNme.grid(row=0,column=0)
formFrame.grid(row=0, column=0)
gbutton=Button(formFrame, text="Generate",command=genpass)
gbutton.grid(row=1, column=0)
password=Label(formFrame)
password.grid(row=4,column=1)
root.title("Password Generator")

root.geometry('400x300')
root.mainloop()






