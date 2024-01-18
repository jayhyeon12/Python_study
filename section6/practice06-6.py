# 2×1=2 3×1=3   4×1=4   ... 9×1=9
# 2×2=4 3×2=6   4×2=8   ... 9×2=18
# .
# .
# .

n = 1
while n <= 9:
    dan = 2
    while dan <= 9:
        print(f"{dan}×{n}={dan*n}", end="\t")
        dan += 1
    n += 1