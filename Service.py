from Model import Student
from Helper import modify_field
from Files import File


class System:
    def __init__(self, input_file=None):
        self.students = []
        self.input_file = "Students_info.txt"
        self.file = File(self.input_file)

    def add_new_student(self, student):
        if len(self.students) >= 100:
            print("Sorry, students array is full, you can't add more students.")
        else:
            self.students.append(student)
            print("Student added successfully.\n")

    def get_student_by_id(self, std_id):
        is_exist = -1
        for i in range(0, len(self.students)):
            if self.students[i].get_id() == std_id:
                print("The information of the student with ID = " + str(std_id) + " is: ")
                print(self.students[i].display_student_information())
                is_exist = i
        if is_exist == -1:
            print("Student with ID = " + str(std_id) + " doesn't exist!!")
        return is_exist

    def display_students_information(self, students=None):
        print("\n# Students Information:")
        if students:
            for student in students:
                print(student.display_student_information())
                print("><><><><><><><><><><><><><><><><><><")
        else:
            for student in self.students:
                print(student.display_student_information())
                print("><><><><><><><><><><><><><><><><><><")

    def get_students_by_birth_year(self, birth_year):
        student_by_birth_year = []
        for student in self.students:
            if int(student.get_birth_year()) == int(birth_year):
                student_by_birth_year.append(student)
        self.display_students_information(student_by_birth_year)
        return student_by_birth_year

    def modify_student_record(self, std_id, new_value_field, new_value):
        student = self.get_student_by_id(std_id)
        if student == -1:
            return -1
        field_chosen = f"set_{new_value_field}"
        var = getattr(self.students[student], field_chosen)
        var(new_value)

    def delete_student(self, std_id):
        is_student_exist = self.get_student_by_id(std_id)
        if is_student_exist == -1:
            print("Student with ID = " + str(std_id) + " doesn't exist!!")
        self.students.pop(is_student_exist)
        print("Student with ID = " + str(std_id) + " is deleted successfully: \n")

    def get_all_students(self):
        self.display_students_information()

    def write_students_information(self):
        if self.input_file is None:
            print("No input file provided")
        else:
            self.file.write_to_file(self.students)
