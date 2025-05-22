# name = input("이름 : ")

# 3.6 버전 이상에서 사용 가능

# formatting = f"{name}님 환영합니다."

# print(formatting)

# 두 정수를 입력받은 후 곱셈 결과 출력

# number1 = input("첫 번째 숫자 : ")
# number2 = input("두 번째 숫자 : ")
# result = int(number1) * int(number2)
# formatting = f"곱셈 결과는 {result} 입니다."
# print(formatting)

# 두 정수를 입력 받은 후 곱셈 결과 출력
import functools
result = functools.reduce(lambda x, y: x * y, list(map(int, input("두 정수를 입력하세요\nex)1, 5\n").split(", "))))
print(result)