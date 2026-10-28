# Aaron Walker



def safe_divide(a, b):
    """Divide a by b, raising ValueError if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


# Interactive division
try:
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))

    result = safe_divide(a, b)
    print(f"Result: {result}")

except ValueError as e:
    print(f"Error: {e}")

finally:
    print("Division operation completed")


# Demonstrate catching a generic exception
try:
    text = input("\nEnter a whole number to convert: ")
    number = int(text)
    print(f"Converted number: {number}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")

