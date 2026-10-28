# Aaron Walker

# Add numbers
def add(a, b):
    return a + b

# Subtract numbers
def subtract(a, b):
    return a - b

# Multiply numbers
def mutilpy(a, * b):
    return a * b

# Divide numbers
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."


def calculate(a, b, op):
    if op == "+":
        return add(a, b)
    elif op == "-":
        return subtract(a, b)
    elif op == "*":
        return multiply(a, b)
    elif op == "/":
        return divide(a, b)
    else:
        return "Error: Invalid operation."


try:
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    op = input("Enter an operation (+, -, *, /): ")

    result = calculate(a, b, op)
    print("Result:", result)


except ValueError:
    print("Error: Please enter valid numbers.")
