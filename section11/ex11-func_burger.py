'''
def 나_함수(매개 변수1, 매개 변수2):
    return '나_반환값'

나_함수(나_인수1, 나_인수2)
'''
# 햄버거 가게
# 1. 인수 없음, 반환값 없음
def greet():
    print("어서오세요, 손님!")

# greet()
# 2. 인수 있음, 반환값 없음
# def order(burger, money):
#     print(f"{burger}, {money}원 주문 받았습니다.")
#     print("잠시만 기다려 주세요!")

# order("치즈버거", 3000)
    
# 3. 인수 있음, 반환값 있음
# def order(burger, money):
#     print(f"{burger}, {money}원 주문 받았습니다.")
#     print(f"주문하신 {burger}가 나왔습니다.")
#     return "cheese burger"

# my_bag = order("치즈버거", 3000)
# print(f"내 가방에 {my_bag}가 있어!")

# 4. 인수 없음, 반환값 있음
def give_coke():
    print("콜라는 서비스 입니다 ^^")
    return 'coke'

my_bag = give_coke()
print(f"내 가방에 {my_bag}가 있어!")
