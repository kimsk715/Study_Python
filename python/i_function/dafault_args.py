# 오버로딩 없음.

def add(number1, number2, number3 = 0):
    return number1 + number2 + number3

result = add(1,2)
print(result)

result = add(1,2, 3)
print(result)