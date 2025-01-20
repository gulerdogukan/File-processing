from Model import Student


class File:
    def __init__(self, file_name):
        self.file_name = file_name

    def write_to_file(self, students_info):
        with open(self.file_name, "w", encoding='utf-8') as f:
            for std in students_info:
                student_file_format = std.get_file_format()
                f.write(f"{student_file_format}\n")
        f.close()
        print("Students information are stored in the file successfully.\n")

