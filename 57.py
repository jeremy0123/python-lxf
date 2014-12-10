# -*- coding: utf-8 -*-

# 因为互联网协议包含了上百种协议标准，但是最重要的两个协议是TCP和IP协议，
# 所以，大家把互联网的协议简称TCP/IP协议。

import socket

# AF_INET指定使用IPv4协议，如果要用更先进的IPv6，就指定为AF_INET6。SOCK_STREAM指定使用面向流的TCP协议
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 注意参数是一个tuple，包含地址和端口号。
s.connect(('www.sina.com.cn', 80))
# 发送数据
s.send('GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

buffer = []
while True:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break

data = ''.join(buffer)
print len(data)

s.close()

header, html = data.split('\r\n\r\n', 1)
print header
with open('/home/ww/python/python-lxf/sina.html', 'wb') as f:
    f.write(html)
