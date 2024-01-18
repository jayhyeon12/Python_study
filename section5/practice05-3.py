# 가장 큰 수 구하기

num1 = int(input("정수1 입력 >>> "))
num2 = int(input("정수2 입력 >>> "))
num3 = int(input("정수3 입력 >>> "))

# if num1 > num2 and num1 > num3:
#     max_num = num1
# elif num2 > num1 and num2 > num3:
#     max_num = num2
# else:
#     max_num = num3

max_num = max(num1, num2, num3)

print(f"가장 큰 수는 {max_num}입니다.")