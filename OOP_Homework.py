# https://github.com/netology-code/py-homeworks-basic/tree/new_oop/6.classes
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lector(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def mid_grade(self):
        for grade in self.grades.values():
            res = sum(grade) / len(grade)
            return res

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.mid_grade()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы {", ".join(self.finished_courses)}'
        return res

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def mid_grade(self):
        # res = map(lambda grade: sum(grade) / len(grade), self.grades.values())
        # return list(res) вроде всё работает, но как распаковать список - не понимаю, может, подскажете?
        for grade in self.grades.values():
            res = sum(grade) / len(grade)
            return res

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.mid_grade()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Сравнение не верно!')
            return
        return list(self.grades.values()) < list(other.grades.values())

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res

def mid_students_grade(student_list, course_name):
    grades_list = []
    for student in student_list:
        if course_name not in student.courses_in_progress:
            return f'{student.name} {student.surname} не учится на данном курсе'
        grades_list.extend(student.grades.get(course_name))
        res = sum(grades_list) / len(grades_list)
    return f'Средняя оценка по студентам на курсе {course_name}: {res}'

def mid_lecturers_grade(lecturers_list, course_name):
    grades_list = []
    for lecturer in lecturers_list:
        if course_name not in lecturer.courses_attached:
            return f'{lecturer.name} {lecturer.surname} не преподает на данном курсе'
        grades_list.extend(lecturer.grades.get(course_name))
        res = sum(grades_list) / len(grades_list)
    return f'Средняя оценка по лекторам на курсе {course_name}: {res}'

hermione_granger = Student('Hermione', 'Granger', 'female')
hermione_granger.courses_in_progress += ['Python', 'Git']
hermione_granger.finished_courses += ['Введение в программирование']

ron_weasley = Student('Ron', 'Weasley', 'male')
ron_weasley.courses_in_progress += ['Python', 'Git']
ron_weasley.finished_courses += ['Введение в программирование']

steven_strange = Lecturer('Steven', 'Strange')
steven_strange.courses_attached += ['Python']

tony_stark = Lecturer('Tony', 'Stark')
tony_stark.courses_attached += ['Python']

davy_jones = Reviewer('Davy', 'Jones')
davy_jones.courses_attached += ['Python']

hector_barbossa = Reviewer('Hector', 'Barbossa')
hector_barbossa.courses_attached += ['Python']

davy_jones.rate_hw(hermione_granger, 'Python', 10)
davy_jones.rate_hw(hermione_granger, 'Python', 8)
hector_barbossa.rate_hw(ron_weasley, 'Python', 8)
hector_barbossa.rate_hw(ron_weasley, 'Python', 7)

hermione_granger.rate_lector(steven_strange, 'Python', 10)
hermione_granger.rate_lector(steven_strange, 'Python', 8)
ron_weasley.rate_lector(tony_stark, 'Python', 10)
ron_weasley.rate_lector(tony_stark, 'Python', 9)

print(hermione_granger.grades)
print(ron_weasley.grades)
print(steven_strange.grades)
print(tony_stark.grades)
print(hermione_granger)
print(ron_weasley)
print(steven_strange)
print(tony_stark)
print(davy_jones)
print(hector_barbossa)
print(steven_strange < hermione_granger)
print(mid_students_grade([hermione_granger, ron_weasley], 'Python'))
print(mid_lecturers_grade([steven_strange, tony_stark], 'Python'))