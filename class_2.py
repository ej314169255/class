from datetime import datetime
import time
""" The datetime module is used to commit to the dictionary.
    with the name of the person who gave the grade, the name of the subject
    for the uniqueness of recording and analysis
    
    time is used to stimulate delay
    at the time of the assessment

"""

def average_of_dict(b):
    remember_grades = b
    counter = 0
    for key, value in remember_grades.items():
        counter += value
    return round(counter/len(remember_grades), 2)


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course):
        self.finished_courses.append(course)

    def level(self, evaluated, course, vol):
        if course in self.courses_in_progress and course in evaluated.courses_attached:
            evaluated.grades[self.name, self.surname, course, f"{datetime.now()}"] = vol

    def calculate_grades(self, grades):
        return average_of_dict(grades)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

class Reviewer(Mentor):
    def __init__(self, name, surname, cur_example_class):
        super().__init__(name, surname)
        self.cur_example_class = cur_example_class

    def level(self, evaluated, course, vol):
        if isinstance(evaluated, self.cur_example_class) and \
                course in self.courses_attached and \
                course in evaluated.courses_in_progress:
            evaluated.grades[self.name, self.surname, course, f"{datetime.now()}"] = vol


best_student = Student('Ruoy', 'Eman', 'man')
best_student.courses_in_progress += ['R', 'Python']

cool_mentor = Reviewer('Some', 'Buddy', Student)
cool_mentor.courses_attached = ['R', 'Python']

cool_mentor.level(best_student, 'R', 10)
time.sleep(0.001)
cool_mentor.level(best_student, 'R', 10)
time.sleep(0.001)
cool_mentor.level(best_student, 'Python', 5)

lecturer = Lecturer('Том', 'Сойер')
lecturer.courses_attached =['Python']
best_student.level(lecturer, 'Python',7)
time.sleep(0.000005)
best_student.level(lecturer, 'Python', 8)
print(best_student.courses_in_progress)
print(best_student.calculate_grades(best_student.grades))
print(lecturer.grades)
