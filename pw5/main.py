import os
import zipfile
import math
import numpy as np
import output
import input as input_mod
from domains.student import Student
from domains.course import Course

def main():
    students = []
    courses = []
    marks = {}

    if os.path.exists("students.dat"):
        with zipfile.ZipFile("students.dat", "r") as archive:
            archive.extractall()
        print("Data decompressed from students.dat")

    while True:
        output.show_menu()
        choice = __builtins__.input("Your choice: ")

        if choice == '1':
            s = Student()
            s.input()
            students.append(s)
            with open("students.txt", "a") as f:
                f.write(f"{s.get_id()},{s.get_name()}\n")

        elif choice == '2':
            c = Course()
            c.input()
            courses.append(c)
            with open("courses.txt", "a") as f:
                f.write(f"{c.get_id()},{c.get_name()}\n")

        elif choice == '3':
            if not courses or not students:
                print("Add students and courses first.")
            else:
                for c in courses:
                    print(c.list())
                cid = __builtins__.input("Enter Course ID: ")
                if cid not in marks:
                    marks[cid] = {}
                for s in students:
                    m = float(__builtins__.input(f"Mark for {s.get_name()}: "))
                    m = math.floor(m * 10) / 10
                    marks[cid][s.get_id()] = m
                with open("marks.txt", "w") as f:
                    for c_id, s_marks in marks.items():
                        for s_id, mark in s_marks.items():
                            f.write(f"{c_id},{s_id},{mark}\n")

        elif choice == '4':
            print("\n--- Student List ---")
            for s in students: print(s.list())

        elif choice == '5':
            print("\n--- Course List ---")
            for c in courses: print(c.list())

        elif choice == '6':
            cid = __builtins__.input("Enter Course ID to show marks: ")
            if cid in marks:
                print(f"\n--- Marks for Course {cid} ---")
                for sid, m in marks[cid].items():
                    print(f"Student ID: {sid} | Mark: {m}")
            else:
                print("No marks found for this course.")

        elif choice == '7':
            gpa_list = []
            for s in students:
                sid = s.get_id()
                student_marks = []
                course_credits = []
                for c in courses:
                    cid = c.get_id()
                    if cid in marks and sid in marks[cid]:
                        student_marks.append(marks[cid][sid])
                        course_credits.append(c.get_credit())
                
                if student_marks:
                    marks_arr = np.array(student_marks)
                    credits_arr = np.array(course_credits)
                    gpa = np.sum(marks_arr * credits_arr) / np.sum(credits_arr)
                    gpa_list.append((s.get_name(), round(gpa, 2)))
                else:
                    gpa_list.append((s.get_name(), 0.0))
            
            gpa_list.sort(key=lambda x: x[1], reverse=True)
            print("\n--- GPA Ranking (Descending) ---")
            for name, gpa in gpa_list:
                print(f"Student: {name} | GPA: {gpa}")

        elif choice == '0':
            with zipfile.ZipFile("students.dat", "w") as archive:
                for filename in ["students.txt", "courses.txt", "marks.txt"]:
                    if os.path.exists(filename):
                        archive.write(filename)
            print("All files compressed into students.dat. Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
