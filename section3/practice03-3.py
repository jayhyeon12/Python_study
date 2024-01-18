# dict
'영어 단어를 입력하세요 >>> '
'flower: 꽃'
eng_dict = {
    'flower': '꽃',
    'fly': '날다',
    'floor': '바닥'
}
# 1. 사용자로 부터 영단어 입력 받기
word = input('영어 단어를 입력하세요 >>> ')
# 2. 출력하기
print(f"{word}:{eng_dict[word]}")