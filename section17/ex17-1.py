try:
  height = float(input('키를 입력하세요>>'))
  height = round(height)
  print(f'입력한 키는 {height}로 처리됩니다')

except:
  print('예외가 발생했습니다')