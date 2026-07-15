class Student:
    """Студент с именем, возрастом и оценками."""

    def __init__(self, name: str, age: int, grades: list[float]):
        self.name = name
        self.age = age
        self.grades = grades


def get_avg_grades(student):
    return sum(student.grades) / len(student.grades)


GRADE_THRESHOLD = 4.1


def get_top_students(students, threshold):
    result = []
    for student in students:
        if get_avg_grades(student) > threshold:
            result.append(student)
    return result


if __name__ == "__main__":
    student1 = Student("Анна", 20, [4.5, 5.0, 3.5])
    student2 = Student("Борис", 22, [3.0, 4.0, 4.0, 5.0])
    student3 = Student("Вера", 19, [5.0, 5.0, 4.5])

    students = [student1, student2, student3]

    for student in students:
        print(f"{student.name}: средний балл {get_avg_grades(student):.2f}")

    print("Средний балл выше", GRADE_THRESHOLD, ":")
    top_students = get_top_students(students, GRADE_THRESHOLD)
    for student in top_students:
        print(student.name)        