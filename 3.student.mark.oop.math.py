import math
import numpy as np

class Student:
    def __init__(self):
        self._id = ""
        self._name = ""
        self._dob = ""
        
    def input(self):
        print("\n--- Input New Student ---")
        self._id = input("ID: ")
        self._name = input("Name: ")
        self._dob = input("Date of Birth (DoB): ")
        print(f"Student {self._name} added.")
        
    def list(self):
        return f"ID: {self._id} | Name: {self._name} | DoB: {self._dob}"
        
    def get_id(self):
        return self._id
        
    def get_name(self):
        return self._name


class Course:
    def __init__(self):
        self._id = ""
        self._name = ""
        self._credit = 0
        
    def input(self):
        print("\n--- Input New Course ---")
        self._id = input("Course ID: ")
        self._name = input("Course Name: ")
        self._credit = int(input("Course Credit: "))
        print(f"Course {self._name} added.")
        
    def list(self):
        return f"ID: {self._id} | Name: {self._name} | Credit: {self._credit}"

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_credit(self):
        return self._credit
        
        
class MarkManager:
    def __init__(self):
        self._students = []
        self._courses = []
        self._marks = {}   # {course_id: {student_id: mark}}

    def input_student(self):
        student = Student()
        student.input()
        self._students.append(student)

    def input_course(self):
        course = Course()
        course.input()
        self._courses.append(course)

    def list_students(self):
        print("\n--- All Students ---")
        if not self._students:
            print("No students enrolled.")
            return
        for student in self._students:
            print(student.list())

    def list_courses(self):
        print("\n--- All Courses ---")
        if not self._courses:
            print("No courses available.")
            return
        for course in self._courses:
            print(course.list())

    def input_marks(self):
        if not self._courses or not self._students:
            print("Please add students and courses first.")
            return

        self.list_courses()
        course_id = input("Enter Course ID to input marks for: ")

        if course_id not in self._marks:
            self._marks[course_id] = {}

        print(f"\n--- Input marks for course ID: {course_id} ---")
        for student in self._students:
            student_id = student.get_id()
            while True:
                try:
                    mark = float(input(f"Enter mark for {student.get_name()} ({student_id}): "))
                    mark = math.floor(mark * 10) / 10   
                    self._marks[course_id][student_id] = mark
                    break
                except ValueError:
                    print("Mark must be a number. Try again.")

    def list_marks(self):
        if not self._marks:
            print("No marks recorded.")
            return

        self.list_courses()
        course_id = input("Enter Course ID to show marks for: ")

        if course_id in self._marks:
            print(f"\n--- Marks for Course ID: {course_id} ---")
            course_marks = self._marks[course_id]

            for student in self._students:
                student_id = student.get_id()
                mark = course_marks.get(student_id, 'N/A')
                print(f"Student: {student.get_name()} | Mark: {mark}")
        else:
            print(f"Course ID {course_id} not found.")

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
        print("\n--- Students Sorted by GPA (Descending) ---")

        gpa_list = []
        for student in self._students:
            sid = student.get_id()
            name = student.get_name()
            gpa = self.calculate_gpa(sid)
            gpa_list.append((name, sid, gpa))

        sorted_list = sorted(gpa_list, key=lambda x: x[2], reverse=True)

        for name, sid, gpa in sorted_list:
            print(f"Student: {name} | ID: {sid} | GPA: {gpa}")


if __name__ == "__main__":
    manager = MarkManager()

    while True:
        print("\n===== OOP Student Mark Manager (Labwork 3) =====")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Input Student Marks")
        print("4. List Students")
        print("5. List Courses")
        print("6. Show Marks for a Course")
        print("7. Show Students Sorted by GPA")
        print("0. Exit")

        choice = input("Your choice: ")

        if choice == '1':
            manager.input_student()
        elif choice == '2':
            manager.input_course()
        elif choice == '3':
            manager.input_marks()
        elif choice == '4':
            manager.list_students()
        elif choice == '5':
            manager.list_courses()
        elif choice == '6':
            manager.list_marks()
        elif choice == '7':
            manager.list_gpa_sorted()
        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

