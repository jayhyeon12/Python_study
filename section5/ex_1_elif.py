# 나의 파이썬 실력은? "상/중/하"
q1 = input("조건 삼항 연산자 알아요? (y/n)")
q2 = input("class에 대해 알아요? (y/n)")
'''
if q1 == 'y':
    # 중첩 조건문(if문)
    if q1 == 'y' and q2 == 'y':
        print('나의 파이썬 실력은 "상"이지!')
    else:
        print('나의 파이썬 실력은 "중"이지!')
else:
    print('나의 파이썬 실력은 "하"이지!')
'''

if q1 == 'y' and q2 == 'y':
    print('나의 파이썬 실력은 "상"이지!')
elif q1 == 'y' and q2 == "n":
    print('나의 파이썬 실력은 "중"이지!')
else:
    print('나의 파이썬 실력은 "하"이지!')