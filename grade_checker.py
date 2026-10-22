# Aaron Walker

# Ask the user to enter a numeric grade
grade = float(input("Enter your numeric grade (0-100): "))

# Validate the grade
if not 0 <= grade <= 100:
    print("Invalid grade. Please enter a value from 0 to 100.")
else:
    # Determine the letter grade
    if grade >= 90:
        letter_grade = "A"
    elif grade >= 80:
        letter_grade = "B"
    elif grade >= 70:
        letter_grade = "C"
    elif grade >= 60:
        letter_grade = "D"
    else:
        letter_grade = "F"

    # Print the letter grade
    print(f"Your grade is: {letter_grade}")

    message = (
        "Congratulations! You passed!"
        if letter_grade in ("A", "B", "C")
        else "Keep trying! You can do better next time."
    )

    print(message)
