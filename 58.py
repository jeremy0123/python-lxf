# -*-coding: utf-8 -*-

# tcp Server
import socket, threading, time

def tcplink(sock, addr):
    print 'Accept new connection from %s:%s' % addr
    sock.send('Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if data == 'exit' or not data:
            break
        sock.send('Hello, %s!' % data)

    sock.close()
    print 'Connection from %s:%s closed.' % addr

# 服务器进程首先要绑定一个端口并监听来自其他客户端的连接。
# 每个连接都需要一个新的进程或者新的线程来处理，否则，服务器一次就只能服务一个客户端了。

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 9999))
# 调用listen()方法开始监听端口，传入的参数指定等待连接的最大数量
s.listen(5)
print 'Waiting for connection'

while True:
    sock, addr = s.accept()
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
