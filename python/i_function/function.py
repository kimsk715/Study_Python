# 두 정수의 합

def add(number1, number2):
    return number1 + number2

result = add(1, 2)
print(result)

# 두 정수의 나눗셈 후 몫과 나머지

def divide(number1, number2):
    return number1 // number2 , number1 % number2

result1 = divide(10,3)
print(result1)


# unpacking
value, rest = divide(10,3)
print(value, rest, sep=', ')