import datetime


# Parent Class
class Person:
    name = ""
    school = "Palomena High School"
    district = "Orange County School District"
    grade = 0
    gpa = 0
    employee_id = 0
    hire_date = 0
    pay_rate = 0

    def get_student_info(self):
        msg = "\n{} is a student at {} in the {}. {} is in the {}th grade with a GPA of {}.".format(
            self.name,
            self.school,
            self.district,
            self.name,
            self.grade,
            self.gpa,
        )
        return msg

    def get_employee_info(self):
        msg = "\n{} is an employee at {} in the {}. {} was hired on {} and currently makes {}/hour.".format(
            self.name,
            self.school,
            self.district,
            self.name,
            self.hire_date,
            self.pay_rate,
        )
        return msg


# Child class
class Student(Person):
    name = "Alex Smith"
    grade = 10
    gpa = 3.55


# Child Class
class Employee(Person):
    name = "Edgar Warez"
    employee_id = ""
    hire_date = datetime.date(2015, 8, 11)
    pay_rate = 19


if __name__ == "__main__":
    stud = Student()
    print(stud.get_student_info())

    emp = Employee()
    print(emp.get_employee_info())
