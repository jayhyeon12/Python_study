# 소멸자(__del__)

import time

class Sample:
  def __del__(self):
    print('인스턴스가 소멸했습니다')

sample = Sample()
time.sleep(2)
del sample
input()