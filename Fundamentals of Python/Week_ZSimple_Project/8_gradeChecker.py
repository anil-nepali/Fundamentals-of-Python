print(" ---------------------------------------------------------------- ")
print(" -------Pokhara University Grading System---------- ")
# Show the grading scale table
print("\n + = *60")
print(" POKHARA UNIVERSITY BEIT - GRADING SCALE ")
print(" = *60")
print(" Percentage Range | Grade | Points | Description ")
print("- * 60")
print(" 90 and above | A | 4.0 | Outstanding ")
print(" 85 to less than 90 | A- | 3.7 | Excellent ")
print(" 80 to less than 85 | B+ | 3.3 | Very Good ")
print(" 75 to less than 80 | B | 3.0 | Good ")
print(" 70 to less than 75 | B- | 2.7 | Fair ")
print(" 65 to less than 70 | C+ | 2.3 | Fair ")
print(" 60 to less than 65 | C | 2.0 | Fair ")
print(" 55 to less than 60 | C- | 1.7 | Poor ")
print(" 50 to less than 55 | D+ | 1.3 | Poor ")
print(" 45 to less than 50 | D | 1.0 | Poor (Minimum Pass) ")
print(" Below 45 | F | 0.0 | Fail ")

try:
    # Use float for marks in case a student gets a non-integer score, or int if only whole numbers are used.
    # The original prompt used int(), so we stick with that for consistency.
    marks = int(input("Enter the Marks obtain by student: "))
    grade = ""
    points = 0.0
    description = ""

    if marks >= 90:
        grade = "A"
        points = 4.0
        description = "Outstanding"
    elif marks >= 85:
        grade = "A-"
        points = 3.7
        description = "Excellent"
    elif marks >= 80:
        grade = "B+"
        points = 3.3
        description = "Very Good"
    elif marks >= 75:
        grade = "B"
        points = 3.0
        description = "Good"
    elif marks >= 70:
        grade = "B-"
        points = 2.7
        description = "Fair"
    elif marks >= 65:
        grade = "C+"
        points = 2.3
        description = "Fair"
    elif marks >= 60:
        grade = "C"
        points = 2.0
        description = "Fair"
    elif marks >= 55:
        grade = "C-"
        points = 1.7
        description = "Poor"
    elif marks >= 50:
        grade = "D+"
        points = 1.3
        description = "Poor"
    elif marks >= 45:
        grade = "D"
        points = 1.0
        description = "Poor (Minimum Pass)"
    else:
        grade = "F"
        points = 0.0
        description = "Fail"

    # Print the results
    print("----------------------------------------------------------------")
    print(f"Marks Obtained: {marks}")
    print(f"Grade: {grade}")
    print(f"Grade Points: {points}")
    print(f"Description: {description}")
    print("----------------------------------------------------------------")

except ValueError:
    print("Invalid input. Please enter a valid number for marks.")
    