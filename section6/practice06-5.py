# 개행(줄바꿈) => 10단위 출력
n = 1
while n <= 100:
    if n % 10 == 0:
        print(n)
    else:
        print(n, end="\t")
    n += 1