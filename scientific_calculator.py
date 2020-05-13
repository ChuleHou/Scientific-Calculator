#CS4085 Final Project
#Scientific Calculator
#Chule Hou
from tkinter import*
import math
import numpy as np

# Function to add in the entry of text display
def button_click(char):
    global calc_operator
    calc_operator += str(char)
    text_input.set(calc_operator)

# Function to clear the whole entry of text display
def button_clear_all():
    global calc_operator
    calc_operator = ""
    text_input.set("")

# Function to delete one by one from the last in the entry of text display
def button_delete():
    global calc_operator
    text = calc_operator[:-1]
    calc_operator = text
    text_input.set(text)

# Function to calculate the factorial of a number
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

def fact_func():
    global calc_operator
    result = str(factorial(int(calc_operator)))
    calc_operator = result
    text_input.set(result)

# Function to calculate trigonometric numbers of an angle
def trig_sin():
    global calc_operator
    result = str(math.sin(math.radians(int(calc_operator))))
    calc_operator = result
    text_input.set(result)

def trig_cos():
    global calc_operator
    result = str(math.cos(math.radians(int(calc_operator))))
    calc_operator = result
    text_input.set(result)

def trig_tan():
    global calc_operator
    result = str(math.tan(math.radians(int(calc_operator))))
    calc_operator = result
    text_input.set(result)

def trig_cot():
    global calc_operator
    result = str(1/math.tan(math.radians(int(calc_operator))))
    calc_operator = result
    text_input.set(result)

# Function to find the square root of a number
def square_root():
    global calc_operator
    temp = str(eval(calc_operator+'**(1/2)'))
    calc_operator = temp
    text_input.set(temp)

# Function to find the third root of a number
def third_root():
    global calc_operator
    temp = str(eval(calc_operator+'**(1/3)'))
    calc_operator = temp
    text_input.set(temp)

# Function to change the sign of number
def sign_change():
    global calc_operator
    if calc_operator[0]=='-':
        temp = calc_operator[1:]
    else:
        temp = '-'+calc_operator
    calc_operator = temp
    text_input.set(temp)    

# Function to calculate the percentage of a number
def percent():
    global calc_operator
    temp = str(eval(calc_operator+'/100'))
    calc_operator = temp
    text_input.set(temp)

# Funtion to find the result of an operation
def button_equal():
    global calc_operator
    temp_op = str(eval(calc_operator))
    text_input.set(temp_op)
    calc_operator = temp_op


sin = math.sin
cos = math.cos
tan = math.tan
log = math.log10
ln = math.log
e = math.exp
p = math.pi
E = '*10**'

calculator = Tk()
calculator.configure(bg="#A0522D", bd=10)
calculator.title("Scientific Calculator")

calc_operator = ""
text_input    = StringVar()

text_display  = Entry(calculator, font=('sans-serif', 20, 'bold'), textvariable=text_input, bd=5, insertwidth = 5, bg='#BBB', justify='right').grid(columnspan=5, padx = 10, pady = 15)
button_style  = {'bd':5, 'fg':'#000', 'bg':'#BBB', 'font':('sans-serif', 20, 'bold')}

# Absolute value of a number
abs_value        = Button(calculator, button_style, text='abs', command=lambda:button_click('abs(')).grid(row=1, column=0, sticky="nsew")
# Remainder of a division
modulo           = Button(calculator, button_style, text='mod', command=lambda:button_click('%')).grid(row=1, column=1, sticky="nsew")
# Integer division quotient
int_div          = Button(calculator, button_style, text='div', command=lambda:button_click('//')).grid(row=1, column=2, sticky="nsew")
# Factorial of a number
factorial_button = Button(calculator, button_style, text='x!',  command=fact_func).grid(row=1, column=3, sticky="nsew")
# Euler's number e
eulers_num       = Button(calculator, button_style, text='e',   command=lambda:button_click(str(math.exp(1)))).grid(row=1, column=4, sticky="nsew")


# Sine of an angle in degreese
sine         = Button(calculator, button_style, text='sin', command=trig_sin).grid(row=2, column=0, sticky="nsew")
# Cosine of an angle in degreese 
cosine       = Button(calculator, button_style, text='cos', command=trig_cos).grid(row=2, column=1, sticky="nsew")
# Tangent of an angle in degreese
tangent      = Button(calculator, button_style, text='tan', command=trig_tan).grid(row=2, column=2, sticky="nsew")
# Cotangent of an angle in degreese
cotangent    = Button(calculator, button_style, text='cot', command=trig_cot).grid(row=2, column=3, sticky="nsew")
# Pi(3.14...)
pi_num       = Button(calculator, button_style, text='π',   command=lambda:button_click(str(math.pi))).grid(row=2, column=4, sticky="nsew")


