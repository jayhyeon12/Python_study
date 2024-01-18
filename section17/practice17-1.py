class Quiz:
  answer = ['경기도', '강원도', '충청남도', '충청북도', '전라남도', '전라북도', '경상남도', '경상북도', '제주특별자치도']

  @classmethod
  def challenge(cls):
    if not cls.answer:
      print('모든 도를 맞췄습니다. 성공입니다')
      return
    
    do = input('정답은>>')

    if do not in cls.answer:
      raise Exception('오답입니다')

    for i, v in enumerate(cls.answer):
      if v == do:
        print('정답입니다')
        cls.answer.pop(i)
        break

    cls.challenge()

try:
  print('우리나라 9개의 모든 도를 맞추는 퀴즈입니다. 하나씩 대답하세요')
  Quiz.challenge()

except Exception as e:
  print(e)