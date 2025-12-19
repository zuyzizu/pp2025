import math
import numpy as np
import os
import zipfile
from domains.student import Student
from domains.course import Course

class MarkManager:
    def __init__(self):
        self._students = []
        self._courses = []
        self._marks = {}
        self.load_data()

    def input_student(self):
        student = Student()
        student.input()
        self._students.append(student)
        self.write_students_to_file()

    def input_course(self):
        course = Course()
        course.input()
        self._courses.append(course)
        self.write_courses_to_file()

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
        self.write_marks_to_file()

    def write_students_to_file(self):
        with open("students.txt", "w") as f:
            for s in self._students:
                f.write(f"{s.get_id()},{s.get_name()},{s.get_dob()}\n")

    def write_courses_to_file(self):
        with open("courses.txt", "w") as f:
            for c in self._courses:
                f.write(f"{c.get_id()},{c.get_name()},{c.get_credit()}\n")

    def write_marks_to_file(self):
        with open("marks.txt", "w") as f:
            for cid, s_marks in self._marks.items():
                for sid, mark in s_marks.items():
                    f.write(f"{cid},{sid},{mark}\n")

    def compress_data(self):
        self.write_students_to_file()
        self.write_courses_to_file()
        self.write_marks_to_file()
        with zipfile.ZipFile("students.dat", "w") as archive:
            if os.path.exists("students.txt"): archive.write("students.txt")
            if os.path.exists("courses.txt"): archive.write("courses.txt")
            if os.path.exists("marks.txt"): archive.write("marks.txt")
        print("\nData archived to students.dat")

    def load_data(self):
        if os.path.exists("students.dat"):
            with zipfile.ZipFile("students.dat", "r") as archive:
                archive.extractall()

        if os.path.exists("students.txt"):
            with open("students.txt", "r") as f:
                for line in f:
                    sid, name, dob = line.strip().split(',')
                    s = Student()
                    s._id, s._name, s._dob = sid, name, dob
                    self._students.append(s)

        if os.path.exists("courses.txt"):
            with open("courses.txt", "r") as f:
                for line in f:
                    cid, name, credit = line.strip().split(',')
                    c = Course()
                    c._id, c._name, c._credit = cid, name, int(credit)
                    self._courses.append(c)

        if os.path.exists("marks.txt"):
            with open("marks.txt", "r") as f:
                for line in f:
                    cid, sid, mark = line.strip().split(',')
                    if cid not in self._marks:
                        self._marks[cid] = {}
                    self._marks[cid][sid] = float(mark)

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
