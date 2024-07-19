import os

class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade
    
    def display_student(self):
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grade: {self.grade}")
        print("--------------------")
    
    def update_student(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

def write_to_file(student):
    try:
        with open("student_records.txt", "a") as file:
            file.write(f"{student.student_id},{student.name},{student.age},{student.grade}\n")
    except Exception as e:
        print(f"an error occurred : {e}")

def read_from_file():
    students = []
    if os.path.exists("student_records.txt"):
        try:
            with open("student_records.txt", "r") as file:
                for line in file:
                    student_id, name, age, grade = line.strip().split(",")
                    student = Student(int(student_id), name, int(age), float(grade))
                    students.append(student)
        except Exception as e:
            print(f"an error occurred: {e}")
    else:
        print("file not found.")
    return students

def update_a_record(student_id, new_name, new_age, new_grade):
    students = read_from_file()
    flag = False
    for student in students:
        if student.student_id == student_id:
            student.update_student(new_name, new_age, new_grade)
            flag = True
            break
    if flag:
        try:
            with open("student_records.txt", "w") as file:
                for student in students:
                    file.write(f"{student.student_id},{student.name},{student.age},{student.grade}\n")
            print(f"Student with ID {student_id} updated.")
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print(f"Student with ID {student_id} not found.")

def display_all_records():
    students = read_from_file()
    if students:
        for student in students:
            student.display_student()
    else:
        print("record not found.")

def main():
    while True:
        print("Menu:")
        print("1. Add a new student record")
        print("2. Update an existing student record")
        print("3. Display all student records")
        print("4. Exit")
        choice = input("Enter choice: ")
        
        if choice == "1":
            
            student_id = int(input("Enter student ID: "))
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            grade = float(input("Enter student grade: "))
            new_student = Student(student_id, name, age, grade)
            write_to_file(new_student)
               
        
        elif choice == "2":

            
            student_id = int(input("Enter student ID to update: "))
            name = input("Enter new name: ")
            age = int(input("Enter student age: "))
            grade = float(input("Enter new grade (float value): "))
            update_a_record(student_id, name, age, grade)
          
        
        elif choice == "3":
            display_all_records()
        
        elif choice == "4":
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
