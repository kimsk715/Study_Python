# 기본 값
# start = 0, step = 1
# for i in range(0, 10, 1):
#     print(i)

# for i in range(10):
#     print(i)

# for i in range(100):
#     print(100 - i)

# 실습
# 1~15까지 출력
print(f"\n")
for i in range(15):
    print(i+1, end=' ')

print(f"\n")

# 30~1까지 출력
for i in range(30):
    print(30-i, end=' ')
print(f"\n")

# 1~100까지 중 홀수만 출력
for i in range(50):
    print(i*2+1, end=' ')
print(f"\n")

# 1~10까지 합 출력
result = 0
for i in range(10):
    result += i+1
print(result, end=' ')
print(f"\n")

# 1~n까지 합 출력
number1 = input("숫자를 입력하세요 : ")
result = 0
for i in range(int(number1)):
    result += i+1
print(result, end=' ')
print(f"\n")

# 3 4 5 6 3 4 5 6 3 4 5 6 출력
for i in range(12):
    print(i%4 + 3, end=' ')