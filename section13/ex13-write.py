file = open('hello.txt', 'wt', encoding='utf-8')

file.write("안녕하세요. ^^")
# file.write("Hi!")
file.close() # 메모리 누수 현상 막기 위함