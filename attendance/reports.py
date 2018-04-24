#import module from tkinter for UI
from tkinter import *

import os

#creating instance of TK
root=Tk()

root.configure(background="white")

#root.geometry("600x600")

def function1():
    
    os.system("synopsis.pdf")
    
def function2():
    
    os.system("report1.pdf")

def function3():

    os.system("report2.pdf")

def function4():

    root.destroy()
    os.system("py firstpage.py")

#stting title for the window
root.title("AUTOMATIC ATTENDANCE MANAGEMENT USING FACE RECOGNITION")

#creating a text label
Label(root, text="Project Reports",font=("times new roman",40),fg="white",bg="red",height=2).grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating a button
Button(root,text="Synopsis",font=("times new roman",30),bg="#3F51B5",fg='white',command=function1).grid(row=3,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)

#creating second button
Button(root,text="Report 1",font=("times new roman",30),bg="#3F51B5",fg='white',command=function2).grid(row=4,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating third button
Button(root,text="Report 2",font=('times new roman',30),bg="#3F51B5",fg="white",command=function3).grid(row=5,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating five button
Button(root,text="Back",font=('times new roman',40),bg="red",fg="white",command=function4).grid(row=8,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

root.mainloop()
