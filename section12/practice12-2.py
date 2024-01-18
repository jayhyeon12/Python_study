import random
import time
import math

num = random.randint(1, 10)

print("UpDown게임을 시작합니다.")
start = time.time()
while True:
    n = int(input("어떤 값일까요? >>> "))
    if num == n:
        print('정답입니다.')
        break
    elif num < n:
        print('Down')
    else:
        print('Up')
end = time.time()
print(f'{math.floor(end - start)}초 만에 성공했습니다.')
    