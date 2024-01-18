try:
  filename = input('열려는 파일 이름을 입력하세요>>')
  file = open(f'./section17/{filename}', 'rt')

except:
  print(f'{filename}을 찾을 수 없습니다')

else:
  buffer = file.read()
  print(buffer)
  file.close()

finally:
  print('프로그램 종료합니다')