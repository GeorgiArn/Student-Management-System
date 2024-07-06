# Dictionary to store student records
students = {}


def add_student(name, age, grade, subjects):
    """
    Add a new student record.
    Args:
    - name (str): The name of the student.
    - age (int): The age of the student.
    - grade (float): The grade of the student.
    - subjects (list of str): The subjects the student is enrolled in.
    """
    students[name] = {'age': age, 'grade': grade, 'subjects': subjects}


def update_student(name):
    """
    Update an existing student record.
    Args:
    - name (str): The name of the student whose record is to be updated.
    """
    if name in students.keys():  # Check if the student exists
        new_age = input("Update student's age or enter empty space to skip: ")
        if new_age != " ":
            students[name]['age'] = int(new_age)

        new_grade = input("Update student's grade or enter empty space to skip: ")
        if new_grade != " ":
            students[name]['grade'] = float(new_grade)

        print("Edit student's subject/s\n"
              "1. Add subject\n"
              "2. Delete subject;\n"
              "enter empty space to skip")

        new_subject = input("Enter your choice: ")

        if new_subject != " ":
            if new_subject == '1':
                subject = input("Add new subject: ")
                students[name]['subjects'].append(subject)

            elif new_subject == '2':
                subject = input("Delete subject: ")
                students[name]['subjects'].remove(subject)

    else:
        print(f'Student {name} is not in the system, enter 2 to try again or enter another choice.')
    # Prompt the user to update fields and keep current values if fields are empty
    # Code to update the student's record


def delete_student(name):
    """
    Delete a student record based on the student's name.
    Args:
    - name (str): The name of the student to delete.
    """
    if name in students.keys():  # Check if the student exists
        del students[name]  # Code to delete the student's record
        print(f"Student {name} and all his data had been successfully deleted.")
    else:
        print(f'Student {name} is not in the system, enter 3 to try again or enter another choice.')


def search_student(name):
    """
    Search for a student by name and return their record.
    Args:
    - name (str): The name of the student to search for.
    """
    if name in students.keys():  # Check if the student exists
        age = students[name]['age']
        grade = students[name]['grade']
        subjects = students[name]['subjects']
        # Code to return the student's record
        print(f"{name} is {age} years old, studying {', '.join(subjects)} and has average grade of {grade:.2f}.")
        print(f'Student: {name}\n'
              f'Age: {age}\n'
              f'Assigned subjects: {", ".join(subjects)}\n'
              f'Average grade: {grade:.2f}')
    else:
        print(f'Student {name} is not in the system, enter 4 to try again or enter another choice.')


def list_all_students():
    """
    List all student records.
    """
    if len(students) == 0:  # Check if there are any student records
        print("There are not any students recorded yet.")
    else:
        for key, value in students.items():  # Code to list all students
            print(f'Student: {key}\n'
                  f'Age: {students[key]["age"]}\n'
                  f'Assigned subjects: {", ".join(students[key]["subjects"])}\n'
                  f'Average grade: {students[key]["grade"]:.2f}')
            print()


def main():
    """
    Main function to provide user interaction.
    """
    while True:
        print("\nStudent Management System")  # Display menu options
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Search Student")
        print("5. List All Students")
        print("6. Exit")

        choice = input("Enter your choice: ")  # Prompt user for their choice

        if choice == '1':
            name = input("Enter student's name: ")  # Prompt for student details
            age = int(input("Enter student's age: "))
            grade = float(input("Enter student's grade: "))
            subjects = input("Enter student's subjects (comma-separated): ").split(',')

            add_student(name, age, grade, subjects)  # Call the add_student function

        elif choice == '2':
            name = input("Enter student's name to update: ")  # Prompt for student name to update
            update_student(name)  # Call the update_student function

        elif choice == '3':
            name = input("Enter student's name to delete: ")  # Prompt for student name to delete
            delete_student(name)  # Call the delete_student function

        elif choice == '4':
            name = input("Enter student's name to search: ")  # Prompt for student name to search
            search_student(name)  # Call the search_student function

        elif choice == '5':
            list_all_students()  # Call the list_all_students function

        elif choice == '6':  # Exit the program

            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
