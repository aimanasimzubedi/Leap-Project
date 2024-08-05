import csv

# Dictionaries
students = {
    "00001": "Haania Ajaz",
    "00002": "Marya Ahmed",
    "00003": "Aiman Asim",
    "00004": "Alina Saqib",
    "00005": "Alishba Ahmed",
    "00006": "Shehneez Arif"
}
grades = {
    "00001": {"math": 78, "english": 78.22, "physics": 47.33},
    "00002": {"math": 98.55, "english": 75.25, "physics": 84.22},
    "00003": {"math": 75, "english": 87, "physics": 75},
    "00004": {"math": 87, "english": 78.35, "physics": 87},
    "00005": {"math": 85, "english": 78, "physics": 54},
    "00006": {"math": 87, "english": 45, "physics": 75}
}
average = {}

# Function to calculate average grades
def average_grades(student_id=None):
    if student_id is None:
        student_id = input("\nEnter Student ID: ")
    if student_id in students:
        student_grades = grades[student_id]
        valid_grades = [float_value for float_value in student_grades.values() if float_value is not None]
        if valid_grades:
            avg = sum(valid_grades) / len(valid_grades)
            avg = round(avg, 2)
            average[student_id] = avg
        else:
            average[student_id] = None
    else:
        print(f"Student ID {student_id} does not exist.\n")

# Function to record grades
def record_grade(student_id=None):
    if student_id is None:
        while True:
            display_student_list()
            student_id = input("\nEnter Student ID to change grade: ")
            if student_id in students:
                break
            else:
                print("Invalid Student ID. Please enter from the below Student IDs.")
    if student_id not in students:
        return  # This shouldn't be reached due to the loop above
    for subject in ["math", "english", "physics"]:
        while True:
            try:
                grade = input(f"\nEnter {subject} grade for student {students[student_id]} (0-100): ")
                float_value = float(grade)
                if 0 <= float_value <= 100:
                    break
                else:
                    print("Invalid value, please enter a grade between 0 and 100.\n")
            except ValueError:
                print("Invalid value, please enter a grade between 0 and 100.\n")
        grades[student_id][subject] = float_value
        print(f"Recorded {subject} grade {float_value} for student {students[student_id]}.\n")
    average_grades(student_id)

# Function to add students
def add_student(student_id=None, student_name=None):
    if student_id is None:
        while True:
            student_id = input("\nEnter student ID: ")
            if len(student_id) == 5 and student_id.isnumeric():
                if student_id not in students:
                    break
                else:
                    print(f"\nStudent ID {student_id} already exists.")
            else:
                print("\nInvalid Input. Enter Student ID again: ")
    if student_name is None:
        student_name = input("\nEnter Student Name: ")
        while not is_valid_name(student_name):
            student_name = input("Invalid Output. Enter Student Name again: ")
    students[student_id] = student_name
    grades[student_id] = {"math": None, "english": None, "physics": None}
    print(f"\nStudent {student_name} added with ID {student_id}.\n")
    record_grade(student_id)

def is_valid_name(name):
    # Checks if name contains only alphabetic characters and spaces
    return all(c.isalpha() or c.isspace() for c in name)

# Function to display student list
def display_student_list():
    print("\nAvailable Students:")
    for student_id, name in students.items():
        print(f"ID: {student_id}, Name: {name}")

# Function to display the database
def display_database():
    print(f"{'Student ID':<12}{'Student Name':<30}{'Math':<20}{'English':<20}{'Physics':<20}{'Average':<20}")
    print("-" * 120)  # A line to separate headers from the data
    for student_id, name in students.items():
        math_grade = grades[student_id]['math']
        english_grade = grades[student_id]['english']
        physics_grade = grades[student_id]['physics']
        avg_grade = average.get(student_id, "N/A")  # Default to "N/A" if average is not available
        print(f"{student_id:<12}{name:<30}{math_grade:<20}{english_grade:<20}{physics_grade:<20}{avg_grade:<20}")

# Function to export data to CSV
def export_to_csv():
    with open('students_grades.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        # Adding headers
        headers = ["Student ID", "Name", "Math", "English", "Physics", "Average"]
        writer.writerow(headers)
        
        # Adding data
        for student_id, name in students.items():
            math_grade = grades[student_id]['math']
            english_grade = grades[student_id]['english']
            physics_grade = grades[student_id]['physics']
            avg = average.get(student_id, "N/A")
            writer.writerow([student_id, name, math_grade, english_grade, physics_grade, avg])
    
    print("Data exported to students_grades.csv successfully.")

# Main menu loop
def main_menu():
    # Calculate averages for existing students
    for student_id in students:
        average_grades(student_id)

    while True:
        print("\nMenu:")
        print("1. Add a new student")
        print("2. Change the grade of an existing student")
        print("3. Display the database")
        print("4. Export data to CSV")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            add_student()
        elif choice == '2':
            record_grade()
        elif choice == '3':
            display_database()
        elif choice == '4':
            export_to_csv()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# Start the menu
main_menu()
