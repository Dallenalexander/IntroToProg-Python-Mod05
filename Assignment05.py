# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   Dallen Teruel, 2/25/26, Modify Script
# ------------------------------------------------------------------------------------------ #

import json
from io import TextIOWrapper

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''

FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
file: TextIOWrapper = None  # Holds a reference to an opened file. (Changed to use _io.TextIOWrapper instead of None)
menu_choice: str = ''  # Hold the choice made by the user.
student_data: dict = {}  # one row of student data (Changed from list to dictionary)
students: list = []  # a table of student data

# Processing/Error handling when the file is read into the list of dictionary rows.
try:
    file = open(FILE_NAME, "r")
    students = json.load(file)
except FileNotFoundError as e:
    print("Text file must exist before running this script!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
except Exception as e:
    print("There was a non-specific error!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
finally:
    # Check if a file object exists and is still open
    if file is not None and file.closed == False:
        file.close()

# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    # Error handling when the user enters a first name.
    if menu_choice == "1":  # This will not work if it is an integer!
        try:
            # Input the data
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")
            # Error handling when the user enters a last name.
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")

            course_name = input("Please enter the name of the course: ")
            if course_name.isalnum():
                raise ValueError("Course name should contain alpha and numeric values")

            student_data = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            students.append(student_data)
            print("\nStudent registered successfully!\n")
        except ValueError as e:
            print(e)  # Prints the custom message
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
        except Exception as e:
            print("There was a non-specific error!\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
        continue  # the loop

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-" * 50)
        print(f"Current Student Registrations:")
        for student in students:
            print(f"Student {student['FirstName']},{student['LastName']} is enrolled in {student['CourseName']}")
        print("-" * 50)
        continue

    # Save the data to a file
    # Error handling when the dictionary rows are written to the file.
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file, indent=2)
            print("-" * 50)
            print("Data Saved!")
            print("-" * 50)
        except TypeError as e:
            print("Please check that the data is a valid JSON format\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
        except Exception as e:
            print("-- Technical Error Message -- ")
            print("Built-In Python error info: ")
            print(e, e.__doc__, type(e), sep='\n')
        finally:
            if file is not None and file.closed == False:
                file.close()
        continue  # the loop

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop

    else:
        print("Please only choose option 1, 2, 3, or 4")

print("Program Ended")
