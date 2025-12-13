import math
import numpy as np
from domains.student import Student
from domains.course import Course

class MarkManager:
    def __init__(self):
        self._students = []
        self._courses = []
        self._marks = {}

    def input_student(self):
        student = Student()
        student.input()
        self._students.append(student)

    def input_course(self):
        course = Course()
        course.input()
        self._courses.append(course)

    def input_marks(self):
        if not self._courses or not self._students:
            print("Please add students and courses first.")
            return

        for course in self._courses:
            print(course.list())
        course_id = input("Enter Course ID to input marks for: ")

        if course_id not in self._marks:
            self._marks[course_id] = {}

        for student in self._students:
            student_id = student.get_id()
            try:
                mark = float(input(f"Enter mark for {student.get_name()} ({student_id}): "))
                mark = math.floor(mark * 10) / 10
                self._marks[course_id][student_id] = mark
            except ValueError:
                print("Invalid mark.")

    def calculate_gpa(self, student_id):
        credits = []
        weighted_marks = []

        for course in self._courses:
            cid = course.get_id()
            credit = course.get_credit()
            mark = self._marks.get(cid, {}).get(student_id)

            if mark is not None:
                credits.append(credit)
                weighted_marks.append(mark * credit)

        if not credits:
            return 0

        return round(np.sum(weighted_marks) / np.sum(credits), 2)

    def list_gpa_sorted(self):
        gpa_list = []
        for student in self._students:
            sid = student.get_id()
            name = student.get_name()
            gpa = self.calculate_gpa(sid)
            gpa_list.append((name, sid, gpa))

        sorted_list = sorted(gpa_list, key=lambda x: x[2], reverse=True)

        for name, sid, gpa in sorted_list:
            print(f"Student: {name} | ID: {sid} | GPA: {gpa}")

    def list_students(self):
        for student in self._students:
            print(student.list())

    def list_courses(self):
        for course in self._courses:
            print(course.list())

    def list_marks(self):
        course_id = input("Enter Course ID to show marks for: ")
        if course_id in self._marks:
            for student in self._students:
                sid = student.get_id()
                mark = self._marks[course_id].get(sid, 'N/A')
                print(f"{student.get_name()} | Mark: {mark}")
        else:
            print("Course not found.")

