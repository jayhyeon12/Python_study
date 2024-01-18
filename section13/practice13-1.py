nation = ['그리스', '아테네', '독일', '베들린', '러시아', '모스크바', '미국', '워싱턴']

file_name = 'nation.txt'

file = open(file_name, 'w', encoding='utf-8')
for i in range(0, len(nation), 2):
    file.write(f'{nation[i]}-{nation[i+1]}\n')
file.close()

print(f"생성된 {file_name} 파일의 내용은 다음과 같습니다.")

with open(file_name, 'r', encoding='utf-8') as f:
    line_list = f.readlines()
    for line in line_list:
        print(line, end='')
        