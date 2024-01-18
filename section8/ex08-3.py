# while True:
#     print("코드1")
#     continue
#     print("코드2")

fruits = ['사과', '감귤']
count = 3

while count > 0:
    fruit = input("어떤 과일을 저장할까요? >>> ")
    if fruit in fruits:
        print("동일한 과일이 있습니다.")
        continue
    fruits.append(fruit)
    count -= 1
    print(f'입력이 {count}번 남았습니다.')

print(f"5개 과일은 {fruits}입니다.")