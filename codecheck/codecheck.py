#Anna Vosko CS361
#This code is going to run thru some math operators as a Mathbot

def add(num1, num2):
    print(float(num1) + float(num2))

def subtract(num1, num2):
    print(float(num1) - float(num2))

def multi(num1, num2):
    print(float(num1) * float(num2))

def divide(num1, num2):
    print(float(num1) / float(num2))

def prompt():
    equation = input("SuperMathyBot> ")
    return equation.split(" ")
    
while True:
    equa = prompt()
    if equa[0] == "add":
        add(equa[1],equa[2])
    elif equa[0] == "sub":
        subtract(equa[1],equa[2])
    elif equa[0] == "mul":
        multi(equa[1],equa[2])
    elif equa[0] == "div":
        if equa[2] == "0":
            print("cant divide by zero")
        else:
            divide(equa[1],equa[2])
    elif equa[0] == "quit":
        break
    else: print("usage: add|sub|mul|div v0 v1 quit")