# Aaron Walker

import math

# Greeting function
def greet(name):
    return "Hello, " + name + "! Welcome to Python modules."

# Factorial function
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."

    return math.factorial(n)
