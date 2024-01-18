file = open('./section13/sample.txt', 'r')
# read()
# readline()
# readlines()
# str = file.read()
# print(str)

# while True:
#     str = file.readline()
#     if str == '':
#         break
#     print(str, end='')

line_list = file.readlines()
print(line_list)