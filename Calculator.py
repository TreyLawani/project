import tkinter as tk
import re
import math

#Defining the calculator class
class Calculator:

    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        return a / b 
    
    def percentage(self, a, b):
        return (b / 100) * a
    
    def exp(self, a, b):
        return a**b 
    
    def sin(self, a):
        return math.sin(a)
    
    def cos(self, a):
        return math.cos(a)
    
    def tan(self, a):
        return math.tan(a)
    
    def log(self, a):
        return math.log10(a)
    
    def nat_log(self, a):
        return math.log1p(a)
    
    def square(self, a):
        return a**2
    
    def nat_exp(self, a):
        return math.exp(a)
    
    def square_root(self, a):
        return math.sqrt(a)
    
    def inverse(self, a):
        return 1 / a
    

calc = Calculator()

# Function to change string expressions in the top row

def changeExpression(value):
    global expression
    expression.configure(text=expression.cget("text") + str(value))
    expression.update()

def clearExpression():
    global expression
    expression.configure(text="")
    expression.update


def handleNegation():
    global expression
    text = expression.cget("text")
    if text[0] == "-":
        text = text[1:]
    else:
        text = "-" + text 
    expression.configure(text=text)
    expression.update()


def handleDel():
    global expression
    expression.configure(text=expression.cget("text")[:-1]) 
    expression.update()


def handleSubmit():
    global expression
    try:
        equation = expression.cget("text")
        neg = False
        if equation[0] == "-":
            neg = True
            equation = equation[1:]
        terms = re.split(r"([-+x/%^])",equation)
        if len(terms) !=3:
                return
            
        print(terms)
        if neg == True:
            terms[0] = "-" + terms[0]
        terms[0] = float(terms[0])
        terms[2] = float(terms[2])
        operation = terms[1]

        if operation == "+":
            ans = calc.add(terms[0],terms[2])
        elif operation == "-":
            ans = calc.subtract(terms[0],terms[2])
        elif operation == "x":
            ans = calc.multiply(terms[0],terms[2])
        elif operation == "/":
            ans = calc.divide(terms[0],terms[2])
        elif operation == "%":
            ans = calc.percentage(terms[0],terms[2])
        elif operation == "^":
            ans = calc.exp(terms[0],terms[2])
        
        expression.configure(text=str(ans))
        expression.update()
    except Exception as e:
        print(e)
        expression.configure(text="Error")
        expression.update()


def handleAdvanced(operation):
    global expression 
    try:
        equation = expression.cget("text")
        term = float(equation)

        if operation == "sin":
            ans = calc.sin(term)
        elif operation == "cos":
            ans = calc.cos(term)
        elif operation == "tan":
            ans = calc.tan(term)
        elif operation == "log":
            ans = calc.log(term)
        elif operation == "nat_log":
            ans = calc.nat_log(term)
        elif operation == "square":
            ans = calc.square(term)
        elif operation == "nat_exp":
            ans = calc.nat_exp(term)
        elif operation == "square_root":
            ans = calc.square_root(term)
        elif operation == "inverse":
            ans = calc.inverse(term)

        expression.configure(text=str(ans))
        expression.update()
    except:
        expression.configure(text="Error")
        expression.update()


def createAdvancedButton(display,
    operation):
    return tk.Button(
        text=str(display),
        width=10,
        height=5,
        bg="gray",
        fg="black",
        padx=1,
        pady=1,
        font=("Courier", 20),
        command=lambda: handleAdvanced(operation=operation),
    )


def createButton(value):
    return tk.Button(
        text=str(value),
        width=10,
        height=5,
        bg="gray",
        fg="black",
        padx=1,
        pady=1,
        font=("Courier", 20),
        command=lambda: changeExpression(value=value),
    )


main_window = tk.Tk()

expression = tk.Label(text="", font=("Courier", 84))
expression.grid(row=0, column=0, columnspan=6, sticky=tk.W + tk.E, pady=2, padx=2)

button_clear = tk.Button(
    text="Clear",
    width=10,
    height=5,
    bg="gray",
    fg="black",
    padx=2,
    pady=2,
    font=("Courier", 20),
    command=clearExpression,
)
button_clear.grid(row=1, column=0, sticky=tk.W, pady=2, padx=2)

