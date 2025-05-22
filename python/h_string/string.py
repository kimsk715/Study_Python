print(list("ABC"))

for i in "ABC":
    print(i)

print("Apple123!@#".upper())
print("Apple123!@#".lower())

data = "사과, 바나나, 파일애플, 포도, 복숭아"
print(data.split(", ", maxsplit=3))

print("A B C D E F".split())
print("A         B".split())
print("A    B".split(" "))

# join()
result = ",".join(['a', 'b', 'c'])
print(result)

result = "".join(['a', 'b', 'c'])
print(result)

# replace('기존 값', '새로운 값')
print("A b C d".replace(" ", ""))
print("       Abcd      ".replace(" ", ""))
print(len("       Abcd      ".strip()))

# find()
# print("ABC".index("Z"))
print("ABC".find("Z"))

# print([1, 2, 3, 4].index(10))

# count('검색할 값')
print("fnmsdkjfnenqoinfndsjklnfjkdnsofnpoiqnpnaipfniopdnfiofnol".count('f'))

# 아래 문자열을 189000 출력, join() 사용
# '0' <= i <= '9'
s = "189,000 원"
result = "".join(i for i in s if '0' <= i <= '9')
print(result)

