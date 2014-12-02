# -*-coding: utf8 -*-

# 循环
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print name

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print sum

# range()
sum = 0
for x in range(101): # range(101) 0-100
    sum = sum + x
print sum

# while 循环
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print sum

# int()
birth = int(raw_input('birth: ')) #int() 当输入非数字时会报错
if birth > 2000:
    print '00后'
else:
    print '00前'
