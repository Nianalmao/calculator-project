def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def divide(x,y):
    return x / y

def multiply(x,y):
    return x * y

def power(x,y):
    return x**y

a = int(input("gimme a number: "))
b= int(input("another one: "))
operator = input("choose an operator(+, -, /, * or **): ")
while not (operator in ["+","-","/","*","**"]):
    print("DONT FUCKING INPUT SOMETHING ELSE!!")
    operator = input("TRY AGAIN: ")

def calculator(a,b,operator):
    if (operator == "+"):
        return add(a,b)
    elif (operator == "-"):
        return subtract(a,b)
    elif (operator == "/"):
        return divide(a,b)
    elif (operator == "*"):
        return multiply(a,b)
    else:
        return power(a,b)

result = calculator(a, b, operator)
print("The result is:", result)