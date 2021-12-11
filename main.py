class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and isinstance(self, Student):
            if course in lecturer.grades and course in self.grades:
                lecturer.grades[course] += [grade]
            else:
                return 'Ошибка'
        else:
            return 'Ошибка'

    def average_grades(self):
        mean_grades = 0
        number_grades = 0
        for course, grades in self.grades.items():
            mean_grades += sum(grades)
            number_grades += len(grades)
        average_grade = round(mean_grades / number_grades, 1)
        return average_grade

    def __lt__(self, other):
        if not isinstance(self, Student) and not isinstance(other, Student):
            print('Ошибка')
            return
        return Student.average_grades(self) < Student.average_grades(other)


    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания:' \
              f' {Student.average_grades(self)}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
              f'Завершенные курсы: {", ".join(self.finished_courses)}'
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

    def average_grades(self):
        mean_grades = 0
        number_grades = 0
        for course, grades in self.grades.items():
            mean_grades += sum(grades)
            number_grades += len(grades)
        average_grade = round(mean_grades / number_grades, 1)
        return average_grade

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {Lecturer.average_grades(self)}'
        return res

    def __lt__(self, other):
        if not isinstance(self, Lecturer) and not isinstance(other, Lecturer):
            print('Ошибка')
            return
        return Lecturer.average_grades(self) < Lecturer.average_grades(other)


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and isinstance(self, Reviewer) and course in self.courses_attached and \
                course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res

def mean_grades_students(all_students, course):
    all_grades = 0
    all_number_grades = 0
    for student in all_students:
        for path, grades in student.grades.items():
            if path == course:
                all_grades += sum(grades)
                all_number_grades += len(grades)
    average_grade = round(all_grades / all_number_grades, 1)
    return f'Средняя оценка студентов в рамках курса {course}: {average_grade}'

def mean_grades_lectures(all_lectures, course):
    all_grades = 0
    all_number_grades = 0
    for lecturer in all_lectures:
        for path, grades in lecturer.grades.items():
            if path == course:
                all_grades += sum(grades)
                all_number_grades += len(grades)
    average_grade = round(all_grades / all_number_grades, 1)
    return f'Средняя оценка лекторов в рамках курса {course}: {average_grade}'


first_student = Student('Максим', 'Исаев', 'your_gender')
first_student.courses_in_progress += ['Python']
first_student.courses_in_progress += ['GIT']
first_student.grades['Python'] = [10, 9, 7]
first_student.grades['GIT'] = [10, 10, 10, 10]
# print(first_student)

second_student = Student('Рихард', 'Зорге', 'your_gender')
second_student.courses_in_progress += ['GIT']
second_student.courses_in_progress += ['Python']
second_student.grades['GIT'] = [10, 9, 10]
second_student.grades['Python'] = [9, 10]
# print(second_student)

first_lecturer = Lecturer('Данила', 'Багров')
first_lecturer.grades['GIT'] = []
first_lecturer.grades['Python'] = []
first_student.rate_hw(first_lecturer, 'Python', 10)
second_student.rate_hw(first_lecturer, 'Python', 8)
first_student.rate_hw(first_lecturer, 'GIT', 9)
# print(first_lecturer)

second_lecturer = Lecturer('Сергей', 'Бодров')
second_lecturer.grades['GIT'] = []
second_lecturer.grades['Python'] = []
first_student.rate_hw(second_lecturer, 'GIT', 10)
second_student.rate_hw(second_lecturer, 'Python', 10)
second_student.rate_hw(second_lecturer, 'GIT', 9)
# print(second_lecturer)

# print(first_student > second_student)
# print(first_lecturer > second_lecturer)

first_reviewer = Reviewer('Глеб', 'Жеглов')
first_reviewer.courses_attached += ['Python']
first_reviewer.rate_hw(first_student, 'Python', 8)
# print(first_student.grades)

second_reviewer = Reviewer('Владимир', 'Шарапов')
second_reviewer.courses_attached += ['GIT']
second_reviewer.rate_hw(second_student, 'GIT', 8)
# print(second_student.grades)

all_students = [first_student, second_student]
# print(mean_grades_students(all_students,'GIT'))

all_lectures = [first_lecturer, second_lecturer]
# print(mean_grades_lectures(all_lectures,'Python'))
