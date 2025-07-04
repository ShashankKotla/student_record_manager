# 📝 Student Record Manager (CLI Version)

A simple and extensible command-line application built in Python to manage student records efficiently. It allows you to add, search, and view student records using persistent file storage.

---

## ⚙️ Features

- Add a new student record (name, age, grade)
- View all students
- Search students by name (case-insensitive)
- Automatic logging of actions (logged to `log.txt`)
- Persistent storage using `students.txt`

---

## 🚀 How to Run

Make sure you have **Python 3** installed.

```bash
python3 main.py

1. Add Student
2. View All
3. Search
4. Exit
Choose: 1
Enter name: shashank
Enter age: 25
Enter grade: A
Student added.

1. Add Student
2. View All
3. Search
4. Exit
Choose: 2
1. shashank | Age:25 | Grade: A

1. Add Student
2. View All
3. Search
4. Exit
Choose: 3
Enter name to search: shashank
1. shashank | Age:25 | Grade: A

1. Add Student
2. View All
3. Search
4. Exit
Choose: 4

