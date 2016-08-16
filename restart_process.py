#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import sys
import os

num = 0

def restart_program():
    # get compile path
    # like:  >>> sys.executable
    #         'C:\\Python27\\python.exe'
    python = sys.executable
    print sys.argv
    # an os interface to replace the current process, pid dont get changed
    os.execl(python, python, * sys.argv)
    print 'restart...pid:', os.getpid()

if __name__ == "__main__":
    print 'start...pid:', os.getpid()
    num += 1
    print num
#  answer = raw_input("Do you want to restart this program ? ")
#  if answer.strip() in "y Y yes Yes YES".split():
#    restart_program()
    print u"1秒后,程序将结束并重启..."#.encode("utf-8")
    time.sleep(1)
    restart_program()
    # print 'restart...pid:', os.getpid()