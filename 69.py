# -*- coding: utf-8 -*-
# gevent是第三方库，通过greenlet实现协程，其基本思想是：
# 当一个greenlet遇到IO操作时，比如访问网络，就自动切换到其他的greenlet，等到IO操
# 作完成，再在适当的时候切换回来继续执行。由于IO操作非常耗时，经常使程序处于等待状
# 态，有了gevent为我们自动切换协程，就保证总有greenlet在运行，而不是等待IO。

from gevent import monkey; monkey.patch_socket()
import gevent

def f(n):
    for i in range(n):
        print gevent.getcurrent(), i
        gevent.sleep(0)

g1 = gevent.spawn(f, 500000)
g2 = gevent.spawn(f, 500000)
g3 = gevent.spawn(f, 500000)
g1.join()
g2.join()
g3.join()
