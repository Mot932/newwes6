from random import randint



class Student:
    def __init__(self, name) -> None:
        self.name = name
        self.grades = []
       
    def get_grade(self, grade: int):
        self.grades.append(grade)


    def get_random_grade(self):
        self.grades.append(randint(1, 5))


s1 = Student("Вася Чёрный")
s2 = Student("Киррил Анушко")
print(s1.name)
print(s2.name)
print(s1.grades)
print(s2.grades)
for i in range(5):
    s1.get_random_grade()
for i in range(5):
    s2.get_random_grade()
print(f"Получил оценки {s1.name} {s1.grades}")
print(f"Получил оценки {s2.name} {s2.grades}")

