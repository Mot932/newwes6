class Human:
    def __init__(self):
        self.name = "Вася"

    
    def speak(self):
        print(f"Я {self.name}, я обычный человек")

class Student(Human):
    def __init__(self):
        super().__init__()
        self.grades = []

    def speak(self):
        print(f"Я {self.name}, я студент и я не сплю уже неделю, помогите!")

    

h = Human()
C = Student()

print(h.name)
print(C.name)
h.speak()
C.speak()
