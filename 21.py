# -*- coding: utf-8 -*-

import Image
im = Image.open('test.png')
print im.format, im.size, im.mode
im.thumbnail((200, 100)) # yum install zlib-devel
im.save('thumb.jpg', 'JPEG') # yum install libjpeg-devel

# Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，搜索路径存放在sys模块的path变量中
import sys
print sys.path
# sys.path.append('/Users/michael/my_py_scripts') # 模块搜索路径的增加
# 或设置环境变量PYTHONPATH
