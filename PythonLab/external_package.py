# Aaron Walker


from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)

# Ask the user to enter their name
name = input("Enter your name: ")

# Display colored messages
print(Fore.GREEN + "Hello, " + name + "!")
print(Fore.YELLOW + "Welcome to Python packages!")
print(Fore.CYAN + "This message uses the Colorama package.")
print(Fore.RED + "Thank you for using this program!")
