import datetime # 날짜, 시간 다룸

present = datetime.datetime.now()
print(present)

birthday = datetime.date(1950, 1, 1)
print(birthday) # 1950-01-01

wake = datetime.time(10, 48, 0)
print(wake) # 10:48:00

print(present.year)
print(present.month)
print(present.day)
print(present.hour)
print(present.minute)
print(present.second)

yesterday = present - datetime.timedelta(days=1) # 1일
print(yesterday)

tomorrow = present + datetime.timedelta(days=1) # 1일
print(tomorrow)

date1 = datetime.date(2023, 12, 10)
date2 = datetime.date(2023, 12, 11)
tomorrow_seconds = (date2-date1).total_seconds()
print(tomorrow_seconds) # 86400.0
