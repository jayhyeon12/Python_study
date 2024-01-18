age = int(input("몇 살입니까? >>> "))
if age >= 20:
    print("성인")
if age >= 17 and age < 20:
    print("고등학생")
if age >= 14 and age < 17:
    print("중학생")
if age >= 8 and age < 14:
    print("초등학생")
if age < 8:
    print("미취학")