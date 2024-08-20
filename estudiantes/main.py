class Student:

    def __init__(self, name: str, age: int, grades: list[float]):
        self.name: str = name
        self.age: int = age
        self.grades: list[float] = grades

    def add_grade(self, grade: float):
        self.grades.append(grade)

    def average_grade(self, grades) -> float:
        return sum(self.grades) / len(grades)


estudiantes_info: list[dict] = [
    {"name": "Tomás", "age": 18, "grades": [5.0, 3.5]},
    {"name": "José", "age": 17, "grades": [4.0, 4.5]},
    {"name": "Fernando", "age": 38, "grades": [3.0, 2.5]}
]

estudiantes = [Student(datos_estudiantes["name"], datos_estudiantes["age"], datos_estudiantes["grades"]) for
               datos_estudiantes in estudiantes_info]

estudiantes_filtrados = [estudiante for estudiante in estudiantes if estudiante.average_grade() > 3]
