# 1박스 : 20개 => 21개 : 2박스 필요
print("""한 박스에 20개의 라면을 담을 수 있습니다.
라면의 개수를 입력하시면 필요한 박스 수를 알려드립니다.""")
ramen = int(input("라면의 개수를 입력하세요 >>> "))
# 20으로 나눴을때 나머지가 있으면 +1박스, 아니면 +0박스

result = ramen // 20 if ramen % 20 == 0 else ramen // 20 + 1 # 힌트: 조건삼항, % 연산자 사용

print(f"{ramen}개 라면을 담으려면 {result}박스가 필요합니다.")