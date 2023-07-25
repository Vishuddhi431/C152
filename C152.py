#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 07:41:32 2023

@author: vishuddhimakeshwaran
"""

from tkinter import *
root = Tk()
root.geometry("500x600")
root.title("Report Card")

labelAns1 = Label(root)
labelAns2 = Label(root)
labelAns3 = Label(root)

array1 = ["Sophie", "Jess", "Diya"]
array2 = [["Sophie", "A+"], ["Jess", "C-"], ["Diya", "B-"]]
array3 = [[["Sophie", "A+", "Excellent!"], ["Jess", "C-", "Needs Work"], ["Diya", "B-", "Approaching Standards"]]]

print(array1)
print(array2)
print(array3)

def report1(): 
    labelAns1["text"] = (str(array3[0][0][0]) + " got an " + str(array3[0][0][1]) + ". " + str(array3[0][0][2]))
    print(str(array3[0][0][0]) + " got an " + str(array3[0][0][1]) + ". " + str(array3[0][0][2]))
    
def report2(): 
    labelAns2["text"] = (str(array3[0][1][0]) + " got a " + str(array3[0][1][1]) + ". " + str(array3[0][1][2]))
    print(str(array3[0][1][0]) + " got a " + str(array3[0][1][1]) + ". " + str(array3[0][1][2]))
    
def report3(): 
    labelAns3["text"] = (str(array3[0][2][0]) + " got a " + str(array3[0][2][1]) + ". " + str(array3[0][2][2]))
    print(str(array3[0][2][0]) + " got a " + str(array3[0][2][1]) + ". " + str(array3[0][2][2]))
    
button1 = Button(root, text = "View Sophie's Report Card", command = report1)
button1.place(relx = 0.3, rely = 0.3, anchor = CENTER)
labelAns1.place(relx = 0.3, rely = 0.4, anchor = CENTER)

button2 = Button(root, text = "View Jess' Report Card", command = report2)
button2.place(relx = 0.7, rely = 0.3, anchor = CENTER)
labelAns2.place(relx = 0.7, rely = 0.4, anchor = CENTER)

button3 = Button(root, text = "View Diya's Report Card", command = report3)
button3.place(relx = 0.5, rely = 0.6, anchor = CENTER)
labelAns3.place(relx = 0.5, rely = 0.7, anchor = CENTER)

labelAns4 = Label(root)

def reportRandom(): 
    labelAns4["text"] = str(array3[0][0][0] + "got a " + array3[0][2][1] + ". She " + array3[0][1][2])
    print(str(array3[0][0][0] + " got a " + array3[0][2][1] + ". She " + array3[0][1][2]))
    
button4 = Button(root, text = "Random Report", command = reportRandom)
button4.place(relx = 0.5, rely = 0.8, anchor = CENTER)
labelAns4.place(relx = 0.5, rely = 0.9, anchor = CENTER)

root.mainloop()
