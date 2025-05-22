class A:
    # 클래스 변수(static)
    name = 'A'

    # 생성자
    def __init__(self, data = 10):
        # self = java의 this
        print(self)
        self.data = data

    def print_data(self):
        print(self.data)

# 주소가 자동으로 들어감.
obj1 = A()
obj2 = A(100)
print(obj1)
print(obj1.data)
print(obj2)
print(obj2.data)
print(A.print_data())