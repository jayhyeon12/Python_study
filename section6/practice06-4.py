# 중복! 중복제거 자료형 set()
# 사용자로 부터 5개의 정수를 입력받는 프로그램
"0 ~ 9 사이 정수를 입력하세요 >>> " # 입력
"""모두 입력되었습니다.
입력된 값은 {0, 1, 2, 3, 5}입니다.""" # 출력

numbers = set()
while len(numbers) < 5:
    num = int(input("0 ~ 9 사이 정수를 입력하세요 >>> "))
    numbers.add(num)

print("모두 입력되었습니다.")
print(f"입력된 값은 {numbers}입니다.")

            