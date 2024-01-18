def charge(energy):
    total = 0
    count = 0
    while True:
        total += energy[count]
        count += 1
        if total > 10:
            return
            # break
        print(f'에너지가 {total} 충전되었습니다.')

charge(range(1, 11))