# def introduce(**info):  #dictionary로 입력
#     print(type(info))
#     print(info)

# introduce(name = "한동석", age = 20)

# info = {"name":"한동석", "age":20}
# introduce(**info)


# unpacking
# def print_info(*, name, email):
#     print(name, email)


# info2 = {"name":"한동석", "email": "test@gamil.com"}
# print_info(name = "한동석", email = "test@gamil.com")
# print_info(**info2)

# 회원의 주문 금액(pay)과 회원의 쿠폰 할인율과 개수(coupon, count)를 전달받은 뒤
# 회원이 보유한 쿠폰의 할인율을 주문 금액에 순차 적용하는 함수 제작
# 할인율이 적용된 주문 금액이 정수로 리턴된다.
# 쿠폰의 할인율은 백분율로 되어있다.
# 쿠폰의 개수는 주문 개수보다 많을 수 있다.




grade = {"kor" : 100, "eng" : 80, "math" : 90}

def get_average(**grade):
    sum = 0
    for item in grade.values():
        sum += item

    average = sum/len(grade)
    print("*" * 50)
    print(average)

get_average(**grade)

info = {"discount" : 33, "count" : 13} # 쿠폰 정보
pay = [i*10000 for i in range(1,11)] # 주문 가격 정보

def get_discount(*pay, **info):
    result = []
    for item in pay:
        if info["count"] > 0 : # 쿠폰이 남아 있는 경우
            info["count"] -= 1 # 쿠폰 차감
            item -= (info["discount"] / 100)*item
            result.append(int(item))
        else: # 쿠폰이 모자란 경우
            result.append(int(item))
    formatting = "남은 쿠폰 수 : {}".format(info["count"])
    print("*" * 50)
    print(formatting)
    print("*" * 50)
    print(result)
    print("*" * 50)

get_discount(*pay, **info)

# 국어, 영어, 수학 점수의 평균 구하기
def get_average(**scores):
    kor = scores.get('kor')
    eng = scores.get('eng')
    math = scores.get('math')

    total = kor + eng + math
    average = total / scores.get('length')
    return average

scores = {'kor': 100, 'eng': 90, 'math': 80, 'length': 3}
average = get_average(**scores)
print(average)

# 회원의 주문 금액(pay)과 회원의 쿠폰 할인율과 개수(coupon, count)를 전달받은 뒤
# 회원이 보유한 쿠폰의 할인율을 주문 금액에 순차 적용하는 함수 제작
# 할인율이 적용된 주문 금액이 정수로 리턴된다.
# 쿠폰의 할인율은 백분율로 되어있다.
# 쿠폰의 개수는 주문 개수보다 많을 수 있다.

def use_coupon(*pay, **kwargs):
    return [pay[i] * (1 - (kwargs.get('coupon') * 0.01))
            for i in range(len(pay) if kwargs.get('count') >= len(pay) else kwargs.get('count'))]

print(use_coupon(1000, 2000, 3000, coupon=40, count=2))

