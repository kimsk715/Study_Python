# Comprehension (어떤 뜻을 내포.)
# 반복되거나 특정 조건을 만족하는 리스트를 보다 쉽게 만들어 내기 위한 방법.

# List Comprehension 구문
# [표현식 for 변수 in iterator (if 조건)] --> 조건식은 생략 가능

datas = [1, 2, 3, 4]

result1 = [i * 3 for i in datas]
print(result1)

result2 = [i * 3 for i in datas if i % 2 == 0]
print(result2)
print("*" * 50)

# 실습
# 양수만 추출 & 출력
datas = [10, 20, 30, -20, -3, 50, -70]
result3 = [i for i in datas if i > 0]
print(result3)

# 제곱의 결과가 10보다 큰 값만 담은 List -> 제곱의 값이 아닌 원본 list의 값.
datas = [1, -2, 3, -4, 5]
result4 = [i for i in datas if i**2 > 10]
print(result4)

# 0 ~ 9 중 3의 배수만 출력
result5 = [i for i in range(10) if i % 3 == 0]
print(result5)


