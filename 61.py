# -*-coding: utf-8 -*-

# UDP client
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in ['Machael', 'Tracy', 'Sarah']:
    s.sendto(data, ('127.0.0.1', 9999))
    print s.recv(1024)
s.close()

# UDP的使用与TCP类似，但是不需要建立连接
