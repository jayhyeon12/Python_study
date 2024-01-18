import time # 시간을 다루는 모듈

print(time.time()) # 현제 시간을 초로 리턴함(소수점 이하는 마이크로초) 밀리초(1/1000), 마이크로초(1/1000000), 1970-1-1 00:00:00 리눅스

print(time.ctime(1702169985.8073626)) # Sun Dec 10 09:59:45 2023

print(time.ctime(time.time()))

# 2023-01-10 00:00:00
print(time.strftime('%Y-%m-%d %a %H:%M:%S')) # 2023-12-10 Sun 10:05:38
time.sleep(1) # 아래 코드의 실행을 1초간 중지
print(time.strftime('%Y/%m/%d %H:%M')) # 2023/12/10 10:06
