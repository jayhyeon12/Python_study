# result = "a" if False else "b" # 조건 삼항 연산자
# print(result)
'''
lst = [1, 2, 3] # 리스트 안에 값 넣기
# ! 리스트 표현식 = [표현식 for 변수 in 반복가능객체]
new_lst = [n * 10 for n in lst] # 리스트 안에 식 넣기(리스트 내포, list comprehension, 리스트 표현식)
print(new_lst)

for_lst = []
for n in lst:
    for_lst.append(n * 10)
print(for_lst)
'''

exam = [100, 83, 100, 96, 86, 90, 59, 100, 76, 55]
# result = [100, 88, 100, 100, 91, 95, 64, 100, 81, 60]
score = [min(n + 5, 100) for n in exam]
print(score)

