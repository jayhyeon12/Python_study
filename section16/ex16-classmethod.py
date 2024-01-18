# 클래스 메서드: @(데코레이션)classmethod

class Korean:
  country = '대한민국'

  @classmethod
  def trip(cls, country):
    if cls.country == country:
      print('국내여행 입니다')
    else:
      print('해외여행 입니다')

# print(Korean.country)

Korean.trip('대한민국')
Korean.trip('Germany')