button_del = tk.Button(
    text="Del",
    width=10,
    height=5,
    bg="gray",
    fg="black",
    padx=2,
    pady=2,
    font=("Courier", 20),
    command=handleDel,
)
button_del.grid(row=1, column=1, sticky=tk.W, pady=2, padx=2)

# Function to create Buttons
button_percent = createButton("%")
button_percent.grid(row=1, column=2, sticky=tk.W, pady=2, padx=2)

button_div = createButton("/")
button_div.grid(row=1, column=3, sticky=tk.W, pady=2, padx=2)

button_exp = createButton("^")
button_exp.grid(row=1, column=4, sticky=tk.W, pady=2, padx=2)

button_sin = createAdvancedButton("sin", "sin")
button_sin.grid(row=1, column=5, sticky=tk.W, pady=2, padx=2)

button_7 = createButton(7)
button_7.grid(row=2, column=0, sticky=tk.W, pady=2, padx=2)

button_8 = createButton(8)
button_8.grid(row=2, column=1, sticky=tk.W, pady=2, padx=2)

button_9 = createButton(9)
button_9.grid(row=2, column=2, sticky=tk.W, pady=2, padx=2)

button_x = createButton("x")
button_x.grid(row=2, column=3, sticky=tk.W, pady=2, padx=2)

button_cos = createAdvancedButton("cos", "cos")
button_cos.grid(row=2, column=4, sticky=tk.W, pady=2, padx=2)

button_tan = createAdvancedButton("tan", "tan")
button_tan.grid(row=2, column=5, sticky=tk.W, pady=2, padx=2)

button_4 = createButton(4)
button_4.grid(row=3, column=0, sticky=tk.W, pady=2, padx=2)

button_5 = createButton(5)
button_5.grid(row=3, column=1, sticky=tk.W, pady=2, padx=2)

button_6 = createButton(6)
button_6.grid(row=3, column=2, sticky=tk.W, pady=2, padx=2)

button_sub = createButton("-")
button_sub.grid(row=3, column=3, sticky=tk.W, pady=2, padx=2)

button_log = createAdvancedButton("log10", "log")
button_log.grid(row=3, column=4, sticky=tk.W, pady=2, padx=2)

button_nat_log = createAdvancedButton("ln", "nat_log")
button_nat_log.grid(row=3, column=5, sticky=tk.W, pady=2, padx=2)

button_1 = createButton(1)
button_1.grid(row=4, column=0, sticky=tk.W, pady=2, padx=2)

button_2 = createButton(2)
button_2.grid(row=4, column=1, sticky=tk.W, pady=2, padx=2)

button_3 = createButton(3)
button_3.grid(row=4, column=2, sticky=tk.W, pady=2, padx=2)

button_add = createButton("+")
button_add.grid(row=4, column=3, sticky=tk.W, pady=2, padx=2)

button_square = createAdvancedButton("x^2", "square")
button_square.grid(row=4, column=4, sticky=tk.W, pady=2, padx=2)

button_nat_exp = createAdvancedButton("e^x", "nat_exp")
button_nat_exp.grid(row=4, column=5, sticky=tk.W, pady=2, padx=2)


button_neg = tk.Button(
    text="+/-",
    width=10,
    height=5,
    bg="gray",
    fg="black",
    padx=2,
    pady=2,
    font=("Courier", 20),
    command=handleNegation,
)
button_neg.grid(row=5, column=0, sticky=tk.W, pady=2, padx=2)

button_0 = createButton(0)
button_0.grid(row=5, column=1, sticky=tk.W, pady=2, padx=2)

button_dot = createButton(".")
button_dot.grid(row=5, column=2, sticky=tk.W, pady=2, padx=2)

button_eq = tk.Button(
    text="=",
    width=10,
    height=5,
    bg="gray",
    fg="black",
    padx=2,
    pady=2,
    font=("Courier", 20),
    command=handleSubmit,
)
button_eq.grid(row=5, column=3, sticky=tk.W, pady=2, padx=2)

button_square_root = createAdvancedButton("sq. root", "square_root")
button_square_root.grid(row=5, column=4, sticky=tk.W, pady=2, padx=2)

button_inverse = createAdvancedButton("1/x", "inverse")
button_inverse.grid(row=5, column=5, sticky=tk.W, pady=2, padx=2)

main_window.mainloop()
