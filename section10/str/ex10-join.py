s = '#'
print(s.join('python')) # p#y#t#h#o#n

lst = ['a', 'b', 'c']
print(s.join(lst)) # a#b#c

s = " best! "
lst = ['python', 'world', '!']
print(s.join(lst))

dict = {'a': 'apple', 'b': 'banana'}
print(''.join(dict)) # ab
print('-'.join(dict)) # a-b
print('-'.join(dict.values())) # apple-banana
