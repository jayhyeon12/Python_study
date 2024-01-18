"현재 10000원이 있습니다."
"사용할 금액 입력 >>> " # 5000
"현재 5000원이 있습니다."

money = 10000

while True:
    if money == 0:
        break
    spend = input("사용할 금액 입력 >>> ")
    if spend == '':
        print("금액을 입력해 주세요!")
    else:
        spend = int(spend)
        if spend <= 0:
            print("0이하의 금액은 사용할 수 없습니다.")
        elif spend > money:
            print(f"{spend - money}원이 부족합니다.")
        else:
            money -= spend
            print(f"현재 {money}원이 있습니다.")
