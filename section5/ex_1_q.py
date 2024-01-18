# 5가지 : 매우 만족(90이상), 만족(80이상), 그저 그럼(60이상), 불만(30이상), 매우 불만(30미만)
score = int(input("제 점수는... "))

if score >= 90:
    print("매우 만족")
elif score >= 80:
    print("만족")
elif score >= 60:
    print("그저 그럼")
elif score >= 30:
    print("불만")
else:
    print("매우 불만")

