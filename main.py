from tkinter import *

result = 0
n1 = 0
n2 = 0
current_op = " "


# Defines functions

# Function for displaying numbers on the entry field
def put_number_on_screen(num):
    number = str(num)
    x = number_entry.get()
    number_entry.insert(len(x), number)


# Function for clearing the screen
def clear():
    number_entry.delete(0, 'end')


# Function for adding
def plus():
    global current_op
    global n1
    current_op = "+"
    n1 = float(number_entry.get())
    clear()


# Function for subtracting
def minus():
    global current_op
    global n1
    current_op = "-"
    n1 = float(number_entry.get())
    clear()


# Function for division
def div():
    global current_op
    global n1
    current_op = "/"
    n1 = float(number_entry.get())
    clear()


# Function for multiplication
def mult():
    global current_op
    global n1
    current_op = "*"
    n1 = float(number_entry.get())
    clear()


# Function for doing the math
def do_math():
    global result
    global current_op
    if current_op == "+":
        result = n1 + n2
    elif current_op == "*":
        result = n1 * n2
    elif current_op == "-":
        result = n1 - n2
    elif current_op == "/":
        result = n1 / n2
    return result


# Function for equal button
def equal():
    global n2
    global current_op
    global result
    n2 = float(number_entry.get())
    do_math()
    clear()
    number_entry.insert(0, str(result))
    current_op = "none"


# Makes widgets

# Makes window
window = Tk()
window.title("Calculator")
window.geometry("277x400")

# Creating the widgets

# Variables for Width, Height, Padding x, Padding Y, and Active Background for buttons
w = 7
h = 5
px = 3
py = 5
ab = "grey"

# Makes entry window
number_entry = Entry(window)

# Makes buttons 0 - 9
button0 = Button(window, text="0", activebackground=ab, command=lambda: put_number_on_screen(0))
button1 = Button(window, text="1", activebackground=ab, command=lambda: put_number_on_screen(1))
button2 = Button(window, text="2", activebackground=ab, command=lambda: put_number_on_screen(2))
button3 = Button(window, text="3", activebackground=ab, command=lambda: put_number_on_screen(3))
button4 = Button(window, text="4", activebackground=ab, command=lambda: put_number_on_screen(4))
button5 = Button(window, text="5", activebackground=ab, command=lambda: put_number_on_screen(5))
button6 = Button(window, text="6", activebackground=ab, command=lambda: put_number_on_screen(6))
button7 = Button(window, text="7", activebackground=ab, command=lambda: put_number_on_screen(7))
button8 = Button(window, text="8", activebackground=ab, command=lambda: put_number_on_screen(8))
button9 = Button(window, text="9", activebackground=ab, command=lambda: put_number_on_screen(9))

# Makes function buttons
button_multiplication = Button(window, text="*", activebackground=ab, command=mult)
button_division = Button(window, text="/", activebackground=ab, command=div)
button_plus = Button(window, text="+", activebackground=ab, command=plus)
button_minus = Button(window, text="-", activebackground=ab, command=minus)
button_clear = Button(window, text="clear", activebackground=ab, command=clear)
button_equal = Button(window, text="=", activebackground=ab, command=equal)

# Sets width and height of the buttons entry field and function buttons
number_entry.config(width=45)

button1.config(height=h, width=w)
button2.config(height=h, width=w)
button3.config(height=h, width=w)
button4.config(height=h, width=w)
button5.config(height=h, width=w)
button6.config(height=h, width=w)
button7.config(height=h, width=w)
button8.config(height=h, width=w)
button9.config(height=h, width=w)
button0.config(height=h, width=w)

button_multiplication.config(height=h, width=w)
button_division.config(height=h, width=w)
button_plus.config(height=h, width=w)
button_minus.config(height=h, width=w)
button_clear.config(height=h, width=w)
button_equal.config(height=h, width=w)

# Placing the widgets in grid pattern

number_entry.grid(column=0, row=0, columnspan=4)

button7.grid(row=2, column=0, pady=py, padx=px)
button8.grid(row=2, column=1, pady=py, padx=px)
button9.grid(row=2, column=2, pady=py, padx=px)
button4.grid(row=3, column=0, pady=py, padx=px)
button5.grid(row=3, column=1, pady=py, padx=px)
button6.grid(row=3, column=2, pady=py, padx=px)
button1.grid(row=4, column=0, pady=py, padx=px)
button2.grid(row=4, column=1, pady=py, padx=px)
button3.grid(row=4, column=2, pady=py, padx=px)
button0.grid(row=5, column=0)

button_division.grid(row=2, column=3)
button_multiplication.grid(row=3, column=3)
button_minus.grid(row=4, column=3)
button_plus.grid(row=5, column=3)
button_clear.grid(row=5, column=1)
button_equal.grid(row=5, column=2)

# Keeps program running until window is closed
window.mainloop()
