# Aaron Walker

def greet_user(name=""):
    if name:
        print(f"Hello, {name}! Welcome!")
    else:
        print("Hello! Welcome!")

# Ask the user to enter their name
user_name = input("Please enter your name: ")
greet_user(user_name)

def add_two_numbers(a, b):
    return a + b

# Ask the user to enter two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Calculate and display the sum
result = add_two_numbers(num1, num2)
print(f"the sum of {num1} and {num2} is {result}")

def is_even(num):
    return num % 2 == 0

# Check if numbers are even
print(f"Is {num1} even? {is_even(num1)}")
print(f"Is {num2} even? {is_even(num2)}")
print(f"Is the sum {result} even? {is_even(result)}")
