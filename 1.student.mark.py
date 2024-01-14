def input_nums_of_student():
    nums_of_student = int(input("Number of student: "))
    return nums_of_student

def input_nums_of_course():
    nums_of_course = int(input("Number of course: "))
    return nums_of_course

def input_student_info(my_list):
    n = input_nums_of_student()
    if n <= 0:
        print("Invalid number of student")
        return
    while n > 0:
        student_id = input("Id of student: ")
        student_name = input("Name of student: ")
        DoB = input("Date of Birth of Student: ")
        info = {"Student ID" : student_id, "Student name" : student_name, "DoB" : DoB}
        my_list.append(info)
        n = n - 1

def input_course_info(my_list):
    n = input_nums_of_course()
    if n <= 0:
        print("Invalid number of course")
        return
    while n > 0:
        course_id = input("Id of course: ")
        course_name = input("Name of course: ")
        info = {"Course ID" : course_id, "Course name" : course_name}
        my_list.append(info)
        n = n - 1
        
def student_mark(my_students_list, my_courses_list, student_marks_list):  
    for course in my_courses_list:
        print("Course: " + course["Course name"])
        for student in my_students_list:
            print("Student: " + student["Student name"], end = " ")
            mark = input("Input mark: ")
            info = {"Course" : course["Course name"], "Student" : student["Student name"], "Mark" : mark}
            student_marks_list.append(info)

def list_course(my_course_list):
    for course in my_course_list:
        print(course)


def list_student(my_student_list):
    for student in my_student_list:
        print(student)

def show_students_mark(my_mark_list, my_course_list):
    course_name = input("Input a course: ")
    for course in my_course_list:
        if course_name == course["Course name"]:
            for mark in my_mark_list:
                if course_name == mark["Course"]:
                    print(mark)
            break
    else:
        print("The course doesn't exist!")

student_list = []
course_list = []
mark_list = []

input_student_info(student_list)
print("Show student list: ")
list_student(student_list)

input_course_info(course_list)
print("Show course list")
list_course(course_list)

student_mark(student_list, course_list, mark_list)
print("Show mark for a given course")
show_students_mark(mark_list, course_list)