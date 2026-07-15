class Student:
    """Студент с именем, возрастом и оценками."""

    def __init__(self, name: str, age: int, grades: list[float]):
        self.name = name
        self.age = age
        self.grades = grades


def get_avg_grades(student):
    return sum(student.grades) / len(student.grades)


if __name__ == "__main__":
    student1 = Student("Анна", 20, [4.5, 5.0, 3.5])
    student2 = Student("Борис", 22, [3.0, 4.0, 4.0, 5.0])
    student3 = Student("Вера", 19, [5.0, 5.0, 4.5])

    for student in (student1, student2, student3):
        print(f"{student.name}: средний балл {get_avg_grades(student):.2f}")