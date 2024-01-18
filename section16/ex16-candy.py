# 생성자(__init__)

class Candy:
  def __init__(self, shape, color): # __:던더스코어
    self.shape = shape
    self.color = color

candy = Candy('오각형', '보라색')
print(candy.shape)
print(candy.color)