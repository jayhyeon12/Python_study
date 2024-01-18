'''
123-45-67890
전체 글자수?
하이픈의 위치?
하이픈 제거 후 숫자인지?
'''
no = input('사업자등록번호를 입력하세요 >>> ')

case1 = no.find('-') == 3
# case2 = no.find('-', 4) == 6
case2 = no.rfind('-') == 6
case3 = len(no) == 12
case4 = no.replace('-', '').isdecimal()

if case1 and case2 and case3 and case4:
    print("올바른 형식입니다.")
else:
    print("올바른 형식이 아닙니다.")