from Service import System, Student
from Helper import *


def main():
    introduction()
    main_system = System()
    number_chosen = 0

    while True:
        main_menu()
        number_chosen = int(input("\nEnter the number: "))
        if number_chosen == 1:
            print("\nAdding a new student...")
            new_student = add_new_student()
            main_system.add_new_student(new_student)

        elif number_chosen == 2:
            print("\nGetting a student...")
            student_id = get_std_id()
            main_system.get_student_by_id(student_id)

        elif number_chosen == 3:
            print("\nGetting a student...")
            birth_year = get_std_birth_year()
            main_system.get_students_by_birth_year(birth_year)

        elif number_chosen == 4:
            print("\nEnter the student ID that you want to modify his/her record.")
            student_id = get_std_id()
            new_value, new_value_filed = student_record_menu()
            main_system.modify_student_record(student_id, new_value_filed, new_value)

        elif number_chosen == 5:
            print("\nDeleting a student...")
            student_id = get_std_id()
            main_system.delete_student(student_id)

        elif number_chosen == 6:
            print("\nAll available students:")
            main_system.get_all_students()

        elif number_chosen == 7:
            main_system.write_students_information()

        elif number_chosen == 0:
            print("The system has been logged out.")
            exit()

        else:
            print("Invalid Operation Number!!!.")


if __name__ == "__main__":
    main()