# Power of 2
second_power = Button(calculator, button_style, text='x\u00B2', command=lambda:button_click('**2')).grid(row=3, column=0, sticky="nsew")
# Power of 3
third_power  = Button(calculator, button_style, text='x\u00B3', command=lambda:button_click('**3')).grid(row=3, column=1, sticky="nsew")
# Power of n
nth_power    = Button(calculator, button_style, text='x^n',     command=lambda:button_click('**')).grid(row=3, column=2, sticky="nsew")
# Inverse number
inv_power    = Button(calculator, button_style, text='x\u207b\xb9', command=lambda:button_click('**(-1)')).grid(row=3, column=3, sticky="nsew")
# Powers of 10
tens_powers  = Button(calculator, button_style, text='10^x', font=('sans-serif', 15, 'bold'), command=lambda:button_click('10**')).grid(row=3, column=4, sticky="nsew")

# Square root of a number
square_root  = Button(calculator, button_style, text='\u00B2\u221A', command=square_root).grid(row=4, column=0, sticky="nsew")
# Third root of a number
third_root   = Button(calculator, button_style, text='\u00B3\u221A', command=third_root).grid(row=4, column=1, sticky="nsew")
# nth root of a number
nth_root     = Button(calculator, button_style, text='\u221A', command=lambda:button_click('**(1/')).grid(row=4, column=2, sticky="nsew")
# Log 10
log_base10   = Button(calculator, button_style, text='log\u2081\u2080', font=('sans-serif', 16, 'bold'), command=lambda:button_click('log(')).grid(row=4, column=3, sticky="nsew")
# e (ln)
log_basee    = Button(calculator, button_style, text='ln',   command=lambda:button_click('ln(')).grid(row=4, column=4, sticky="nsew")


#(
left_par   = Button(calculator, button_style, text='(',      command=lambda:button_click('(')).grid(row=5, column=0, sticky="nsew")
#)
right_par  = Button(calculator, button_style, text=')',      command=lambda:button_click(')')).grid(row=5, column=1, sticky="nsew")   
# + and -
signs      = Button(calculator, button_style, text='\u00B1', command=sign_change).grid(row=5, column=2, sticky="nsew")
# %
percentage = Button(calculator, button_style, text='%',      command=percent).grid(row=5, column=3, sticky="nsew")
# e^x
ex         = Button(calculator, button_style, text='e^x',    command=lambda:button_click('e(')).grid(row=5, column=4, sticky="nsew")


button_1   = Button(calculator, button_style, text='1', command=lambda:button_click('1')).grid(row=8, column=0, sticky="nsew")
button_2   = Button(calculator, button_style, text='2', command=lambda:button_click('2')).grid(row=8, column=1, sticky="nsew")
button_3   = Button(calculator, button_style, text='3', command=lambda:button_click('3')).grid(row=8, column=2, sticky="nsew")
button_4   = Button(calculator, button_style, text='4', command=lambda:button_click('4')).grid(row=7, column=0, sticky="nsew")
button_5   = Button(calculator, button_style, text='5', command=lambda:button_click('5')).grid(row=7, column=1, sticky="nsew")
button_6   = Button(calculator, button_style, text='6', command=lambda:button_click('6')).grid(row=7, column=2, sticky="nsew")

button_7   = Button(calculator, button_style, text='7', command=lambda:button_click('7')).grid(row=6, column=0, sticky="nsew")
button_8   = Button(calculator, button_style, text='8', command=lambda:button_click('8')).grid(row=6, column=1, sticky="nsew")
button_9   = Button(calculator, button_style, text='9', command=lambda:button_click('9')).grid(row=6, column=2, sticky="nsew")

add        = Button(calculator, button_style, text='+', command=lambda:button_click('+')).grid(row=8, column=3, sticky="nsew")
sub        = Button(calculator, button_style, text='-', command=lambda:button_click('-')).grid(row=8, column=4, sticky="nsew")
mul        = Button(calculator, button_style, text='*', command=lambda:button_click('*')).grid(row=7, column=3, sticky="nsew")
div        = Button(calculator, button_style, text='/', command=lambda:button_click('/')).grid(row=7, column=4, sticky="nsew")

delete_one = Button(calculator, button_style, text='DEL', command=button_delete, bg='#db701f').grid(row=6, column=3, sticky="nsew")
delete_all = Button(calculator, button_style, text='AC',  command=button_clear_all, bg='#db701f').grid(row=6, column=4, sticky="nsew")


button_0 = Button(calculator, button_style, text='0', command=lambda:button_click('0')).grid(row=9, column=0, sticky="nsew")
point = Button(calculator, button_style, text='.', command=lambda:button_click('.')).grid(row=9, column=1, sticky="nsew")
exp = Button(calculator, button_style, text='EXP', font=('sans-serif', 16, 'bold'), command=lambda:button_click(E)).grid(row=9, column=2, sticky="nsew")
equal = Button(calculator, button_style, text='=', command=button_equal).grid(row=9, columnspan=2, column=3, sticky="nsew")



calculator.mainloop()