 #Objective: The aim of this assignment is to build a basic calculator that can perform addition, subtraction, multiplication, and division.
 # Task 1: Create functions for each arithmetic operation.

def addition(a,b):
    return  a + b

def subtraction(a,b):
    return a - b

def multiplication(a,b):
    return a * b

def division(a,b):
    try: 
        return a / b
    except ZeroDivisionError:
        print(f"Cant Divide By Zero")

def get_numbers():
    a = int(input("Enter Number: "))
    b = int(input("Enter Second Number: "))
    return a,b

# Task 2 : Use inputs to ask the user what operation they want to perform, and what numbers they want to use.

def calculator():
    while True:
        operation = input("What is the operation you would like to use: (+,-,/,*)")
        if operation == "exit":
            break
        if operation == "+":
            a,b = get_numbers()
            print(addition(a,b))
        elif operation == "-":
            a,b = get_numbers()
            print(subtraction(a,b))
        elif operation == "/":
            a,b = get_numbers()
            print(division(a,b))
        elif operation == "*": 
            a,b = get_numbers()
            print(multiplication(a,b))
        else:
            print(f'This operation is invalid....')
calculator()





