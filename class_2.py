from datetime import datetime

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

    def level(self, course, vol):
        if course in self.courses_in_progress:
            return {take_grades(self.name, self.surname, course): vol}
        else:
            return {take_grades(self.name, self.surname,course): 'уточните запрос'}

"""выставлять студентам оценки за домашние задания. 
   Теперь это могут делать только Reviewer (реализуйте такой метод)!
   А что могут делать лекторы? Получать оценки за лекции от студентов :)
   Реализуйте метод выставления оценок лекторам у класса Student
   (оценки по 10-балльной шкале, хранятся в атрибуте-словаре у Lecturer,
   в котором ключи – названия курсов, а значения – списки оценок).
   Лектор при этом должен быть закреплен за тем курсом, на который записан студент."""

def take_grades(name, surname, course):
    """
    Формирование ключа словаря выставленных оценок
    где name, surname кто выставляет
    """
    return (name, surname, course, f"{datetime.now()}")
print(take_grades('Roy', 'Tead', 'php'))

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname, some_val):
        super().__init__(name, surname)
        self.some_val = some_val
        self.grades = {}

class Reviewer(Mentor):
    def __init__(self, name, surname, some_val):
        super().__init__(name, surname)
        self.some_val = some_val
    
    def level(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[take_grades(self.name, self.surname, course)] += [grade]
            else:
                student.grades[take_grades(self.name, self.surname, course)] = [grade]
        else:
            return 'уточните запрос'