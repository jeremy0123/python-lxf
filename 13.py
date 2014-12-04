# -*- coding: utf-8 -*-

# 切片 slice
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print L[0:3] # [0 - 3)
print L[3:] # [3 - end]
print L[:3] # [begin, 3)
print L[-2:] # [-2 - end]

L = range(100)
print L
print L[:10]
print L[10:20]
print L[-10:]
print L[:10:2] # 前10个数，每2个取一个
print L[::5] # 所有数，每5个取一个
print L[:] # 取所有的数

# tuple 和 string 都可以看做list，进行切片操作
