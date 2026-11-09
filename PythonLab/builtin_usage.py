# Aaron Walker

import math
import random
import platform


# Generate a random integer between 1-100
number = random.randint(1, 100)

# Calculate the square root and round it down
square_root = math.floor(math.sqrt(number))

# Get Operating System and Python version
os_name = platform.system()
python_version = platform.python_version()

# Display results
print("Random Number:", number)
print("Square Root (floored):", square_root)
print("Operating System:", os_name)
print("Python Version:", python_version)
