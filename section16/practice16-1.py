class Person:
  count = 0

  def __init__(self, name):
    self.name = name
    print(f'{name} is born')
    Person.count += 1
  
  def __del__(self):
    print(f'{self.name} is dead')
    Person.count -= 1

  @classmethod
  def get_count(cls):
    return cls.count

man = Person('james')
woman = Person('emily')

del man

print(f'전체 인구 수: {Person.get_count()}')
input()