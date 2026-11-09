# Aaron Walker

from mypackage import utilities

# Ask the user for their name
name = input("Enter your name: ")

# Ask the user for a number
number = int(input("Enter a number to calculate: "))

# Display greeting
print(utilities.greet(name))

# Display factorial
print("Factorial of", number, "is:", utilities.factorial(number))
