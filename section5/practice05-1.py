# 100~90: A, 89~80: B, 79~70: C, 69~60: D, 59~0: F
score = int(input("점수를 입력하세요 >>> "))

if score >= 90:
    result = "A"
elif score >= 80:
    result = "B"
elif score >= 70:
    result = "C"
elif score >= 60:
    result = "D"
else:
    result = "F"

print(f"점수는 {score}점이고, 학점은 {result}학점입니다.")