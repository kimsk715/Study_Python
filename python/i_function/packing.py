# packing과 unpacking
# 함수 선언 시 매개 변수에 한 번에 받을 것인지(packing)
# 따로 분리해서 받을 것인지(unpacking)를 선택할 수 있음.
# unpacking
# def sub(number1, number2, number3):
#     return number1 - number2 - number3
#
#
# data = 1, 2, 3
#
#
# result = sub(*data)
# print(result)

# unpacking
# 매개변수 : a, b, c
# 사용 시 : (*datas)

# packing
# 매개변수 : *args(가변인자)
# 사용 시 : (*datas)

# n개 정수의 합
# 매개 변수의 개수를 알 수 없음.
# 가변 인자는 tuple 타입.
#packing
# def getTotal(*args):
#     total = 0
#     for i in args:
#         total += int(i)
#     return total


# print("tuple로 입력받은 값.")
# datas = list(range(1,11))
# result = getTotal(*datas)
# print(result)
# print("*" * 50)
#
# def getTotal2(number1, number2, number3):
#     return int(number1) + int(number2) + int(number3)

# unpacking
#
# datas = input("과목별 점수를 띄어쓰기로 구분해서 입력하세요.\n").split(" ")
# result = getTotal2(*datas)
# print(result)

# 문자열에서 'A'가 몇 개 있는지 검사하는 감수
# packing

def countA(*string):
    count = 0
    for char in string:
        if char == 'A':
            count += 1

    print(count)

string = input('Enter a string: ')
countA(*string)


# =====================

# packing과 unpacking
# 함수 선언 시 매개변수에 한 번에 받을 것인지(packing)
# 따로 따로 분리해서 받을 것인지(unpacking)를 선택할 수 있다.

# unpacking
# 매개변수: a, b, c
# 사용 시: (*datas)

# packing
# 매개변수: *args(가변인자)
# 사용 시: (*datas)

# unpacking
def sub(number1, number2, number3):
    return number1 - number2 - number3

data = 1, 2, 3

result = sub(*data)
print(result)

# n개 정수의 합
# 매개변수의 개수를 알 수 없다.
# 가변인자는 Tuple 타입이며, 전달할 때에는 ,로 여러 개의 값을 전달할 수 있다.
def getTotal(*numbers):
    total = 0
    for i in numbers:
        total += i

    return total

numbers = list(range(1, 11))
print(getTotal(*numbers))

# 국어, 영어, 수학 점수를 전달받은 뒤 총 점을 출력하는 함수
# unpacking
def print_total1(kor, eng, math):
    print(f'총 점: {kor + eng + math}')


def print_total2(*scores):
    total = 0
    for i in scores:
        total += i
    print(f'총 점: {total}')


scores = [i * 100 for i in range(1, 4)]
print_total1(*scores)
print_total2(*scores)


# 문자열에서 'A'가 몇 개 있는지 검사하는 함수
# packing
def get_count(*string):
    count = 0
    for i in string:
        if i == 'A':
            count += 1

    return count

count = get_count(*"ABCAD")
print(f'{count}개')








