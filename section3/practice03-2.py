days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

'1~12 사이의 월을 입력하세요 >>> '
'2월 28일까지 있습니다.'
# list 인덱스는 0부터 시작
# 사용자의 입력은 1부터 시작

# 1. 사용자로 부터 월 입력 받기
# 2. 정수로 변환
# 3. 변수에 할당
month = int(input('1~12 사이의 월을 입력하세요 >>> '))
# 4. 문자열 동적 출력
print(f'{month}월 {days[month-1]}일까지 있습니다.')