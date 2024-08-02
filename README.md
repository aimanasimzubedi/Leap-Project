students = {"3": "haania"}
grades = {"3": {"math": 34, "english": 98, "physics": None}}

#function to record grades
def record_grade(student_id=None):
    if student_id is None:
        student_id = input("Enter student ID: ")
    if student_id not in students:
        print(f"Student ID {student_id} does not exist.")
        return
    for subject in ["math", "english", "physics"]:
        grade = float(input(f"Enter {subject} grade for student {students[student_id]}: "))
        grades[student_id][subject] = grade
        print(f"Recorded {subject} grade {grade} for student {students[student_id]}.")
 
#function to calculate average grades
def average_grades(student_id=None):
    if student_id is None:
        student_id = input("Enter student ID: ")
    if student_id in students:
        student_grades = grades[student_id]
        if all(grade is not None for grade in student_grades.values()):
            avg = sum(student_grades.values()) / len(student_grades)
            return f"Average grade for student ID {student_id} is {avg:.2f}."
        return f"Some grades are missing for student ID {student_id}."
    return f"Student ID {student_id} does not exist."

    
    for subject in ["math", "english", "physics"]:
        grade = float(input(f"Enter {subject} grade for student {students[student_id]}: "))
        grades[student_id][subject] = grade
        print(f"Recorded {subject} grade {grade} for student {students[student_id]}.")

def add_student(student_id=None, student_name=None):
    if student_id is None:
        student_id = input("Enter student ID: ")
        if student_id in students:
            print(f"Student ID {student_id} already exists.")
            return
    if student_name is None:
        student_name = input("Enter student name: ")
        students[student_id] = student_name
        grades[student_id] = {"math": None, "english": None, "physics": None}
        print(f"Student {student_name} added with ID {student_id}.")
        record_grade(student_id)
        average_grades(student_id)
    else:
        students[student_id] = student_name
        grades[student_id] = {"math": None, "english": None, "physics": None}
        print(f"Student {student_name} added with ID {student_id}.")


# Loop to add students
while True:
    add_student()
    continue_adding = input("Do you want to add another student? (yes/no): ")
    if continue_adding != 'yes':
        break

print("Student list:", students)


# Loop to record grades
while True:
    record_grade()
    continue_recording = input("Do you want to record another grade? (yes/no): ")
    if continue_recording != 'yes':
        break
print("Grades list:", grades)


# loop for average grades
while True:
    average_grades()
    continue_average = input("Do you want to calculate another average? (yes/no): ")
    if continue_recording != 'yes':
        break

for student_id, name in students.items():
    math_grade = grades[student_id]['math']
    english_grade = grades[student_id]['english']
    physics_grade = grades[student_id]['physics']
    print (student_id ,name, math_grade, english_grade, physics_grade)


