class Student_list:
    def __init__(self, n):
        self.__list = []
        self.__num = n
    def input_student(self):
        count = 0
        while (count < self.__num):
            id_of_student = input("Input id of student: ")
            name_of_student = input("Input name of student: ")
            date_of_birth = input("Input student's date of birth: ")
            student = Student(id_of_student, name_of_student, date_of_birth)
            self.__list.append(student)
            count = count + 1
    def list_students(self):
        for student in self.__list:
            print(student)
    def get_list(self):
        return self.__list
    def set_clone_list(self, cl_list):
        for i in range(0, len(cl_list)):
            self.__list.append(cl_list[i])  
    def get_nums_of_student(self):
        return self.__num
    def set_nums_of_student(self, n):
        self.__num = n
class Course_list:
    def __init__(self, n):
        self.__list = []
        self.__num = n
    def input_course(self, student_list):
        count = 0
        while (count < self.__num):
            id_of_course = input("Input id of course: ")
            name_of_course = input("Input name of course: ")
            course = Course(id_of_course, name_of_course, student_list)
            self.__list.append(course)
            count = count + 1
    def list_courses(self):
        for course in self.__list:
            print(course)
    def list_courses_name(self):
        for course in self.__list:
            print(course.get_name())
    def __iter__(self):
        return iter(self.__list)

class Student:
    def __init__(self, id, name, DoB):
        self.__id = id
        self.__name = name
        self.__DoB = DoB
        self.__mark = 0
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_DoB(self):
        return self.__DoB
    def set_mark(self, mark):
        self.__mark = mark
    def __str__(self):
        return f"Student ID: {self.__id}. Student name: {self.__name}. Student DoB: {self.__DoB}" 
    def show_mark(self):
        return f"Student ID: {self.__id}. Student name: {self.__name}. Mark: {self.__mark}"
    
class Course:
    def __init__(self, id, name, student_list):
        self.__id = id
        self.__name = name
        self.__student_list = self.student_list_of_course(student_list)
    def student_list_of_course(self, student_list):
        clone_list = Student_list(student_list.get_nums_of_student())
        clone_list.set_clone_list(student_list.get_list())
        return clone_list
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def __str__(self):
        return f"Course ID: {self.__id}. Course name: {self.__name}"
    def input_student_marks(self):
        n = 0
        list_student = self.__student_list.get_list()
        while n < len(self.__student_list.get_list()):
            mark = int(input("Input mark for student " + list_student[n].get_name() + ": "))
            list_student[n].set_mark(mark)
            n += 1
    def show_student_mark(self):
        for student in self.__student_list.get_list():
            print(student.show_mark())

number_of_student = int(input("Input number of student: "))
student_list = Student_list(number_of_student)
student_list.input_student()
student_list.list_students()

num_of_course = int(input("Input number of course: "))
course_list = Course_list(num_of_course)
course_list.input_course(student_list)
course_list.list_courses()

input_mark = input("Choose a course to input student mark:")
course_list.list_courses()
for course in course_list:
    if input_mark == course.get_name():
        course.input_student_marks()
        course.show_student_mark()