# 700원 음료수 자판기
# 음료수 개수? 잔돈 얼마?

def vending_machine(money):
    price = 700
    count = money // price
    for i in range(count + 1):
        change = money - i*price
        print(f"음료수 = {i}개, 잔돈 = {change}원")

vending_machine(3000)