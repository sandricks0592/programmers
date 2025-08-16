# 목표 금액 100만원
# 첫 달 x 원 넣고 70만원까지는 조금씩 저축
# 70만원 이후부터는 저축량을 늘린다.
# 첫달 저축하는 금액 : int start
# 두 번째 달 부터 70만 원 이상 모일때까지 매월 저축하는 금액 : int before
# 100만원 이상 모일때까지 : int after
# 100만원 이상 모을 때 까지 걸리는 개월 수

start,before,after = map(int, input().split)
total_money = 0
def save_money(start,before,after):
    total_money = start
    while total_money < 70:
        total_money += before
    while total_money 