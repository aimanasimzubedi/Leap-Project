#Dictionaries
students = {"00003": "haania"}
grades = {"00003": {"math": None, "english": None, "physics": None}}
average = {}

#function to calculate average grades
def average_grades(student_id=None):
    if student_id is None:
        student_id = input("Enter student ID: ")
    if student_id in students:
        student_grades = grades[student_id]
        valid_grades = [float_value for float_value in student_grades.values() if float_value is not None]
        if valid_grades:
            avg = sum(valid_grades) / len(valid_grades)
            avg = round(avg, 2)
            average[student_id] = avg
            print(f"Average grade for student ID {student_id} is {avg}.")
            if len(valid_grades) < len(student_grades):
                print(f"Some grades are missing for student ID {student_id}.")
        else:
            print(f"No grades available for student ID {student_id}.")
    else:
        print(f"Student ID {student_id} does not exist.")


#Function to record grades
def record_grade(student_id=None):
    if student_id is None:
        student_id = input("Enter student ID: ")
    if student_id not in students:
        print(f"Student ID {student_id} does not exist.")
        return
    for subject in ["math", "english", "physics"]:
        while True:
            try:
                grade = (input(f"Enter {subject} grade for student {students[student_id]} (0-100): "))
                float_value= float(grade)
                if (0 <= float_value <= 100):
                    break
                else:
                    print("Invalid value, please enter a grade between 0 and 100.")
            except:
                print("Invalid value, please enter a grade between 0 and 100.")
        grades[student_id][subject] = float_value
        print(f"Recorded {subject} grade {float_value} for student {students[student_id]}.")
    average_grades(student_id)


#Function to keep recording/changing grades
def continue_recording():
    while True:
        continue_recording = input("Do you want to add/change an existing grade? (yes/no): ")
        while continue_recording != 'yes' and continue_recording != 'no':
            continue_recording = input("Invalid input. Do you want to add/change an existing grade? (yes/no): ")
        if continue_recording == 'no':
            break
        record_grade()


#Function to add students
def add_student(student_id=None, student_name=None):
    if student_id is None:
        student_id = input("Enter student ID: ")
        while len(student_id)!=5 or student_id.isnumeric() == False:
            student_id=input("Enter Student ID again: ")
        if student_id in students:
            print(f"Student ID {student_id} already exists.")
            return
    if student_name is None:
        student_name = input("Enter student name: ")
        while not is_valid_name(student_name):
            student_name = input("Invalid Output. Enter student name again: ")
    students[student_id] = student_name
    grades[student_id] = {"math": None, "english": None, "physics": None}
    print(f"Student {student_name} added with ID {student_id}.")
    record_grade(student_id)
    continue_recording()
    
def is_valid_name(name):
    # Checks if name contains only alphabetic characters and spaces
    return all(c.isalpha() or c.isspace() for c in name)

#Loop to keep adding students
while True:
    add_student()
    continue_adding = input("Do you want to add another student? (yes/no): ")
    while continue_adding != 'yes' and continue_adding != 'no':
        continue_adding = input("Invalid input. Do you want to add another student? (yes/no): ")
    if continue_adding == 'no':
        break


#For printing the database
print("Student list:", students)
print("Grades list:", grades)

for student_id, name in students.items():
    math_grade = grades[student_id]['math']
    english_grade = grades[student_id]['english']
    physics_grade = grades[student_id]['physics']
    print(
        "ID: ", student_id, "  ", 
        "Name: ", name, "  ",
        "Math: ", math_grade, "  ",
        "English: ", english_grade, "  ",
        "Physics: ", physics_grade, "  ",
        "Average: ", average.get(student_id, "N/A"), "  "
    )
