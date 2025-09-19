import json
import csv
import statistics
from pathlib import Path

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, student_id, name, age, grade, marks):
        super().__init__(name, age)
        self.id = student_id
        self.grade = grade
        self.marks = marks

    def get_average(self):
        return sum(self.marks.values()) / len(self.marks)

    def __str__(self):
        return f"{self.name} (Grade {self.grade}, Age {self.age}) - Avg: {self.get_average():.2f}"


class Teacher(Person):
    def __init__(self, teacher_id, name, age, subject, salary):
        super().__init__(name, age)
        self.id = teacher_id
        self.subject = subject
        self.salary = salary

    def get_details(self):
        return f"ID: {self.id}, {self.name}, Subject: {self.subject}, Salary: {self.salary}"

    def __str__(self):
        return self.get_details()

def load_students(filepath="students.json"):
    with open(filepath, "r") as f:
        data = json.load(f)
    return [Student(s["id"], s["name"], s["age"], s["grade"], s["marks"]) for s in data]


def save_students(students, filepath="students.json"):
    data = [{"id": s.id, "name": s.name, "age": s.age, "grade": s.grade, "marks": s.marks}
            for s in students]
    with open(filepath, "w") as f:
        json.dump(data, f, indent=2)


def load_teachers(filepath="teachers.csv"):
    teachers = []
    with open(filepath, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            teachers.append(
                Teacher(int(row["id"]), row["name"], 0, row["subject"], int(row["salary"]))
            )
    return teachers


def save_teachers(teachers, filepath="teachers.csv"):
    with open(filepath, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "name", "subject", "salary"])
        writer.writeheader()
        for t in teachers:
            writer.writerow({
                "id": t.id, "name": t.name, "subject": t.subject, "salary": t.salary
            })

def generate_student_teacher_report(students, teachers):
    report = []
    for s in students:
        best_subject = max(s.marks, key=s.marks.get)
        teacher = next((t for t in teachers if t.subject == best_subject), None)
        teacher_name = teacher.name if teacher else "No teacher found"
        report.append((s.name, best_subject, teacher_name))
    return report


def generate_summary(students, teachers):
    summary = {}
    # Students per grade
    grades = {}
    for s in students:
        grades[s.grade] = grades.get(s.grade, 0) + 1
    summary["students_per_grade"] = grades

    subject_scores = {}
    for s in students:
        for subj, mark in s.marks.items():
            subject_scores.setdefault(subj, []).append(mark)
    subject_avg = {subj: statistics.mean(scores) for subj, scores in subject_scores.items()}
    summary["average_marks"] = subject_avg

    summary["total_salary"] = sum(t.salary for t in teachers)

    return summary

def menu():
    students = load_students()
    teachers = load_teachers()

    while True:
        print("\n--- School Management System ---")
        print("1. View Students")
        print("2. View Teachers")
        print("3. Add Student")
        print("4. Add Teacher")
        print("5. Generate Reports")
        print("6. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            for s in students:
                print(s)
        elif choice == "2":
            for t in teachers:
                print(t.get_details())
        elif choice == "3":
            sid = max(s.id for s in students) + 1
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            grade = input("Enter grade: ")
            marks = {}
            for subj in ["Math", "Science", "English"]:
                marks[subj] = int(input(f"Enter marks for {subj}: "))
            students.append(Student(sid, name, age, grade, marks))
            save_students(students)
            print("Student added successfully!")
        elif choice == "4":
            tid = max(t.id for t in teachers) + 1
            name = input("Enter name: ")
            subject = input("Enter subject: ")
            salary = int(input("Enter salary: "))
            teachers.append(Teacher(tid, name, 0, subject, salary))
            save_teachers(teachers)
            print("Teacher added successfully!")
        elif choice == "5":
            print("\n--- Student-Teacher Report ---")
            report = generate_student_teacher_report(students, teachers)
            for r in report:
                print(f"Student: {r[0]}, Best Subject: {r[1]}, Class Teacher: {r[2]}")

            print("\n--- Summary ---")
            summary = generate_summary(students, teachers)
            print("Students per grade:", summary["students_per_grade"])
            print("Average marks:", summary["average_marks"])
            print("Total salary:", summary["total_salary"])
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    # Ensure data files exist
    if not Path("students.json").exists():
        with open("students.json", "w") as f:
            json.dump([], f)
    if not Path("teachers.csv").exists():
        with open("teachers.csv", "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "name", "subject", "salary"])
            writer.writeheader()

    menu()