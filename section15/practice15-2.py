'''
watch class 정의
- 시간을 입력하세요: hh:mm:ss
- 인스턴스 변수: hour, minute, second
- add_hour()

인스턴스 메서드
add_hour() # 0~23
add_minute() # 0~59
add_second() # 0~59

출력 결과: '계산된 시간은 00시 00분 00초 입니다'
'''

class Watch:
  def set_time(self):
    now = input('시간을 입력하세요>>')
    hms = now.split(':')
    self.hour = int(hms[0])
    self.minute = int(hms[1])
    self.second = int(hms[2])

  def add_hour(self, hour):
    if hour <= 0:
      return
    self.hour += hour
    self.hour %= 24

  def add_minute(self, minute):
    if minute <= 0:
      return
    self.minute += minute
    self.add_hour(self.minute // 60)
    self.minute %= 60
  
  def add_second(self, second):
    if second <= 0:
      return
    self.second += second
    self.add_minute(self.second // 60)
    self.second %= 60

  def see(self):
    print(f'계산된 시간은 {self.hour}시 {self.minute}분 {self.second}초 입니다')

watch = Watch()
watch.set_time()
watch.add_hour(int(input('계산할 시간을 입력하세요')))
watch.add_minute(int(input('계산할 분을 입력하세요')))
watch.add_second(int(input('계산할 초를 입력하세요')))
watch.see()