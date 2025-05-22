# 여러 개의 변수를 한 줄에 선언할 때는 세미콜론 사용
from setuptools.command.alias import format_alias

a = 10; b = 20; c = 30

print(a, b, c)

a, b, c = 100, 200, 300 #unpacking
print(a, b, c)

temp = a
a = b
b = temp
print(a, b)

a, b = b, a
print(a, b)

# type(변수)
a = 10
print(type(a))

a = "한동석"
print(type(a))

formatting =  "{},{},{}".format(1,2,3)
print(f'내 이름은 {a}이다.')
print(formatting)

formatting =  "{2},{1},{0}".format(1,2,3)
print(formatting)

formatting =  "{number1}, {number2}, {number3}".format(number1 = 100, number2 = 200, number3 = 300)
print(formatting)


# 이름과 나이를 변수에 담는다.
# format()을 사용해서 출력

name, age = '한동석', 20
info = '한동석', 20
data = {name:'한동석', age: 20}

formatting = "이름: {}, 나이: {}살".format(name, age)
print(formatting)

formatting = "이름: {}, 나이: {}살".format(*info)
print(formatting)

formatting = "이름: {name}, 나이: {age}살".format(name=name, age=age)
print(formatting)
