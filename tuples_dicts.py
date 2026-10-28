# Aaron Walker


# Create a tuple containing the twelve months
months = (
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
)

# Print the first and last month
print("First month:", months[0])
print("Last month:", months[-1])

# Attempt to modify the tuple to demonstrate immutability
try:
    months[0] = "NewMonth"
except TypeError as error:
    print(f"Tuples are immutable, error: {error}")

# Create a dictionary of students and their grades
students = {
    "Alice": 90,
    "Bob": 85,
    "Charlie": 92,
    "Diana": 88
}

# Add a new student and grade
students["Ethan"] = 95

# Print all student names and grades
print("\nAll students and grades:")
print(students)

# Update an existing student's grade
students["Bob"] = 91

# Print the updated entry
print("\nUpdated grade:")
print(f"Bob: {students['Bob']}")

# Loop through the dictionary and print each student and grade
print("\nStudent grades:")
for name, grade in students.items():
    print(f"{name}: {grade}")
