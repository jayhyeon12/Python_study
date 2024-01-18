# a_list = ['above', 'cookie', 'app', 'about', 'admin', 'bisket', 'apple', 'april']

# a_list = ['aaa', 'bbb', 'ccc', 'ddd']
a_list = ['above', 'cookie', 'app', 'about', 'admin', 'bisket', 'apple', 'april']
new_list = []

while a_list:
    item = a_list.pop(0)
    if item.find('a') != -1:
        new_list.append(item)
    else:
        print(f'{item} 제거됩니다.')

print(new_list)
