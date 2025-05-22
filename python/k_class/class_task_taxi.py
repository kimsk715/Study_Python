class Taxi:

    """
    # '택시'에서 승객들에게 공통적으로 적용되는 자료
    # - 기본 요금 : 5800원
    # - 기본 주행 거리 : 2km
    # - 택시 요금(기본 주행 거리 이후 거리 1km 당 요금)  : 1000원

    # 택시 객체 생성시 승객별로 돈과, 거리를 받아서 생성

    # 거리에 따른 요금 계산 메소드 정의
    # 거리에 따른 잔돈 계산 메소드 정의
    """

    basic_pay = 5800 # 기본 금액
    basic_distance = 2 # 기본 거리
    pay_of_distance = 1000 # 단위 거리 당 요금

    def __init__(self, money, distance):
        self.money = money
        self.distance = distance

    def pay(self):
        if self.distance <= Taxi.basic_distance:
            return Taxi.basic_pay
        else:
            return Taxi.basic_pay + (self.distance - Taxi.basic_distance) * Taxi.pay_of_distance

    def remain_money(self):
        pay = self.pay()
        return self.money - pay

customer1 = Taxi(20000, 0.5) # 기본 금액
print(f'지불할 금액 : {customer1.pay()}')
print(f'남은 금액 : {customer1.remain_money()}')

customer2 = Taxi(20000, 3) # 5800 + 1 * 1000 = 6800원
print(f'지불할 금액 : {customer2.pay()}')
print(f'남은 금액 : {customer2.remain_money()}')

help(Taxi)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# '택시'에서 승객들에게 공통적으로 적용되는 자료
# - 기본 요금 : 5800원
# - 기본 주행 거리 : 2km
# - 택시 요금(기본 주행 거리 이후 거리 1km 당 요금)  : 1000원

# 택시 객체 생성시 승객별로 돈과, 거리를 받아서 생성

# 거리에 따른 요금 계산 메소드 정의
# 거리에 따른 잔돈 계산 메소드 정의

class Taxi:
    init_fare = 5800
    init_distance = 2
    fare_per_km = 1000

    def calc_cost(self, money, distance):
        cost = Taxi.init_fare
        if distance > Taxi.init_distance:
            cost += (distance - Taxi.init_distance) * Taxi.fare_per_km

        def get_change():
            change = money - cost
            return change

        return cost, get_change()


taxi = Taxi()
print(taxi.calc_cost(20000, 1))
print(taxi.calc_cost(30000, 10))




#_--------------------------------------

# '택시'에서 승객들에게 공통적으로 적용되는 자료
# - 기본 요금 : 5800원
# - 기본 주행 거리 : 2km
# - 택시 요금(기본 주행 거리 이후 거리 1km 당 요금)  : 1000원

# 택시 객체 생성시 승객별로 돈과, 거리를 받아서 생성

# 거리에 따른 요금 계산 메소드 정의
# 거리에 따른 잔돈 계산 메소드 정의

class Taxi:
    init_fare = 5800
    init_distance = 2
    fare_per_km = 1000

    def calc_cost(self, money, distance):
        cost = Taxi.init_fare
        if distance > Taxi.init_distance:
            cost += (distance - Taxi.init_distance) * Taxi.fare_per_km

        def get_change():
            change = money - cost
            return change

        return cost, get_change()


taxi = Taxi()
print(taxi.calc_cost(20000, 1))
print(taxi.calc_cost(30000, 10))