
# Aaron Walker

# Ask the user to enter five numbers
number1 = int(input("What is the first number? "))
number2 = int(input("What is the second number? "))
number3 = int(input("What is the third number? "))
number4 = int(input("What is the fourth number? "))
number5 = int(input("What is the fifth number? "))

# Create a list to store the numbers
my_list = []

# Add the numbers to the list
my_list.append(number1)
my_list.append(number2)
my_list.append(number3)
my_list.append(number4)
my_list.append(number5)

# Display the original list
print("Original list:", my_list)

# Use sorted() to display the numbers in ascending order
print("Sorted list using sorted():", sorted(my_list))

# Create a copy of the original list using slicing
sorted_list = my_list[:]

# Sort the copied list in place in ascending order
sorted_list.sort()

# Display the sorted list
print("List after sort():", sorted_list)

# Create a copy of the sorted list
new_list = sorted_list[:]

# Ask the user to enter an additional number
number6 = int(input("What is your extra number? "))

# Add the new number to the end of the copied list
new_list.append(number6)

# Display the list after adding the new number
print("List after adding a number:", new_list)

# Create a copy of the list containing six numbers
deleted_list = new_list[:]

# Delete the first element of the copied list
del deleted_list[0]

# Display the list after deleting the first element
print("List after deleting the first element:", deleted_list)

# Create a copy of the list after deletion
reversed_list = deleted_list[:]

# Reverse the order of the elements in the copied list
reversed_list.reverse()

# Display the reversed list
print("Reversed list:", reversed_list)
