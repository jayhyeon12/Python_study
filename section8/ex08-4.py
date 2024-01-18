count = 1
total = 0
while count <= 5:
    n = int(input(f"{count}번째 정수를 입력하세요 >>> "))
    if n <= 0:
        print("0이하의 정수는 처리할 수 없습니다.")
        continue
    total += n
    count += 1

print(f"입력된 5개 양수의 총 합은 {total}입니다.")