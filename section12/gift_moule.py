total = 0

def gift(dic, who, money):
    dic[who] = money
    global total
    total = total + money
    # total += money

wedding = {"김일남": 1000}