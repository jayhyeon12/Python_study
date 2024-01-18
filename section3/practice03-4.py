# 동일한 입력은 무시!!!
# 학생 3명 => 사용자 입력 3번 받기
result = set()
result.add(input('희망하는 수학여행지를 입력하세요 >>> '))
result.add(input('희망하는 수학여행지를 입력하세요 >>> '))
result.add(input('희망하는 수학여행지를 입력하세요 >>> '))
print(f'조사된 수학여행지는 {result}입니다.')