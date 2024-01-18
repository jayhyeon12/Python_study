class Bag:
  count = 0 # 클래스 변수
  
  def __init__(self):
    Bag.count += 1

  @classmethod
  def sell(cls): # 클래스 메서드
    cls.count -= 1

  @staticmethod
  def sell_any():
    Bag.count -= 1

  @classmethod
  def remain_Bag(cls):
    return cls.count


bag1 = Bag()
bag2 = Bag()
bag3 = Bag()
bag4 = Bag()
bag5 = Bag()


bag1.sell()
bag2.sell()
Bag.sell_any()

print(f'현재 가방: {Bag.remain_Bag()}개')