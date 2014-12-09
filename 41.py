# -*- coding: utf-8 -*-

# 跨平台多进程接口

# multiprocessing模块就是跨平台版本的多进程模块
from multiprocessing import Process
import os

def run_proc(name):
    print 'Run child process %s (%s)...' % (name, os.getpid())

if __name__ == '__main__':
    print 'Parent process %s.' % os.getpid()
    p = Process(target=run_proc, args=('test', ))
    print 'Progress will start.'
    p.start()
    p.join() # join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
    print 'Process end.'
