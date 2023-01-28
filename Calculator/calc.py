#Simple Calculator using python
from tkinter import *
import tkinter.ttk as ttk
root = Tk()
class Window:
    def __init__(self, master):
        style=ttk.Style()
        style.theme_use('winnative')
root.title("Calculator")
#('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')
root.geometry("400x400")
inputframe=Frame(root)
inp=Entry(inputframe)
i=1
j=1
def equals():
    expression=inp.get()
    inp.delete(0,END)
    try:
        result=eval(expression)
    except Exception as e:
        inp.insert(END,e)
    inp.insert(END, result)

def fun(x):
    inp.insert(END,x)

def clear():
    inp.delete(0,END)
while i<=3:
    keypad_i=Frame(root,padx=20)
    keypad_i.grid(row=i )
    while j<=(i*3):
        button_j=Button(keypad_i, text=j,padx=13, pady=7, command=lambda num=j:fun(num))
        j+=1
        button_j.pack(side=LEFT)
    i+=1
keypad_0=Frame(root)
button_0=Button(keypad_0, text=0,padx=34, pady=7,command= lambda num=0:fun(num))
Equals=Button(keypad_0, text='=',padx=11, pady=7, command=equals)
button_0.pack(side=LEFT)
Equals.pack(side=RIGHT)

keypad_0.grid(row=4,column=0 )
plus=Button(root, text='+',command=lambda num='+':fun(num), padx=7,pady=6)
minus=Button(root, text='-',command=lambda num='-':fun(num),  padx=8, pady=6)
multiply=Button(root, text='*',command=lambda num='*':fun(num),  padx=8, pady=6)
divide=Button(root, text='/',command=lambda num='/':fun(num),  padx=8, pady=6)
clear=Button(text='clear', padx=45, command=clear)
clear.grid(row=5,column=0)
plus.grid(row=1,column=5)
minus.grid(row=2,column=5)
multiply.grid(row=3,column=5)
divide.grid(row=4, column=5)

inp.pack(side=TOP)   
inputframe.grid(row=0,column=0)
window=Window(root)
root.mainloop()
