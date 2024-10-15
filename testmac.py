import tkinter as tk
from tkinter import font
from tkinter import *
window = tk.Tk()
window.title("Calculator")
window.geometry("1440x1080")
global variable_bg
variable_bg = ""
window.configure(bg=variable_bg)
global placeholder
placeholder = ""
num = 0
expression = ""
global button_bg
button_bg = "orange"
globalButtonBG = "orange"
equation = StringVar() 

# The following code below detects the button press of a number and adds it into an equation.
def change(num):
    global expression
    if num == 1:
        placeholder = "1"
    elif num == 2:
        placeholder = "2"
    elif num == 3:
        placeholder = "3"
    elif num == 4:
        placeholder = "4"
    elif num == 5:
        placeholder = "5"
    elif num == 6:
        placeholder = "6"
    elif num == 7:
        placeholder = "7"
    elif num == 8:
        placeholder = "8"
    elif num == 9:
        placeholder = "9"
    elif num == "+":
        placeholder = "+"
    elif num == "-":
        placeholder = "-"
    elif num == "*":
        placeholder = "*"
    elif num == "/":
        placeholder = "/"
    else:
        placeholder = "0"
    global screen
    screen = tk.Entry(window, text=equation, font=("calibri", 69), foreground="white", background="#b6cfcb", bd="3")
    screen.config(width="14")
    screen.place(x=430, y=195)
    expression = expression + str(num)
    equation.set(expression)

# The equal button down below will calculate the final expression
def equalOmega():
    try:
        global expression
        final = str(eval(expression))
        equation.set(final)
        expression = ""
    except:
        equation.set("error")
        expression = ""

# The clear button sets the expression back to "0"
def clearCE():
    global expression
    clear = "0"
    equation.set(clear)
    expression = ""

# The following code down below lets the user pick their preferred theme for the calculator
def themeChange(variable_bg, button_bg, operator_bg):
    window.configure(bg=variable_bg)
    globalButtonBG = button_bg
    button1 = tk.Button(window, text="1", font=("arial", 50), bg=globalButtonBG, bd="3"
, activebackground = "green", activeforeground = "white", command=lambda: change(1))
    button1.place(x=560, y=400)
    button2 = tk.Button(window, text="2", font=("arial", 50), bg =globalButtonBG, bd="3"
, activebackground = "green", activeforeground = "white", command=lambda: change(2))
    button2.place(x=710, y=400)
    button3 = tk.Button(window, text="3", font=("arial", 50), bg =globalButtonBG, bd="3"
, activebackground = "green", activeforeground = "white", command=lambda: change(3))
    button3.place(x=860, y=400)
    button4 = tk.Button(window, text="4", font=("arial", 50), bg =globalButtonBG, bd="3"
, activebackground = "green", activeforeground = "white", command=lambda: change(4))
    button4.place(x=560, y=550)
    button5 = tk.Button(window, text="5", font=("arial", 50), bg =globalButtonBG, bd="3"
, activebackground = "green", activeforeground = "white", command=lambda: change(5))
    button5.place(x=710, y=550)
    button6 = tk.Button(window, text="6", font=("arial", 50), bg =globalButtonBG, bd="3"
, activebackground = "green", activeforeground = "white", command=lambda: change(6))
    button6.place(x=860, y=550)
    button7 = tk.Button(window, text="7", font=("arial", 50), bg =globalButtonBG, bd="3"
, activebackground = "green", activeforeground = "white", command=lambda: change(7))
    button7.place(x=560, y=700)
    button8 = tk.Button(window, text="8", font=("arial", 50), bg =globalButtonBG, bd="3"
, activebackground = "green", activeforeground = "white", command=lambda: change(8))
    button8.place(x=710, y=700)
    button9 = tk.Button(window, text="9", font=("arial", 50), bg =globalButtonBG, bd="3"
, activebackground = "green", activeforeground = "white", command=lambda: change(9))
    button9.place(x=860, y=700)
    button0 = tk.Button(window, text="0", font=("arial", 50), bg =globalButtonBG, bd="3"
, activebackground = "green", activeforeground = "white", command=lambda: change(0))
    button0.place(x=710, y=850)
    operators = ["+", "-", "*", "/", "=", "CE"]
    buttonplus = tk.Button(window, text=operators[0], font=("arial", 30), bg =operator_bg, bd="3"
, activebackground = "green", activeforeground = "white", command=lambda: change("+"))
    buttonplus.place(x=400, y=400)

    buttonminus = tk.Button(window, text=operators[1], font=("arial", 35), bg =operator_bg, bd="3"
    , activebackground = "green", activeforeground = "white", command=lambda: change("-"))
    buttonminus.place(x=400, y=500)

    buttontimes = tk.Button(window, text=operators[2], font=("arial", 35), bg =operator_bg, bd="3"
, activebackground = "green", activeforeground = "white", command=lambda: change("*"))
    buttontimes.place(x=400, y=600)

    buttondivide = tk.Button(window, text=operators[3], font=("arial", 35), bg =operator_bg, bd="3"
    , activebackground = "green", activeforeground = "white", command=lambda: change("/"))
    buttondivide.place(x=402, y=725)

    buttonequal = tk.Button(window, text=operators[4], font=("arial", 35), bg =operator_bg, bd="3"
    ,activebackground = "green", activeforeground = "white", command=equalOmega)
    buttonequal.place(x=1025, y=700)

    buttonclear = tk.Button(window, text=operators[5], font=("arial", 35), bg =operator_bg, bd="3"
    ,activebackground = "green", activeforeground = "white", command=clearCE)
    buttonclear.place(x=1025, y=900)

