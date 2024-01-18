try:

  a = int(input('제수를 입력하세요>>'))
  b = int(input('피제수를 입력하세요>>'))
  result = a / b

except ZeroDivisionError:
  print('0으로는 나눌 수 없습니다')
  
except ValueError:
  print('정수만 입력 가능합니다')

else:
  print(f'{a} / {b} = {result}')

finally: # 오류 발생 여부 상관없이 무조건 실행됨
  print('프로그램 종료합니다')