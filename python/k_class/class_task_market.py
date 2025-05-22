# 상품
# 상품명, 가격
# 상품의 정보를 print()로 출력하는 함수

# 마켓
# 상품, 재고
# 손님 한 명에게 한 개의 상품을 판매한다.
# 판매 시 손님의 할인율을 적용하여 판매한다.

# 손님
# 이름, 나이, 할인율, 잔액

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def print_data(self):
        print(self.name)
        print(self.price)


class Market:
    def __init__(self, product, stack):
        self.product = product
        self.stack = stack

    def sell_product(self, customer):
        if self.stack <= 0 :
            print("재고 X")
            return

        discounted_price = self.product.price * (1 - customer.discount)
        if customer.money < discounted_price:
            print("잔고 부족")
            return
        else:
            customer.money -= discounted_price
            self.stack -= 1
            print(f'고객님 잔고는 {int(customer.money)}원 이고, 재고는 {self.stack}개 입니다.')

class Customer:

    def __init__(self, name, age, discount, money):
        self.name = name
        self.age = age
        self.discount = discount
        self.money = money



product = Product("노트북", 1000)
# 할인율은 소수점으로 가정했음.
customer = Customer("홍길동", 30, 0.1, 10000)
market = Market(product, 100)

product.print_data()
market.sell_product(customer)