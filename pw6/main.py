import os
import zipfile
import math
import pickle
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
        
        if os.path.exists("students.pkl"):
            with open("students.pkl", "rb") as f:
                students = pickle.load(f)
        if os.path.exists("courses.pkl"):
            with open("courses.pkl", "rb") as f:
                courses = pickle.load(f)
        if os.path.exists("marks.pkl"):
            with open("marks.pkl", "rb") as f:
                marks = pickle.load(f)
        print("Data loaded via pickle from students.dat")

    while True:
        output.show_menu()
        choice = __builtins__.input("Your choice: ")

        if choice == '1':
            s = Student()
            s.input()
            students.append(s)

        elif choice == '2':
            c = Course()
            c.input()
            courses.append(c)

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

        elif choice == '4':
            for s in students: print(s.list())

        elif choice == '5':
            for c in courses: print(c.list())

        elif choice == '6':
            cid = __builtins__.input("Enter Course ID to show marks: ")
            if cid in marks:
                for sid, m in marks[cid].items():
                    print(f"Student ID: {sid} | Mark: {m}")
            else:
                print("No marks found.")

        elif choice == '7':
            gpa_list = []
            for s in students:
                sid = s.get_id()
                s_marks, s_credits = [], []
                for c in courses:
                    cid = c.get_id()
                    if cid in marks and sid in marks[cid]:
                        s_marks.append(marks[cid][sid])
                        s_credits.append(c.get_credit())
                if s_marks:
                    gpa = np.sum(np.array(s_marks) * np.array(s_credits)) / np.sum(s_credits)
                    gpa_list.append((s.get_name(), round(gpa, 2)))
                else:
                    gpa_list.append((s.get_name(), 0.0))
            gpa_list.sort(key=lambda x: x[1], reverse=True)
            for name, gpa in gpa_list: print(f"Student: {name} | GPA: {gpa}")

        elif choice == '0':
            with open("students.pkl", "wb") as f:
                pickle.dump(students, f)
            with open("courses.pkl", "wb") as f:
                pickle.dump(courses, f)
            with open("marks.pkl", "wb") as f:
                pickle.dump(marks, f)

            with zipfile.ZipFile("students.dat", "w") as archive:
                for f in ["students.pkl", "courses.pkl", "marks.pkl"]:
                    if os.path.exists(f):
                        archive.write(f)
            print("Data pickled and compressed into students.dat. Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
