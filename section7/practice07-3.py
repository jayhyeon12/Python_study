basket = []
num = int(input("몇 개의 과일을 보관할까요? >>> "))
for i in range(num):
    basket.append(input(f"{i+1}번째 과일을 입력하세요 >>> "))
print(f"입력받은 과일들은 {basket}입니다.")