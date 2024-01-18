import time

# file = open(time.strftime('%Y-%m-%d')+'.txt', 'at', encoding='utf-8')

# while True:
#     schedule = input("오늘의 스케줄을 입력하세요 >>> ")
#     if not schedule:
#         break
#     file.write(f'{schedule}\n')

# file.close()

with open(time.strftime('%Y-%m-%d')+'.txt', 'at', encoding='utf-8') as f:
    while True:
        schedule = input("오늘의 스케줄을 입력하세요 >>> ")
        if not schedule:
            break
        f.write(f'{schedule}\n')
