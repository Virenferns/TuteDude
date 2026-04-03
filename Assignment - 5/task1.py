"""
Task 1: Create a Dictionary of Student Marks

Problem Statement: Write a Python program that:
1. Creates a dictionary where student names are keys and their marks are values.
2. Asks the user to input a student's name.
3. Retrieves and displays the corresponding marks.
4. If the student’s name is not found, display an appropriate message.
"""

student_dict = {
    'alice': 85,
    'bob': 90,
}
try:
    user_input = input("Enter the student's name: ")
    user_input = user_input.lower()
    marks = student_dict[user_input]
except KeyError as err:
    print("Student not found.")
else:
    print(f"{user_input.capitalize()}'s marks: {marks}")