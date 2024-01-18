class Service:
  def __init__(self, service):
    self.service = service
    print(f'{self.service} Service가 시작되었습니다')
  
  def __del__(self):
    print(f'{self.service} Service가 종료됐습니다')

u = Service('room')
input()
del u