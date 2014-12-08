# -*- coding:utf-8 -*-
# 操作文件和目录
import os
print os.name # 操作系统名字
print os.uname() # 系统信息 Windows上无此接口

print os.environ # 操作系统环境变量，定义为dict
print '----'
print os.getenv('PATH') # 某个变量

# 操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中
print os.path.abspath('.')

# os.path.join()返回的字符串 区别操作系统的路径分隔符
os.mkdir(os.path.join('/home/ww', 'testdir'))
os.rmdir(os.path.join('/home/ww', 'testdir'))

print os.path.split('/home/ww/python/python-lxf/test.txt') # 分隔最后一个文件
print os.path.splitext('/home/ww/python/python-lxf/test.txt') # 分隔扩展名

os.rename('/home/ww/python/python-lxf/test.txt', '/home/ww/python/python-lxf/test.txt1') #改名
os.rename('/home/ww/python/python-lxf/test.txt1', '/home/ww/python/python-lxf/test.txt')

# os.remove('/home/ww/python/python-lxf/test.txt1') # 删除

# shutil 是 os的补充 shutil.copyfile()

print '----'
# 列出目录
print [x for x in os.listdir('.') if os.path.isdir(x)]
