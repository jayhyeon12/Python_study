money = 10000
price = 3000
'''
result = divmod(money, price)
print(f"빵을 {result[0]}개 사고 {result[1]}원이 남았습니다.")
'''
bread, change = divmod(money, price) # 구조분해할당, 언패킹
print(f"빵을 {bread}개 사고 {change}원이 남았습니다.")