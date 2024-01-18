# 예외 처리
# 형식
#- try: 코드1 코드2 코드3 ... except 코드1-1 (필수) 
# else ...... finally .... (옵션)

while True:

  a = int(input('제수를 입력하세요>>'))
  b = int(input('피제수를 입력하세요>>'))

  try:
    print(f'{a} / {b} = {a/b}')
  except:
    print('0으로는 나눌 수 없습니다')

# while True:

#   a = int(input('제수를 입력하세요>>'))
#   b = int(input('피제수를 입력하세요>>'))

#   if b != 0:
#     print(f'{a} / {b} = {a/b}')
#   else:
#     print('0으로는 나눌 수 없습니다')