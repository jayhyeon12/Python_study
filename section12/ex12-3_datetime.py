from datetime import *

start = datetime.now()
total = 0
for num in range(1, 10000001):
    total += num
end = datetime.now()

print(f'총 합은 {total}입니다.')
print(f'총 {(end - start).total_seconds()}초가 소요되었습니다.')