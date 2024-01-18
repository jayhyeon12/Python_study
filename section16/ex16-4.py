# 클래스의 상속
# - 부모 클래스(슈퍼, 기반): 클래스(변수, 메서드)를 상속하는 클래스 
# - 자식 클래스(서브, ): 클래스를 상속 받는 클래스. '클래스 명(상속하는 클래스명)' 으로 작성

class Person:
  def __init__(self, name):
    self.name = name

  def eat(self, food):
    print(f'{self.name}가 {food}를 먹습니다')

mr_drac = Person('nickson')
mr_drac.eat('피자')


class Student(Person):
  def __init__(self, school):
    super().__init__(self, school)
    self.school = school

  def study(self):
    print(f'{self.school}에서 공부합니다')

mr_drac = Student('메사추세츠공과대학')
mr_drac.study()
mr_drac.eat('불고기')

print(isinstance(mr_drac, Student))