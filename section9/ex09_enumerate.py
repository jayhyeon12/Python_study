kim1 = ["가위", "바위", "보"]
kim2 = ["보", "가위", "바위"]

'''
for i, v in enumerate(kim1):
    print(f"일남 : {v} vs 이남: {kim2[i]}")
'''

for i in range(len(kim1)):
    print(f"일남 : {kim1[i]} vs 이남: {kim2[i]}")