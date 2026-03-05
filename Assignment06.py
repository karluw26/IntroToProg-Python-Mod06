# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   ...,1/1/2026,Created Script
#   ...,3/4/2026,Updated script for assignment 6.
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course
    2. Show current data  
    3. Save data to a file
    4. Exit the program
----------------------------------------- 
'''
# Define the Data Constants
# FILE_NAME: str = "Enrollments.csv"
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
students: list = []  # a table of student data
menu_choice: str = ''  # Hold the choice made by the user.


class FileProcessor:
    """
       A collection of functions that perform file reads and writes.

       ChangeLog: (Who, When, What)
       KJreijiri,3.4.2026,Created Class
   """

    @staticmethod
    def read_data_from_file(file_name: str):
        """
        Read student data from file.

        ChangeLog: (Who, When, What)
        KJreijiri,3.4.2026,Created Function

        :param file_name: str file name to read the student data from.
        :return: list of dicts of student data
        """
        file = None
        students_read: list = []
        try:
            file = open(file_name, "r")
            students_read = json.load(file)
        except Exception as e:
            IO.output_error_messages("There was a problem with reading the file.", e)
        finally:
            # Check if a file object exists and is still open
            if file is not None and file.closed == False:
                file.close()
        return students_read

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """
        Write student data to file.

        ChangeLog: (Who, When, What)
        KJreijiri,3.4.2026,Created Function

        :param file_name: str file name to write the student data to.
        :param student_data: list of student data.
        :return: None
        """
        file = None
        try:
            file = open(file_name, "w")
            json.dump(student_data, file, indent=2)
            print("The following data was saved to file!")
            for student in student_data:
                print(f'Student {student["FirstName"]} '
                      f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        except Exception as e:
            IO.output_error_messages("There was a problem with writing to the file.", e)
        finally:
            # Check if a file object exists and is still open
            if file is not None and file.closed == False:
                file.close()
        return


class IO:
    """
       A collection of functions that perform program console input and output.

       ChangeLog: (Who, When, What)
       KJreijiri,3.4.2026,Created Class
   """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """
        Display custom error message to the user.

        ChangeLog: (Who, When, What)
        KJreijiri,3.4.2026,Created Function

        :param message: str custom error message.
        :param error: Exception error object. Default to None.
        :return: None
        """
        print(f"Error: {message}\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')
        return

    @staticmethod
    def output_menu(menu: str):
        """
        Display program menu.

        ChangeLog: (Who, When, What)
        KJreijiri,3.4.2026,Created Function

        :return: None
        """
        print(f"\n{menu}\n")
        return

    @staticmethod
    def input_menu_choice():
        """
        Get input from user for the choice in the program menu.

        ChangeLog: (Who, When, What)
        KJreijiri,3.4.2026,Created Function

        :return: str selected menu choice
        """
        input_choice = input("\nWhat would you like to do: ")
        try:
            if input_choice not in ["1", "2", "3", "4"]:
                raise Exception(f"Invalid menu choice '{input_choice}'."
                                "You can only choose 1, 2, 3, or 4.")
        except Exception as e:
            IO.output_error_messages(e.__str__())
        return input_choice

    @staticmethod
    def output_student_courses(student_data: list):
        """
        Process the data to create and display CSV rows of student data.

        ChangeLog: (Who, When, What)
        KJreijiri,3.4.2026,Created Function

        :param student_data: list of students.
        :return: None
        """
        # Process the data to create and display a custom message
        print("-" * 50)
        for student in student_data:
            print(f'{student["FirstName"]},{student["LastName"]},{student["CourseName"]}')
        print("-" * 50)
        return

    @staticmethod
    def input_student_data(student_data: list):
        """
        Insert data to create and display student data.

        ChangeLog: (Who, When, What)
        KJreijiri,3.4.2026,Created Function

        :param student_data: list of students.
        :return: list of student data
        """
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student_obj = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            student_data.append(student_obj)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except Exception as e:
            IO.output_error_messages("There was a problem with your entered data.", e)
        return student_data


# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
students = FileProcessor.read_data_from_file(FILE_NAME)

# Present and Process the data
while (True):

    # Present the menu of choices
    IO.output_menu(MENU)
    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        students = IO.input_student_data(students)
        continue

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_courses(students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(FILE_NAME, students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop

print("Program Ended")
