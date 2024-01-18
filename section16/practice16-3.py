class Car:
  max_oil = 50
  
  def __init__(self, oil):
    self.oil = oil

  def add_oil(self, oil):
    if oil <= 0:
      return
    self.oil += oil
    if self.oil > Car.max_oil:
      self.oil = Car.max_oil

  def car_info(self):
    print(f'현재 주유상태: {self.oil}')

class Hybrid(Car):
  max_batt = 30

  def __init__(self, oil, batt):
    super().__init__(oil)
    self.batt = batt

  def charge(self, batt):
    if batt <= 0:
      return
    self.batt += batt
    if self.batt > Hybrid.max_batt:
      self.batt = Hybrid.max_batt

  def hybrid_info(self):
    super().car_info()
    print(f'현재 충전상태: {self.batt}')


car = Hybrid(0, 20)
car.add_oil(70)
car.charge(50)
car.hybrid_info()