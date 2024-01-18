# raise : 의도적으로 에러 유발

'''
사용자에게서 나이(양수) 입력 받기

'''

age = int(input('나이를 입력하세요>>'))

try:
  if age <= 0:
    raise Exception('0보다 적은 나이는 입력할 수 없습니다')
  print(f'당신의 나이는 {age}세 입니다')

except Exception as e:
  print(e)