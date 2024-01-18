# num = '951211-1234567'

while True:
    p = input("하이픈을 포함하여 전체 주민번호를 입력하세요 >>> ")
    if p.find('-') != 6:
        print("하이픈의 위치가 잘못되었습니다.")
        continue
    birthday = p.split('-')[0]
    print(f'생년월일은 {birthday}입니다.')
    break