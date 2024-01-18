class Coffee:
  def __init__(self, bean):
    self.bean = bean

  def coffee_info(self):
    print(f'원두: {self.bean}')

class Espresso(Coffee):
  def __init__(self, bean, water):
    super().__init__(self, bean)
    self.water = water
  
  def espresso_info(self):
    super().coffee_info()
    print(f'물의 양: {self.water}')


coffee = Espresso('콜롬비아', '30')
coffee.espresso_info()