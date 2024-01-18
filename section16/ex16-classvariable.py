# 클래스 변수

class Korean:
  country = '대한민국' 

  def __init__(self, name, gender):
    self.name = name
    self.gender = gender


mr_kim = Korean('김일남', 'M')
ms_kim = Korean('김일여', 'F')

print(f'{mr_kim.name}씨는 성별이 {mr_kim.gender}이고 국적은 {Korean.country} 입니다')
# print(f'{ms_kim.name}씨는 성별이 {ms_kim.gender}이고 국적은 {ms_kim.country} 입니다')