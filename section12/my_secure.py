def secure_name(name):
    # 김일남 => 김**
    return name[0] + '**'

def secure_no(no):
    # 500101-1234567 => 500101-1******
    return no[:8] + '******'

def secure_phone(phone):
    # 010-1111-1111 => 010-****-1111
    return phone.replace(phone[4:8], '****')
