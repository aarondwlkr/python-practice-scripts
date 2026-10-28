# Aaron Walker


# data_processing.py

def get_average_grade(grades_tuple):
    """Return the average of a tuple of numeric grades."""
    try:
        return sum(grades_tuple) / len(grades_tuple)
    except ZeroDivisionError:
        print("Warning: Cannot calculate the average of an empty tuple.")
        return None


# Dictionary containing course names and their grades
course_grades = {
    "Math": (90, 85, 88, 78),
    "Science": (92, 87, 95, 89),
    "History": (80, 84, 79, 85),
    "Art": ()  # Edge case: no grades available
}


# Process each course and display its average grade
for course, grades_tuple in course_grades.items():
    try:
        average = get_average_grade(grades_tuple)

        if average is not None:
            print(f"The average grade for {course} is {average:.1f}")
        else:
            print(f"The average grade for {course} is unavailable.")

    except (TypeError, ValueError) as error:
        print(f"Could not process grades for {course}: {error}")