# Let's the user pick a random theme
def randTheme():
    import random
    themes = ["skyTheme", "spaceTheme", "coffeeTheme"]
    finalTheme = random.choice(themes)
    if finalTheme == "skyTheme":
        variable_bg = "cyan"
        globalButtonBG = "white"
        operator_bg = "yellow"
    elif finalTheme == "spaceTheme":
        variable_bg = "black"
        globalButtonBG = "green"
        operator_bg = "gray"
    else:
        variable_bg = "beige"
        globalButtonBG = "#f0d973"
        operator_bg = "white"
    window.configure(bg=variable_bg)
    button1 = tk.Button(window, text="1", font=("arial", 50), bg=globalButtonBG, bd="3"
, activebackground = "green", activeforeground = "white", command=lambda: change(1))
    button1.place(x=560, y=400)
    button2 = tk.Button(window, text="2", font=("arial", 50), bg =globalButtonBG, bd="3"
, activebackground = "green", activeforeground = "white", command=lambda: change(2))
    button2.place(x=710, y=400)
    button3 = tk.Button(window, text="3", font=("arial", 50), bg =globalButtonBG, bd="3"
, activebackground = "green", activeforeground = "white", command=lambda: change(3))
    button3.place(x=860, y=400)
    button4 = tk.Button(window, text="4", font=("arial", 50), bg =globalButtonBG, bd="3"
, activebackground = "green", activeforeground = "white", command=lambda: change(4))
    button4.place(x=560, y=550)
    button5 = tk.Button(window, text="5", font=("arial", 50), bg =globalButtonBG, bd="3"
, activebackground = "green", activeforeground = "white", command=lambda: change(5))
    button5.place(x=710, y=550)
    button6 = tk.Button(window, text="6", font=("arial", 50), bg =globalButtonBG, bd="3"
, activebackground = "green", activeforeground = "white", command=lambda: change(6))
    button6.place(x=860, y=550)
    button7 = tk.Button(window, text="7", font=("arial", 50), bg =globalButtonBG, bd="3"
, activebackground = "green", activeforeground = "white", command=lambda: change(7))
    button7.place(x=560, y=700)
    button8 = tk.Button(window, text="8", font=("arial", 50), bg =globalButtonBG, bd="3"
, activebackground = "green", activeforeground = "white", command=lambda: change(8))
    button8.place(x=710, y=700)
    button9 = tk.Button(window, text="9", font=("arial", 50), bg =globalButtonBG, bd="3"
, activebackground = "green", activeforeground = "white", command=lambda: change(9))
    button9.place(x=860, y=700)
    button0 = tk.Button(window, text="0", font=("arial", 50), bg =globalButtonBG, bd="3"
, activebackground = "green", activeforeground = "white", command=lambda: change(0))
    button0.place(x=710, y=850)
    operators = ["+", "-", "*", "/", "=", "CE"]
    buttonplus = tk.Button(window, text=operators[0], font=("arial", 30), bg =operator_bg, bd="3"
, activebackground = "green", activeforeground = "white", command=lambda: change("+"))
    buttonplus.place(x=400, y=400)

    buttonminus = tk.Button(window, text=operators[1], font=("arial", 35), bg =operator_bg, bd="3"
    , activebackground = "green", activeforeground = "white", command=lambda: change("-"))
    buttonminus.place(x=400, y=500)

    buttontimes = tk.Button(window, text=operators[2], font=("arial", 35), bg =operator_bg, bd="3"
, activebackground = "green", activeforeground = "white", command=lambda: change("*"))
    buttontimes.place(x=400, y=600)

    buttondivide = tk.Button(window, text=operators[3], font=("arial", 35), bg =operator_bg, bd="3"
    , activebackground = "green", activeforeground = "white", command=lambda: change("/"))
    buttondivide.place(x=402, y=725)

    buttonequal = tk.Button(window, text=operators[4], font=("arial", 35), bg =operator_bg, bd="3"
    ,activebackground = "green", activeforeground = "white", command=equalOmega)
    buttonequal.place(x=1025, y=700)

    buttonclear = tk.Button(window, text=operators[5], font=("arial", 35), bg =operator_bg, bd="3"
    ,activebackground = "green", activeforeground = "white", command=clearCE)
    buttonclear.place(x=1025, y=900)
