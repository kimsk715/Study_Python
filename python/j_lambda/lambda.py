# add = lambda x,y: x + y
# result = add(1,2)
# print(result)
# print("*" * 50)
#
# datas = [1, 2, 3, 4, 5]
# datas = list(map(lambda x : x * 2, datas))
# print(datas)
# print("*" * 50)
# 실습
#


# 경로(/a, /b, ..) 앞에 /app 연결시키기
# urls = ['/game', '/news', '/fashion', '/ranking']
# urls = list(map(lambda url : '/app'+url, urls))
# print(urls)
# urls = list(map(lambda url : f'/app{url}', urls))
# print(urls)
#
# # 1~10까지 짝수만 출력
#
# result = list(filter(lambda num : num % 2 == 0 ,[i for i in range(1,11)]))
# print(result)

# game 서비스를 제공하는 경로 찾기
# urls = ['/game', '/news', '/fashion', '/ranking']
# services = list(map(lambda url : f'/app{url}', urls))
#
# for service in services:
#     service = service.split('/')
#     if service.__contains__("game"):
#         print(service)
#
# print(list(filter(lambda service : service.__contains__("game"), services)))

#===============================================================
add = lambda x, y: x + y

result = add(1, 2)
print(result)

print("*" * 50)

datas = [1, 2, 3, 4, 5]
datas = list(map(lambda x: x * 2, datas))
print(datas)

# 경로(/a, /b, ..) 앞에 /app 연결시키기
urls = ['/game', '/news', '/fashion', '/ranking']
result = list(map(lambda url: f'/app{url}',urls))
print(result)

# 1~10까지 중 짝수만 출력
print(list(filter(lambda number: number % 2 == 0, [i for i in range(1, 11)])))

# result에서 'game'서비스를 제공하는 경로 찾기
urls = ['/game', '/news', '/fashion', '/ranking']
result = list(map(lambda url: f'/app{url}',urls))

print(list(filter(lambda url: url.split("/")[-1] == 'game', result)))
