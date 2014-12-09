# -*- coding:utf-8 -*-
# 线程锁

import time, threading

balance = 0
lock = threading.Lock()

def change_it(n):
    global balance # !!!
    balance = balance + n # 存钱
    balance = balance - n # 取钱

def run_thread(n):
    for i in range(100000):
        lock.acquire()
        try :
            change_it(n)
        finally:
            lock.release()

t1 = threading.Thread(target=run_thread, args=(5, ))
t2 = threading.Thread(target=run_thread, args=(8, ))
t1.start()
t2.start()
t1.join()
t2.join()
print balance # 不一定为0

# 获得锁的线程用完后一定要释放锁，否则那些苦苦等待锁的线程将永远等待下去，
# 成为死线程。所以我们用try...finally来确保锁一定会被释放。
