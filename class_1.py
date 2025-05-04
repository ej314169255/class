class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)
"""класс Mentor должен стать родительским классом, 
а от него нужно реализовать наследование классов Lecturer (лекторы) и Reviewer
 (эксперты, проверяющие домашние задания). Очевидно, имя, фамилия 
 и список закрепленных курсов логично реализовать на уровне родительского класса"""

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname, some_val):
        super().__init__(name, surname)
        self.some_val = some_val

class Reviewer(Mentor):
    def __init__(self, name, surname,some_val):
        super().__init__(name, surname)
        self.some_val = some_val