import random
quotes = ["enjoy this calculator", "go on", "power"]
finalQuote = random.choice(quotes)
calculator_label = tk.Label(window, text="Calculator", font=("times", 96), foreground="white", background="black")
calculator_label.place(x=500, y=0)

quote_label = tk.Label(window, text=finalQuote, font=("times", 22), foreground="black", background="white")
quote_label.place(x=1150, y=400)
# Had extra space so I added some messages


# The general calculator buttons listed down here

button1 = tk.Button(window, text="1", font=("arial", 50), bg=globalButtonBG, bd="3"
, activebackground = "green", activeforeground = "white", command=lambda: change(1))
button1.place(x=560, y=400)

button2 = tk.Button(window, text="2", font=("arial", 50), bg ="orange", bd="3"
, activebackground = "green", activeforeground = "white", command=lambda: change(2))
button2.place(x=710, y=400)

button3 = tk.Button(window, text="3", font=("arial", 50), bg ="orange", bd="3"
, activebackground = "green", activeforeground = "white", command=lambda: change(3))
button3.place(x=860, y=400)

button4 = tk.Button(window, text="4", font=("arial", 50), bg ="orange", bd="3"
, activebackground = "green", activeforeground = "white", command=lambda: change(4))
button4.place(x=560, y=550)

button5 = tk.Button(window, text="5", font=("arial", 50), bg ="orange", bd="3"
, activebackground = "green", activeforeground = "white", command=lambda: change(5))
button5.place(x=710, y=550)

button6 = tk.Button(window, text="6", font=("arial", 50), bg ="orange", bd="3"
, activebackground = "green", activeforeground = "white", command=lambda: change(6))
button6.place(x=860, y=550)

button7 = tk.Button(window, text="7", font=("arial", 50), bg ="orange", bd="3"
, activebackground = "green", activeforeground = "white", command=lambda: change(7))
button7.place(x=560, y=700)

button8 = tk.Button(window, text="8", font=("arial", 50), bg ="orange", bd="3"
, activebackground = "green", activeforeground = "white", command=lambda: change(8))
button8.place(x=710, y=700)

button9 = tk.Button(window, text="9", font=("arial", 50), bg ="orange", bd="3"
, activebackground = "green", activeforeground = "white", command=lambda: change(9))
button9.place(x=860, y=700)

button0 = tk.Button(window, text="0", font=("arial", 50), bg ="orange", bd="3"
, activebackground = "green", activeforeground = "white", command=lambda: change(0))
button0.place(x=710, y=850)
operators = ["+", "-", "*", "/", "=", "CE"]
buttonplus = tk.Button(window, text=operators[0], font=("arial", 30), bg ="red", bd="3"
, activebackground = "green", activeforeground = "white", command=lambda: change("+"))
buttonplus.place(x=400, y=400)

buttonminus = tk.Button(window, text=operators[1], font=("arial", 35), bg ="red", bd="3"
, activebackground = "green", activeforeground = "white", command=lambda: change("-"))
buttonminus.place(x=400, y=500)

buttontimes = tk.Button(window, text=operators[2], font=("arial", 35), bg ="red", bd="3"
, activebackground = "green", activeforeground = "white", command=lambda: change("*"))
buttontimes.place(x=400, y=600)

buttondivide = tk.Button(window, text=operators[3], font=("arial", 35), bg ="red", bd="3"
, activebackground = "green", activeforeground = "white", command=lambda: change("/"))
buttondivide.place(x=402, y=725)

buttonequal = tk.Button(window, text=operators[4], font=("arial", 35), bg ="red", bd="3"
,activebackground = "green", activeforeground = "white", command=equalOmega)
buttonequal.place(x=1025, y=700)

buttonclear = tk.Button(window, text=operators[5], font=("arial", 35), bg ="red", bd="3"
,activebackground = "green", activeforeground = "white", command=clearCE)
buttonclear.place(x=1025, y=900)

skyTheme = tk.Button(window, text="Sky Theme", font=("arial", 22), bg ="cyan", bd="3"
,activebackground = "green", activeforeground="white", command=lambda: themeChange("cyan", "white", "yellow"))
skyTheme.place(x=155, y=200)

spaceTheme = tk.Button(window, text="Space Theme", font=("arial", 22), bg ="green", bd="3"
,activebackground = "green", activeforeground="white", command=lambda: themeChange("black", "green", "gray"))
spaceTheme.place(x=135, y=280)

coffeeTheme = tk.Button(window, text="Coffee Theme", font=("arial", 22), bg="#f0d973", bd="3"
,activebackground = "green", activeforeground="white", command=lambda: themeChange("beige", "#f0d973", "white"))
coffeeTheme.place(x=135, y=360)

randomTheme = tk.Button(window, text="Random Theme", font=("arial", 22), bg="teal", bd="3"
,activebackground = "green", activeforeground="white", command=randTheme)
randomTheme.place(x=125, y=440)
                                                                                   
window.mainloop()


