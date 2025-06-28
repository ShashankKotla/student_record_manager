import os

FILE_NAME = "students.txt"

def write_record(data: str):
    with open(FILE_NAME, "a") as f:
        f.write(data + "\n")

def read_all_records():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as f:
        return f.readlines()
