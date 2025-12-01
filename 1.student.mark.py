students = []
courses = []
marks = {}

def input_student_info():
    print("\n--- Input New Student ---")
    student_id = input("ID: ")
    name = input("Name: ")
    dob = input("Date of Birth (DoB): ")
    
    students.append({
        'id': student_id,
        'name': name,
        'dob': dob
    })
    print(f"Student {name} added.")

def input_course_info():
    print("\n--- Input New Course ---")
    course_id = input("Course ID: ")
    name = input("Course Name: ")
    
    courses.append({
        'id': course_id,
        'name': name
    })
    print(f"Course {name} added.")

def input_student_marks():
    if not courses or not students:
        print("Please add students and courses first.")
        return
        
    list_courses()
    course_id = input("Enter Course ID to input marks for: ")
    
    if course_id not in marks:
        marks[course_id] = {}
        
    print(f"\n--- Input marks for course ID: {course_id} ---")
    
    for student in students:
        while True:
            try:
                mark = float(input(f"Enter mark for {student['name']} ({student['id']}): "))
                marks[course_id][student['id']] = mark
                break
            except ValueError:
                print("Mark must be a number. Try again.")

def list_courses():
    print("\n--- All Courses ---")
    if not courses:
        print("No courses available.")
        return
    for course in courses:
        print(f"ID: {course['id']} | Name: {course['name']}")

def list_students():
    print("\n--- All Students ---")
    if not students:
        print("No students enrolled.")
        return
    for student in students:
        info_tuple = (student['id'], student['name'], student['dob'])
        print(f"ID: {info_tuple[0]} | Name: {info_tuple[1]} | DoB: {info_tuple[2]}")

def show_student_marks():
    if not marks:
        print("No marks recorded.")
        return
    
    list_courses()
    course_id = input("Enter Course ID to show marks for: ")
    
    if course_id in marks:
        print(f"\n--- Marks for Course ID: {course_id} ---")
        course_marks = marks[course_id]
        
        for student in students:
            student_id = student['id']
            mark = course_marks.get(student_id, 'N/A')
            print(f"Student: {student['name']} | Mark: {mark}")
    else:
        print(f"Course ID {course_id} not found.")

if __name__ == "__main__":
    while True:
        print("\n===== Student Mark Manager =====")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Input Student Marks")
        print("4. List Students")
        print("5. List Courses")
        print("6. Show Marks for a Course")
        print("0. Exit")
        
        choice = input("Your choice: ")
        
        if choice == '1':
            input_student_info()
        elif choice == '2':
            input_course_info()
        elif choice == '3':
            input_student_marks()
        elif choice == '4':
            list_students()
        elif choice == '5':
            list_courses()
        elif choice == '6':
            show_student_marks()
        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
