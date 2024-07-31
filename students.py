students={}
grades={}

def add_student(student_id=None, student_name=None):
    if student_id is None:
        student_id = int(input("Enter student ID(type -1 to quit): "))
        while student_id!=-1:
            if student_name is None:
                student_name = input("Enter student name: ")
            break

    while student_id not in students:
        students[student_id] = student_name
        grades[student_id] = []
        return f"Student {student_name} added with ID {student_id}."
    return f"Student ID {student_id} already exists."


print(add_student())
print(add_student("123","marya"))
