students = {"3":"haania"}
grades = {"3":[34,98]}

def add_student(student_id=None, student_name=None):
    if student_id is None:
        student_id = input("Enter student ID: ")
        if student_id in students:
            print(f"Student ID {student_id} already exists.")
            return
    if student_name is None:
        student_name = input("Enter student name: ")
        students[student_id] = student_name
        grades[student_id] = []
        print(f"Student {student_name} added with ID {student_id}.")
    else:
        students[student_id] = student_name
        grades[student_id] = []
        print(f"Student {student_name} added with ID {student_id}.")

#test data
# print(add_student("3", "haania"))

#to loop add students function
while True:
    add_student()
    continue_adding = input("Do you want to add another student? (yes/no): ")
    if continue_adding != 'yes':
        break

#output
print("Student list:", students)

# Function to record grades for a student
def record_grade(student_id=None, grade=None):
    if student_id is None:
        student_id = input("Enter student ID: ")
    if student_id not in students:
        print(f"Student ID {student_id} does not exist.")
        return
    
    if grade is None:
        grade = float(input(f"Enter grade for student {students[student_id]}: "))

    grades[student_id].append(grade)
    print(f"Recorded grade {grade} for student {students[student_id]}.")
          
#to loop record grades function
while True:
    record_grade()
    continue_recording = input("Do you want to record another grade? (yes/no): ").strip().lower()
    if continue_recording != 'yes':
        break
        
#output
print("Grades list:", grades)
