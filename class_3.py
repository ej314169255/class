from datetime import datetime
import time

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        l = ' '.join(str(x) for x in ['p','x'])
        return (f'Имя: {self.name}\nФамилия: {self.surname}\n'\
                f'Средняя оценка за домашние задания: {"averege_grade"}\n'\
                f'Курсы в процессе изучения: {"l"}\n'\
                f'Завершенные курсы: ' + l)

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def level(self, evaluated, course, vol):
        if course in self.courses_in_progress and course in evaluated.courses_attached:
            evaluated.grades[self.name, self.surname, course, f"{datetime.now()}"] = vol

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\n'\
                f'Средняя оценка за лекции: {"averege_grade"}')

class Reviewer(Mentor):
    def __init__(self, name, surname, cur_example_class):
        super().__init__(name, surname)
        self.cur_example_class = cur_example_class

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

    def level(self, evaluated, course, vol):
        if isinstance(evaluated, self.cur_example_class) and \
                course in self.courses_attached and \
                course in evaluated.courses_in_progress:
            evaluated.grades[self.name, self.surname, course, f"{datetime.now()}"] = vol


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.age} лет'


student = Student("Алексей", "Пирожков", "male")
print(student)
"""
print(some_student)
Имя: Ruoy
Фамилия: Eman
Средняя оценка за домашние задания: 9.9
Курсы в процессе изучения: Python, Git
Завершенные курсы: Введение в программирование
"""