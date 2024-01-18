# 1분 60초
# 1시간 60분 또는 3600초
# 입력 : "초를 입력하세요 >>> " # 3690
# 출력 결과
# "변환 결과는 1시간 1분 30초입니다."
# 힌트: 산술연산자 사용(//, %)
times = int(input("초를 입력하세요 >>> "))
hour = times // 3600
minute = times % 3600 // 60
second = times % 60
print(f"변환 결과는 {hour}시간 {minute}분 {second}초입니다.")