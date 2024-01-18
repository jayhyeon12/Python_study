import random
import time

pot = list(range(1, 46))
jackpot = []

for n in range(1, 7):
    random.shuffle(pot)
    pick = pot.pop()
    jackpot.append(pick)
    print(f'{n}번째 당첨번호는 {pick}입니다.')
    time.sleep(2)

jackpot.sort()

print(f'이번 당첨번호는 {jackpot}입니다.')
# print(f'이번 당첨번호는 {sorted(jackpot)}입니다.')
