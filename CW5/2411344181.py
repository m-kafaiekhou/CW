import re
from uuid import uuid4

class User:
    users = {}

    def __init__(self, nat_id, name, lname, phone, email, passw, age, address):
        self.nat_id = str(nat_id)
        self.name = name
        self.lname = lname
        self.phone = phone
        self.email = self.validate_email(email)
        self.passw = self.validate_passw(passw)
        self.age = age
        self.address = address
        self.__class__.users[self.nat_id] = self

    @staticmethod
    def validate_passw(passw):
        passw = str(passw)
        if len(passw) < 8:
            raise ValueError("pass must be at least 8 chars")
        if not re.search("[a-z]", passw):
            raise ValueError("pass must contain lower case letters")
        if not re.search("[A-Z]", passw):
            raise ValueError("pass must contain upper case letters")
        if not re.search("[0-9]", passw):
            raise ValueError("pass must contain digits")

        return passw

    @staticmethod
    def validate_email(email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

        if re.fullmatch(regex, email):
            return email
        else:
            raise ValueError("Invalid email")

    @classmethod
    def change_pass(cls, nat_id, old_pass, new_pass):
        nat_id = str(nat_id)

        if nat_id not in cls.users:
            raise ValueError("id not found")
        if cls.users[nat_id].passw == old_pass:
            cls.users[nat_id].passw = cls.validate_passw(new_pass)
            print("password has been changed successfuly")
        else:
            raise ValueError("Old password is not valid")

    def __str__(self) -> str:
        return self.nat_id


class Staff(User):
    staffs = {}

    def __init__(self, work_place_name, income, department, nat_id, name, lname, phone, email, passw, age, address):
        super().__init__(nat_id, name, lname, phone, email, passw, age, address)
        self.work_place_name = self.validate_staff(work_place_name)
        self.income = self.net_income(income)
        self.department = department
        self.__class__.staffs[self.nat_id] = self

    @staticmethod
    def net_income(income):
        print(income)
        if income > 50000000:
            return income - (income - 50000000) * 0.16
        else:
            return income * 0.93

    @staticmethod
    def validate_staff(work_place):
        if isinstance(work_place, list):
            if len(work_place) == 1:
                return work_place
            else:
                raise ValueError("Each employee can work in one place only!!")
        else:
            ValueError("Work place must be a list!!")


class Student:
    pass


class Teacher(Staff):
    degrees = {"Instructor": 1.2, "Assistance": 1.8, "Associate": 2.5, "Professor": 3}

    def __init__(self, all_course_list, current_courses, degree, work_place_name, income, department, nat_id, name, lname, phone, email, passw, age, address):
        super().__init__(work_place_name, income, department, nat_id,  name, lname, phone, email, passw, age, address)
        self.degree = degree
        self.income = self.rais(degree, income)
        self.all_course_list = all_course_list
        self.current_courses = current_courses

    def add_course(self, new_course):
        if isinstance(new_course, str):
            new_course = [new_course]
            self.current_courses.append(new_course)
        else:
            self.current_courses += list(new_course)

    @staticmethod
    def validate_degree(degree) -> any:
        if degree in __class__.degrees:
            return degree
        else:
            raise ValueError("Wrong degree input (EX: {Instructor, Assistance, Associate, Professor})!!")

    @staticmethod
    def rais(degree, income) -> any:
        return __class__.degrees[degree] * income


class Course:
    def __init__(self, name, teachers_list, teacher_name):
        self.name = name
        self.course_id = uuid4()
        self.teachers_list = teachers_list
        self.teacher_name = self.validate_teacher(teachers_list, teacher_name)

    @staticmethod
    def validate_teacher(teachers_list, teacher_name):
        if teacher_name in teachers_list:
            return teacher_name
        else:
            raise ValueError("teacher name must be in teacher list !!")


cource_list = ["M1", "M2", "M3","M4","M5","M6","M7"]
u = User(12, 23, 3, 3, "salam@gmail.com", "As8@._djde", 10, 232)
stff1 = Staff("u1", 100000000, ["u2"], 12, 23, 3, 3, "salam@gmail.com", "As8@._djde", 10, 232)
tch1 = Teacher(cource_list,cource_list[:2], "Assistance","u1", 100000000, ["u2"], 12, 23, 3, 3, "salam@gmail.com", "As8@._djde", 10, 232)
print(stff1.__dict__)
print(tch1.__dict__)
u.change_pass(12, "As8@._djde", "As50@._djde")
print(u.passw)
