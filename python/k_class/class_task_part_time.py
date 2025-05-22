# PartTimer

# '모든 직원'에 공통적으로 적용되는 내용
# - 시급(pay_of_hour)
# - 직원수(total_of_part_timers)

# '각 직원'별로 적용되는 내용
# - 별명
# - 근무지(기본값: '청담동')
# - 급여 총액(초기값: 0, 생성자로 초기화 불가능)

# 직원 급여 계산
#   '근무 시간 + 상여금'에 따른 직원 급여 계산
#   '상여금'은 지정 하지 않으면 0 으로 처리


class PartTimer:
    # 공통 적용되는 시급, 직원 수
    pay_of_hour = 10000
    total_of_part_timer = 0

    def __init__(self, nickname, address="청담동"):
        self.nickname = nickname # 별명
        self.address = address # 근무지
        self.total_pay = 0
        # 생성자로 초기화 하지 않고, 기본 값은 0
        PartTimer.total_of_part_timer += 1
        # 호출 시 직원 수 증가

    def pay(self, time, bonus = 0):
        # 상여금은 기본 0, 지정할 수 있음.
        self.total_pay += PartTimer.pay_of_hour * time + bonus



staff1 = PartTimer("홍길동") # 직원 정보
staff1.pay(10, 1000) # 급여 정보

staff2 = PartTimer("김철수", "삼성동")
staff2.pay(5)

print(f"{staff1.nickname}의 급여: {staff1.total_pay}원, {staff1.nickname}의 근무지: {staff1.address}")
print(f"{staff2.nickname}의 급여: {staff2.total_pay}원, {staff2.nickname}의 근무지: {staff2.address} ")
print(f"총 직원 수: {PartTimer.total_of_part_timer}명")