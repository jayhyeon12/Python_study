import random

print(random.randint(1, 10))
print(random.randrange(1, 11, 2))
print(random.random()) # 0~1미만 사이의 실수

seasons = ["봄", "여름", "가을", "겨울"]
print(random.choice(seasons))

nums = range(1, 46)
print(random.sample(nums, 6)) # 중복된 요소가 없도록 함

my_list = [1, 2, 3, 4, 5]
print(my_list)
print(random.shuffle(my_list)) # 불변성을 유지 하지 않음, 기존 값을 변경함, 리턴값 None
print(my_list)



