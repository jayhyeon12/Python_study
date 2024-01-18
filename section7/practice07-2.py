num = int(input("임의의 양수를 입력하세요 >>> "))
result = 0
for i in range(num):
    # 사용자가 5을 입력하면 1+2+3+4+5의 합계가 result가 되어야 함!
    result += i+1
    # result = result + 1

print(f'1부터 {num}사이 모든 정수의 합계는 {result}입니다.')