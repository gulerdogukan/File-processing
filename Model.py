from datetime import datetime


class Student(object):

    def __init__(self, std_id, f_name, l_name, date_of_birth, sex, country_of_birth):
        self.std_id = std_id
        self.f_name = f_name
        self.l_name = l_name
        self.date_of_birth = date_of_birth
        self.sex = sex
        self.country_of_birth = country_of_birth

    def __str__(self):
        return str(self.std_id)

    # getter methods:
    def get_id(self):
        return int(self.std_id)

    def get_fullname(self):
        full_name = "{} {}".format(self.f_name, self.l_name)
        return full_name

    def get_date_of_birth(self):
        return self.date_of_birth

    def get_birth_year(self):
        dt_of_birth = datetime.strptime(self.get_date_of_birth(), "%d-%m-%Y")
        return dt_of_birth.year

    def get_sex(self):
        if self.sex == 'Male' or self.sex == 'male' or self.sex == 'M' or self.sex == 'm':
            return "Male"
        elif self.sex == 'Female' or self.sex == 'female' or self.sex == 'F' or self.sex == 'f':
            return "Female"
        else:
            return "You have entered wrong value!!."

    def get_country_of_birth(self):
        return self.country_of_birth

    def get_file_format(self):
        file_format = f"{self.std_id},\t{self.get_fullname()},\t\t{self.date_of_birth},\t\t" \
                      f"{self.convert_to_age()},\t\t{self.get_sex()},\t\t{self.country_of_birth}"
        return file_format

    # setter methods:
    def set_f_name(self, f_name):
        self.f_name = f_name

    def set_l_name(self, l_name):
        self.l_name = l_name

    def set_sex(self, sex):
        self.sex = sex

    def set_date_of_birth(self, date_of_birth):
        self.date_of_birth = date_of_birth

    def set_country_of_birth(self, country_of_birth):
        self.country_of_birth = country_of_birth

    # This method is converting the date of birth to age:
    def convert_to_age(self, ):
        age = 0
        dt_of_birth = datetime.strptime(self.get_date_of_birth(), "%d-%m-%Y")
        age = datetime.today().year - dt_of_birth.year

        if datetime.today().month < dt_of_birth.month:
            age -= 1
            return age
        elif datetime.today().month == dt_of_birth.month:
            if datetime.today().day < dt_of_birth.day:
                age -= 1
                return age
            else:
                return age
        else:
            return age

    def display_student_information(self):
        print("\tStudent's ID:       " + str(self.get_id()))
        print("\tStudent's Name:     " + self.get_fullname())
        print("\tDate Of Birth:      " + self.get_date_of_birth())
        print("\tStudent's Age:      " + str(self.convert_to_age()))
        print("\tStudent's Gender:   " + self.get_sex())
        print("\tCountry Of Birth:   " + self.get_country_of_birth())
        return ""

