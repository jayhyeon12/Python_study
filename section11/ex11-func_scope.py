# 변수의 사용 범위(scope)
# 전역(global)
num = 1 # 전역 변수

def outer_function():
    # 지역(local)
    # global num
    num = 2 # 지역 변수

    def inner_function():
        # 지역(local)
        nonlocal num
        num = 3
        print(num)
    
    inner_function()
    print(num)

outer_function()
print(num)

