# 구구단을 입력받아 출력!
dan = int(input("출력할 구구단을 입력하세요 >>> "))

for n in range(1, 10, 2):
    print(f"{dan}×{n}={dan*n}")