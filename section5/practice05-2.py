num = int(input("정수를 입력하세요 >>> "))

if num % 3 == 0 and num != 0:
    print(f"{num}는 3의 배수입니다.")
else:
    print(f"{num}는 3의 배수가 아닙니다.")