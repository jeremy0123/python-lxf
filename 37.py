# -*- coding: utf-8 -*-

f = open('/home/ww/python/python-lxf/test.txt', 'r')
print f.read()
f.close()

try:
    f = open('/home/ww/python/python-lxf/test.txt', 'r')
    str = f.read()
    print len(str)
    print str
finally:
    if f:
        f.close()

# with 自动调用close()方法
with open('/home/ww/python/python-lxf/test.txt', 'r') as f:
    print f.read()

with open('/home/ww/python/python-lxf/test.txt', 'r') as f:
    for line in f.readlines(): # 读入一行
        print(line.strip()) # 把末尾的'\n'删掉

# file-like Object
# file-like Object不要求从特定类继承，只要写个read()方法就行。
# StringIO就是在内存中创建的file-like Object，常用作临时缓冲。

with open('/home/ww/python/python-lxf/test.txt', 'rb') as f:
    print f.read() # 读取二进制文件

#import codecs # 转码
#with codecs.open('/home/ww/python/python-lxf/test.txt', 'r', 'gbk') as f:
#    print f.read()

f = open('/home/ww/python/python-lxf/test.txt', 'w')
f.write('hello world!\n')
f.write('测试中文\n')
f.close()
