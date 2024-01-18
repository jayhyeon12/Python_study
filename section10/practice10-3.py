'''
"김철수",85
이름은 김철수이고, 점수는 85점입니다.
'''
student = '"김철수",85'
# name = student.split(',')[0].strip('"')
# score = student.split(',')[1]
name, score = student.split(',')
name = name.strip('"')
print(f"이름은 {name}이고, 점수는 {score}점입니다.")