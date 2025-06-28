from file_handler import write_record, read_all_records
from datetime import datetime

class Student:
    def __init__(self, name: str, age: int, grade: str):
        self.name = name
        self.age = age
        self.grade = grade
    
    def to_string(self):
        return f"{self.name},{self.age},{self.grade}"
    
    def display(self, index=None):
        prefix = f"{index}. "if index else ""
        return f"{prefix}{self.name} | Age:{self.age} | Grade: {self.grade}"
    
def log_action(func):
    def wrapper(*args, **kwargs):
        action = func.__name__.replace("_", " ").title()
        with open("log.txt", "a") as log:
            log.write(f"{datetime.now()} - {action} performed\n")
        return func(*args, **kwargs)
    return wrapper

@log_action
def add_student():
    try:
        name = input("Enter name: ").strip()
        age = int(input("Enter age: ").strip()) #might raise ValueError
        grade = input("Enter grade: ").strip()
        # record = f"{name}, {age}, {grade}"
        # write_record(record)

        student = Student(name, age, grade)
        write_record(student.to_string())
        print("Student added.")

    except ValueError:
        print("Age must be a number.")

@log_action
def view_students():
    records = read_all_records()
    if not records:
        print("No records found")
    else:
        for i, record in enumerate(records, 1):
            name, age, grade = record.strip().split(",")
            # print(f"{i}. {name} | Age: {age} | Grade: {grade}")
            student = Student(name, age, grade)
            print(f"{student.display(i)}")

@log_action
def search_student():
    keyword = input("Enter name to search: ").strip().lower()
    records = read_all_records()

    found = False
    for i, record in enumerate(records, 1):
        name, age, grade = record.strip().split(",")
        if keyword in name.lower():
            student = Student(name, age, grade)
            print(student.display(i))
            found = True
    if not found:
        print("No matching student found")




def main():
    while True:
        print("\n1. Add Student\n2. View All\n3. Search\n4. Exit")
        choice = input("Choose: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            break
        else:
            print("Invalid choice")

if __name__ == '__main__':
    main()

