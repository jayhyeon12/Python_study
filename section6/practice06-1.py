"정수를 입력하세요 >>> " # 입력
"잘못된 입력입니다." # 출력: 0이하의 값 입력시
"1번째 Hello" # 출력

n = int(input("정수를 입력하세요 >>> "))
if n <= 0:
    print("잘못된 입력입니다.")

i = 1
while i <= n:
    print(f"{i}번째 Hello")
    i += 1