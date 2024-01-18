# 유효한(사용가능한) 비밀번호 체크하는 프로그램!
# 영문, 숫자 조합된 경우 : OK!
pwd = input("비밀번호를 입력하세요 >>> ")

ch_count = 0
num_count = 0

for ch in pwd:
    if ch.isalpha():
        ch_count += 1
    if ch.isnumeric():
        num_count += 1

if ch_count > 0 and num_count > 0:
    print("사용 가능한 비밀번호입니다.")
else:
    print("사용할 수 없는 비밀번호입니다.")
