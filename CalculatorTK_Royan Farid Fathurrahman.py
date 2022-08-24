from __future__ import division
from tkinter import *
import tkinter.font as font
import math
# import locale
# from tkinter.ttk import Style
# from unittest import result

# general
root = Tk()
# locale.setlocale(locale.LC_ALL, '')
root.title("Calculator")
root.geometry("320x420")
root["bg"] = "black"
# root.config(cursor="shuttle")

# entry number
entryfont = font.Font(size = 15)

e = Entry(root, width=25, borderwidth=0,)
e["font"] = entryfont
e["bg"] = "black"
e["fg"] = "orange"
e.grid(row=0, column=0, columnspan=4, padx=20, pady=20)
# disable keyboard input in entry number
e.bind("<Key>", lambda e: "break")


def angka(nilai):
    before = e.get()
    e.delete(0,END)
    e.insert(0,str(before)+str(nilai))
    
def tambah():
    first_num = e.get()
    # first_num = float(first_num)
    global f_num
    global calc
    calc = "addition"
    f_num = int(first_num)
    # if first_num == float:
    #     f_num = float(first_num)
    # else:    
    #     f_num = int(first_num)
    e.delete(0,END)

def kurang():
    first_num = e.get()
    global f_num
    global calc
    calc = "subtraction"
    f_num = int(first_num)
    e.delete(0,END)

def kali():
    first_num = e.get()
    global f_num
    global calc
    calc = "multiplication"
    f_num = int(first_num)
    e.delete(0,END)

def bagi():
    first_num = e.get()
    global f_num
    global calc
    calc = "division"
    f_num = int(first_num)
    e.delete(0,END)
    
def pangkat():
    first_num = e.get()
    global f_num
    global calc
    calc = "exponential"
    f_num = int(first_num)
    e.delete(0,END)
    
def akar():
    first_num = e.get()
    global f_num
    f_num = int(first_num)
    e.delete(0,END)
    e.insert(0,math.sqrt(f_num))
    
def sisabagi():
    first_num = e.get()
    global f_num
    global calc
    calc = "modulo"
    f_num = int(first_num)
    e.delete(0,END)
    
# def persen():
#     first_num = e.get()
#     global f_num
#     f_num = float(first_num)
#     e.delete(0,END)
#     e.insert(0,f_num/100)
    
def faktorial():
    first_num = e.get()
    global f_num
    f_num = int(first_num)
    e.delete(0,END)
    e.insert(0,math.factorial(f_num))

def hapussemua():
    e.delete(0,END)

def samadengan():
    second_num = e.get()
    # second_num = int(second_num)
    e.delete(0,END)
    if calc == "addition":
        e.insert(0,f_num + int(second_num))
        # if f_num == float:
        #     e.insert(0,float(f_num) + float(second_num))
        # else:
        #     e.insert(0,f_num + int(second_num))
    elif calc == "subtraction":
        e.insert(0,f_num - int(second_num))
    elif calc == "multiplication":
        e.insert(0,f_num * int(second_num))
    elif calc == "division":
        try:
            divide = f_num / int(second_num)
            e.insert(0,divide)
        except ZeroDivisionError:
            e.insert(0, "Can't divide by zero!")
    elif calc == "exponential":
        e.insert(0,f_num ** int(second_num))
    elif calc == "modulo":
        e.insert(0,f_num % int(second_num))

# number button
btn1 = Button(root, text="1", padx=30, pady=20, command=lambda:angka(1), cursor="hand2").grid(row=4, column=0, pady=2)
btn2 = Button(root, text="2", padx=30, pady=20, command=lambda:angka(2), cursor="hand2").grid(row=4, column=1, pady=2)
btn3 = Button(root, text="3", padx=30, pady=20, command=lambda:angka(3), cursor="hand2").grid(row=4, column=2, pady=2)
btn4 = Button(root, text="4", padx=30, pady=20, command=lambda:angka(4), cursor="hand2").grid(row=3, column=0, pady=2)
btn5 = Button(root, text="5", padx=30, pady=20, command=lambda:angka(5), cursor="hand2").grid(row=3, column=1, pady=2)
btn6 = Button(root, text="6", padx=30, pady=20, command=lambda:angka(6), cursor="hand2").grid(row=3, column=2, pady=2)
btn7 = Button(root, text="7", padx=30, pady=20, command=lambda:angka(7), cursor="hand2").grid(row=2, column=0, pady=2)
btn8 = Button(root, text="8", padx=30, pady=20, command=lambda:angka(8), cursor="hand2").grid(row=2, column=1, pady=2)
btn9 = Button(root, text="9", padx=30, pady=20, command=lambda:angka(9), cursor="hand2").grid(row=2, column=2, pady=2)
btn0 = Button(root, text="0", padx=30, pady=20, command=lambda:angka(0), cursor="hand2").grid(row=5, column=0, pady=2)

# command button
# boldFont = font.Font(weight="bold")
add = Button(root, text="+", bg="orange", fg="white", padx=30, pady=20, command=tambah, cursor="hand2").grid(row=4, column=3, pady=2)
sub = Button(root, text="-", bg="orange", fg="white", padx=31, pady=20, command=kurang, cursor="hand2").grid(row=3, column=3, pady=2)
mul = Button(root, text="x", bg="orange", fg="white", padx=30, pady=20, command=kali, cursor="hand2").grid(row=2, column=3, pady=2)
div = Button(root, text="/", bg="orange", fg="white", padx=30, pady=20, command=bagi, cursor="hand2").grid(row=1, column=3, pady=2)
exp = Button(root, text="^", bg="orange", fg="white", padx=30, pady=20, command=pangkat, cursor="hand2").grid(row=1, column=1, pady=2)
sqt = Button(root, text="√", bg="orange", fg="white", padx=30, pady=20, command=akar, cursor="hand2").grid(row=5, column=1, pady=2)
mod = Button(root, text="mod", bg="orange", fg="white", padx=20, pady=20, command=sisabagi, cursor="hand2").grid(row=1, column=2, pady=2)
# perc = Button(root, text="%", bg="orange", fg="white", padx=28, pady=20, command=persen).grid(row=5, column=1, pady=2)
fact = Button(root, text="!", bg="orange",fg="white", padx=30, pady=20, command=faktorial, cursor="hand2").grid(row=5, column=2, pady=2)
c = Button(root, text="C", bg="red", fg="white", padx=30, pady=20, command=hapussemua, cursor="hand2").grid(row=1, column=0, pady=2)
eq = Button(root, text="=", bg="blue", fg="white", padx=30, pady=20, command=samadengan, cursor="hand2").grid(row=5, column=3, pady=2)


root.mainloop()