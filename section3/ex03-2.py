# 함수에 넣는 값(인풋값) == "인수", "argument"
# print("hello", "python", sep="\n")
# print("hello", end="!")
# print("python", end="\n")
# print("hello")
# print("python")
# print("hello", "python", sep=" ", end="!\n")
# print("hello", "python", sep=" ", end="!")

# file
# fos = open('sample.py', mode='wt') # wt = write text
# fos = open('sample.py', 'wt') # wt = write text
# import sys
fos = open('sample.py', 'w') # wt = write text

# print('print("Hello Python!")', file=sys.stdout)
print('print("Hello Python!")', file=fos)