# with open("C:\\Users\\ITPS\\Desktop\\python1\\section13\\풀꽃.txt", 'r', encoding="utf-8") as f:
# with open("C:/Users/ITPS/Desktop/python1/section13/풀꽃.txt", 'r', encoding="utf-8") as f:
#     line_list = f.readlines()
with open(r"C:\Users\ITPS\Desktop\python1\section13\풀꽃.txt", 'r', encoding="utf-8") as f:
    line_list = f.readlines()

    count = 0
    word = "보아야"
    for line in line_list:
        if word in line:
            count += 1
    
    print(f'{word}는 전체 {count}번 나타납니다.')