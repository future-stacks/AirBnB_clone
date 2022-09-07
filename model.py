import json


class Student():
    def __init__(self, name):
        self.name = name


def reload():
    try:
        with open("file.json", "r") as f:
            students = json.load(f)
    except FileNotFoundError:
        students = []

    return students


def save(students):
    with open("file.json", "w") as f:
        json.dump(students, f)


students = reload()  # recreate the list of Student objects from a file

print("Before:")
print(students)
s = "joeboy"
students.append(s)
print("\nAfter:")
print(students)

save(students)
