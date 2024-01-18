from my_secure import *
# import my_secure

def secure_phone(phone):
    # 010-1111-1111 => 010-****-1111
    return phone[:4]+'****'+phone[-5:]

print(secure_name("김철수")) # 김**
print(secure_phone("010-1111-1111"))