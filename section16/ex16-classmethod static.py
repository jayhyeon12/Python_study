# 정적(static) 메서드: @(데코레이션)staticmethod 

class Korean:
  country = '대한민국'

  @staticmethod
  def trip(country):
    if Korean.country == country:
      print('국내여행 입니다')
    else:
      print('해외여행 입니다')

# print(Korean.country)
kt = Korean()
kt.trip('대한민국')
kt.trip('Germany')

