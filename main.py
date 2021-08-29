from tkinter import *
import math


root = Tk()
root.title("Calculator")
root.geometry("255x300")
root.resizable(height = False, width = False)

myentry = Entry(root, font = "calibri 17")
myentry.place(x = 0, y = 0, height = 45, width = 256)

def click(item):
	correct_arrenge = myentry.get()
	myentry.delete(0, END)
	myentry.insert(0, str(correct_arrenge) + str(item))

def clear():
	myentry.delete(0, END)

def add():
	first_num = myentry.get()
	global first_number
	global operator
	operator = "addition" 
	first_number = float(first_num)
	myentry.delete(0, END)

def sub():
	first_num = myentry.get()
	global first_number
	global operator
	operator = "subtraction" 
	first_number = float(first_num)
	myentry.delete(0, END)

def mult():
	first_num = myentry.get()
	global first_number
	global operator
	operator = "multiplication" 
	first_number = float(first_num)
	myentry.delete(0, END)

def div():
	first_num = myentry.get()
	global first_number
	global operator
	operator = "division" 
	first_number = float(first_num)
	myentry.delete(0, END)

def fact():
	first_num = myentry.get()
	first_number = float(first_num)
	myentry.delete(0, END)
	if first_number == 0:
		myentry.insert(0, 1)
	if first_number == 1 :
		myentry.insert(0, 1)
	else:
		myentry.insert(0, math.factorial(first_number))

def sqrt():
	first_num = myentry.get()
	first_number = float(first_num)
	myentry.delete(0, END)
	myentry.insert(0, math.sqrt(first_number))

def equal():
	second_number = myentry.get()
	myentry.delete(0, END)

	if operator == "addition" :
		myentry.insert(0, first_number + float(second_number))
	
	if operator == "subtraction" :
		myentry.insert(0, first_number - float(second_number))

	if operator == "multiplication" :
		myentry.insert(0, first_number * float(second_number))

	if operator == "division" :
		myentry.insert(0, first_number / float(second_number))

mybutton1 = Button(root, text = "1", bg = "#Bab2b1", height = 3, width = 6, command = lambda: click(1))
mybutton1.place(x = 0, y = 45)
mybutton2 = Button(root, text = "2", bg = "#Bab2b1", height = 3, width = 6, command = lambda: click(2))
mybutton2.place(x = 51, y = 45)
mybutton3 = Button(root, text = "3", bg = "#Bab2b1", height = 3, width = 6, command = lambda: click(3))
mybutton3.place(x = 102, y = 45)
mybutton4 = Button(root, text = "4", bg = "#Bab2b1", height = 3, width = 6, command = lambda: click(4))
mybutton4.place(x = 0, y = 100)
mybutton5 = Button(root, text = "5", bg = "#Bab2b1", height = 3, width = 6, command = lambda: click(5))
mybutton5.place(x = 51, y = 100)
mybutton6 = Button(root, text = "6", bg = "#Bab2b1", height = 3, width = 6, command = lambda: click(6))
mybutton6.place(x = 102, y = 100)
mybutton7 = Button(root, text = "7", bg = "#Bab2b1", height = 3, width = 6, command = lambda: click(7))
mybutton7.place(x = 0, y = 155)
mybutton8 = Button(root, text = "8", bg = "#Bab2b1", height = 3, width = 6, command = lambda: click(8))
mybutton8.place(x = 51, y = 155)
mybutton9 = Button(root, text = "9", bg = "#Bab2b1", height = 3, width = 6, command = lambda: click(9))
mybutton9.place(x = 102, y = 155)
mybutton00 = Button(root, text = "Clear", bg = "#Bab2b1", height = 3, width = 6, command = clear)
mybutton00.place(x = 0, y = 210)
mybutton0 = Button(root, text = "0", bg = "#Bab2b1", height = 3, width = 6, command = lambda: click(0))
mybutton0.place(x = 51, y = 210)
mybutton11 = Button(root, text = ".", bg = "#Bab2b1", height = 3, width = 6, command = lambda: click("."))
mybutton11.place(x = 102, y = 210)
mybuttonoper1 = Button(root, text = "DIV", height = 3, width = 6, command = div)    
mybuttonoper1.place(x = 153, y = 45)
mybuttonoper2 = Button(root, text = "SUB", height = 3, width = 6, command = sub)
mybuttonoper2.place(x = 153, y = 100)
mybuttonoper3 = Button(root, text = "MULT", height = 3, width = 6, command = mult)
mybuttonoper3.place(x = 153, y = 155)
mybuttonoper4 = Button(root, text = "ADD", height = 3, width = 6, command = add)
mybuttonoper4.place(x = 153, y = 210)
mybuttonoper5 = Button(root, text = "SQRT", height = 3, width = 6, command = sqrt)
mybuttonoper5.place(x = 204, y = 45)
mybuttonoper6 = Button(root, text = "=", bg = "#551109", height = 7, width = 6, command = equal)
mybuttonoper6.place(x = 204, y = 150)
mybuttonoper7 = Button(root, text = "FACT", height = 3, width = 6, command = fact)
mybuttonoper7.place(x = 204, y = 100)
mylabel = Label(root, text = "***made by Amin Nazari***")
mylabel.place(x = 51, y = 275)



root.mainloop()











 