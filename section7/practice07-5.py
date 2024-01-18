for n in range(1, 101):
    units = n % 10
    tens  = n // 10
    con1 = units % 3 == 0 and units != 0
    con2 = tens % 3 == 0 and tens != 0
    if con1 and con2:
        print("짝짝", end="\t")
    elif con1 or con2:
        print("짝", end="\t")
    else:
        print(n, end="\t")
    if n % 10 == 0:
        print()