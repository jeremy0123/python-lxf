# -*- coding: utf-8 -*-

# 进程 -- Unix/Linux

# Unix/Linux操作系统提供了一个fork()系统调用，子进程永远返回0，而父进程返回子进程的ID
# 父进程要记下每个子进程的ID，而子进程只需要调用getppid()就可以拿到父进程的ID

import os

print 'Progress (%s) start ...' % os.getpid()
pid = os.fork()

if pid == 0:
    print 'I am child progress (%s) and my parent is %s.' % (os.getpid(), os.getppid())
else:
    print 'I (%s) just created a child progress (%s).' % (os.getpid(), pid)
