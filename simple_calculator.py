#Aaron Walker

# variables are declared here
firstnum = float(input("What is your first number: "))
secondnum = float(input("What is your second number: "))
operation = input("Choose an operation (+, -, *, /): ")

# exception handling is done here
if operation.isdigit():
    print("This is not an operator")

# case of calculations is done here
elif operation == "+":
    result = firstnum + secondnum
    print(f"{firstnum} + {secondnum} = {result}")

elif operation == "-":
    result = firstnum - secondnum
    print(f"{firstnum} - {secondnum} = {result}")

elif operation == "*":
    result = firstnum * secondnum
    print(f"{firstnum} * {secondnum} = {result}")

elif operation == "/":
    if secondnum == 0:
        print("Error: Cannot divide by zero")
    else:
        result = firstnum / secondnum
        print(f"{firstnum} / {secondnum} = {result}")

else:
    print("Invalid operator")
