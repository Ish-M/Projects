# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 18:00:24 2021

@author: Ishaan
"""
#importing
from tkinter import *
import math
import random
import time
from datetime import date
#Making and Formatting window name and color
root=Tk()
root.title("Calculator")
root.configure(bg='gray18')

#defining functions:
#Clear button    
def clear_memory():
    e.delete(0, END)
    
#Decimal button
def button_decimal():
    current=e.get()
    e.delete(0, END)
    e.insert(0, str(current)+str("."))
#Storing and Displaying numbers    
def button_add(number):
    current=e.get()
    e.delete(0, END)
    e.insert(0, str(current)+str(number))
#Storing the type of sign and deleting what is displayed     
def button_click_addition():
    first_number=e.get()
    global f_num 
    global sign
    sign="a"
    f_num= float(first_number)
    e.delete(0, END)        
def button_click_subtraction():
    first_number=e.get()
    global f_num 
    global sign
    sign="s"
    f_num= float(first_number)
    e.delete(0, END)    
def button_click_division():
    first_number=e.get()
    global f_num 
    global sign
    sign="d"
    f_num= float(first_number)
    e.delete(0, END)    
def button_click_multiply():
    first_number=e.get()
    global f_num 
    global sign
    sign="m"
    f_num= float(first_number)
    e.delete(0, END)    
#Doing the equation when Equal is pressed    
def button_equal():

        second_number=e.get()
        e.delete(0, END)
        if sign=="a":
            a=(float(f_num)+float(second_number))    
            e.insert(0, str(a))  
        elif sign=="s":
            a=(float(f_num)-float(second_number))    
            e.insert(0, str(a))
        elif sign=="m":
            a=(float(f_num)*float(second_number))    
            e.insert(0, str(a))    
        elif sign=="d":
                a=(float(f_num)/float(second_number))    
                e.insert(0, str(a))
#Square button function
def button_square():
    answer=(float(e.get())*float(e.get()))
    e.delete(0, END)
    e.insert(0, str(answer))             
#Squareroot function
def button_sqrt():
    answer=(math.sqrt(float(e.get())))    
    e.delete(0, END)
    str(answer)
    e.insert(0, answer)
#¯\_(ツ)_/¯
def button_fun():
    e.delete(0, END)
    randoma=random.randrange(3)
    if randoma==0:
       
        randomb=random.randrange(2)
        if randomb==1:
                e.insert (0, "Yoouuu Areee Havingggg Fuuuuun... did it work?")
        if randomb==0:
                e.insert(0, '3.14159265 Ha! You thought this was a pi button')
    elif randoma==2:
        today= str(date.today())
        dat=("Today is "+today+" Oh, i'm not a calendar")
        e.insert(0,dat )
    elif randoma==1:
        a=("😥")
        b=("🤣")
        c=("😎")
        d=("😜")
        ea=("🤢")
        f=(":-D")
        g=("¯\_(ツ)_/¯")
        h=("🍕")
        i=("(¬_¬ )")
        j=("🍟")
        k=("(￣┰￣*)")
        l=("🤑")
        m=("😷")
        n=("💀")
        o=("😃")
        p=("(x_x)")
        q=("<@_@>")
        r=("🤐")
        s=("🤯")
        t=("OwO")
        u=("UwU")
        u=("🎳")
        v=("🕶")
        w=(">:(")
        x=("\(OvO)/")
        y=("⏳")
        z=("🧨")
        for i in range (1):
                rand=random.randrange(26)
                if rand==(0):
                    e.insert(0,a)
                elif rand==(1):
                    e.insert(0,b)
                elif rand==(2):
                    e.insert(0,c)
                elif rand==(3):
                    e.insert(0,d)
                elif rand==(4):
                    e.insert(0,ea)
                elif rand==(5):
                    e.insert(0,f)
                elif rand==(6):
                    e.insert(0,g)
                elif rand==(7):
                    e.insert(0,h)
                elif rand==(8):
                    e.insert(0,i)
                elif rand==(9):
                    e.insert(0,j)
                elif rand==(10):
                    e.insert(0,k)
                elif rand==(11):
                    e.insert(0,l)
                elif rand==(12):
                    e.insert(0,m)
                elif rand==(13):
                    e.insert(0,n)
                elif rand==(14):
                    e.insert(0,z)
                elif rand==(15):
                    e.insert(0,o)
                elif rand==(16):
                    e.insert(0,p)
                elif rand==(17):
                    e.insert(0,q)
                elif rand==(18):
                    e.insert(0,r)
                elif rand==(19):
                    e.insert(0,s)
                elif rand==(20):
                    e.insert(0,t)
                elif rand==(21):
                    e.insert(0,u)
                elif rand==(22):
                    e.insert(0,v)
                elif rand== (23):
                    e.insert(0,w)
                elif rand==(24):
                    e.insert(0,x)
                elif rand==(25):    
                   e.insert(0,y)
   

    #creating buttons and display
e=Entry(root, width=40, borderwidth=5, bg='light sky blue',)
button_1= Button(root, text="1️", padx=32, pady=30, command=lambda: button_add(1), bg='gray28', fg='floral white')
button_2= Button(root, text="2", padx=40, pady=30, command=lambda:button_add(2), bg='gray28', fg='floral white')
button_3= Button(root, text="3", padx=40, pady=30, command=lambda:button_add(3), bg='gray28', fg='floral white')
button_4= Button(root, text="4", padx=40, pady=30, command=lambda:button_add(4), bg='gray28', fg='floral white')
button_5= Button(root, text="5", padx=40, pady=30, command=lambda:button_add(5), bg='gray28', fg='floral white')
button_6= Button(root, text="6", padx=40, pady=30, command=lambda:button_add(6), bg='gray28', fg='floral white')
button_7= Button(root, text="7", padx=40, pady=30, command=lambda:button_add(7), bg='gray28', fg='floral white')
button_8= Button(root, text="8", padx=40, pady=30, command=lambda:button_add(8), bg='gray28', fg='floral white')
button_9= Button(root, text="9", padx=40, pady=30, command=lambda:button_add(9), bg='gray28', fg='floral white')
button_0= Button(root, text="0", padx=40, pady=30, command=lambda:button_add(0), bg='gray28', fg='floral white')
button_addition=Button(root, text="➕", padx=35, pady=30, command=button_click_addition, bg='gray64')
button_subtraction=Button(root, text="➖", padx=35, pady=30, command=button_click_subtraction, bg='gray64')
button_division=Button(root, text="➗", padx=35, pady=30, command=button_click_division, bg='gray64')
button_multiply=Button(root, text="✖", padx=35, pady=30, command=button_click_multiply, bg='gray64')
button_equal=Button(root, text="=", padx=39, pady=30, command=button_equal, bg='orange')
button_clear=Button(root, text="CE", padx=36, pady=30, command=clear_memory, bg='orange')
decimal=Button(root, text="◾", padx=39, pady=30, command=button_decimal, bg='gray28', fg='floral white')
square=Button(root, text='square', padx=25, pady=30, command=button_square, bg="gray64")
cube=Button(root, text='¯\_(ツ)_/¯', padx=17, pady=30, command=button_fun, bg='gray64')
squareroot=Button(root, text='sqrt', padx=32, pady=30, command=button_sqrt, bg='gray64')


#Putting buttons and Display on GUI
e.grid(row=0, column=0, columnspan=4, padx=20, pady=15, ipady=10, ipadx=10) 
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=1)
button_addition.grid(row=5, column=3)
button_equal.grid(row=4, column=2)
button_clear.grid(row=1, column=3,)
button_subtraction.grid(row=2, column=3)
button_division.grid(row=3, column=3)
button_multiply.grid(row=4, column=3)
decimal.grid(row=4, column=0,)
square.grid(row=5, column=1)
cube.grid(row=5, column=0)
squareroot.grid(row=5, column=2)
#Looping to detect button presses
root.mainloop()