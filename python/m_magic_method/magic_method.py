class Student:
    def __init__(self, score):
        self.score = score

    def __add__(self, other):
        return self.score + other.score

    def __str__(self):
        return "한동석 짱"


std1 = Student(30)
std2 = Student(50)
print(std1)
print(std2)
print(std1 + std2)