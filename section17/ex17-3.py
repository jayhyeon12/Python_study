try:
  score = int(input('점수 입력하세요>>'))
  if score < 0 or score > 100:
    raise Exception('점수는 0~100 사이에서 입력 가능합니다')

except Exception as e:
  print(e)

else:
  if score >= 80:
    print(f'{score}점은 합격입니다')
  else:
    print(f'{score}점은 불합격입니다')