from Model import Student


def add_new_student():
    std_id = input("Enter Student's ID: ")
    f_name = input("Enter Student's first name: ")
    l_name = input("Enter Student's last name: ")
    date_of_birth = input("Enter Student's date of birth in the form of (dd-mm-yyyy): ")
    sex = input("Enter Student's gender: ")
    country_of_birth = input("Enter Student's country of birth: ")
    new_student = Student(std_id, f_name, l_name, date_of_birth, sex, country_of_birth)
    return new_student


def get_std_id():
    student_id = int(input("Enter student ID: "))
    return student_id


def get_std_birth_year():
    birth_year = int(input("Enter the birth year: "))
    return birth_year


modify_field_name = ["First Name", "Last Name", "Date Of Birth", "Gender", "Country Of Birth"]
modify_field = ["f_name", "l_name", "date_of_birth", "sex", "country_of_birth"]


def get_new_value(field_chosen):
    new_value = input(f"Enter the new value for {modify_field_name[field_chosen - 1]}: ")
    return new_value


def student_record_menu():
    print("\n# Enter the number of the field you want to modify: ")
    for i in range(0, len(modify_field_name)):
        print(f"{i + 1}. {modify_field_name[i]}")
    field_chosen = int(input("Enter the number: "))
    new_value_field = modify_field[field_chosen - 1]
    new_value = get_new_value(field_chosen)
    return new_value, new_value_field


def introduction():
    print("\t\t\t\t\t\t ## Welcome to Students Information System ##")
    print("\nDescription about the program:")
    print("\t\tThis program will keep information about students, such as:"
          "\n\t\tStudent Number, Name, Date of birth, Gender, and Country of birth.")


def main_menu():
    print("\nEnter The number of the instruction you want to operate.")
    print("1. Add New Student.")
    print("2. Find Student by ID.")
    print("3. Find Student(s) by Birth Year.")
    print("4. Modify Student's Record by ID.")
    print("5. Delete Student by ID.")
    print("6. Display All Students.")
    print("7. Write All students Information to an External Text File.")
    print("0. Quit.")
