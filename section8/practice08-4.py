"1번 조건 : 홀수단만 출력"
"2번 조건 : 단수 만큼만 출력"

for dan in range(2, 10):
    if dan % 2 == 0:
        print()
        continue
    for num in range(1, 10):
        if dan < num:
            break
        print(f"{dan}×{num}={dan*num}")