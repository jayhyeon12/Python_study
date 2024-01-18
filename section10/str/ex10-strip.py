s = ' apple '

print(s == 'apple') # False
print(s.strip() == 'apple') # True


print(s.lstrip())
print(s.lstrip() == 'apple') # False

print(s.rstrip())
print(s.rstrip() == 'apple') # False

# 메소드 체이닝
print(s.rstrip().lstrip() == 'apple') # True