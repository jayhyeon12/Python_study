# 59쪽
# .format()
'''
[] : list(인덱싱, 슬라이싱), 문자열(인덱싱, 슬라이싱), 딕셔너리[key]
{} : set, dict
() : 함수, 메서드, 튜플
'''
# name = 'James'
'''
print('제 이름은 {}입니다.'.format(name))
name = '김일남'
age = 99
# print('제 이름은 %s입니다. 나이는 %d입니다.' %(name, age))
# print('제 이름은 {0}입니다. 나이는 {1}입니다.{4}{3}{2}'.format(name, age, 'a', 'b', 'c'))
'''

zipcode = "06236"
print('우편번호: {}'.format(zipcode))

address = '''서울 강남구
테헤란노 146'''
print('주소: {addr}'.format(addr=address))

tel1, tel2, tel3 = ('02', '123', '4567') #구조분해할당
print('연락처: {0}-{1}-{2}'.format(tel1, tel2, tel3))


