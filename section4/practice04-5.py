a = int(input("국어 점수를 입력하세요 >>> "))
b = int(input("영어 점수를 입력하세요 >>> "))
c = int(input("수학 점수를 입력하세요 >>> "))

avg = (a + b + c) / 3
# 평균 80점 이상이면 합격, 아니면 불합격
result = '합격' if avg >= 80 else '불합격'

print(f'평균은 {avg}점이고, 결과는 {result}입니다.')