#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import sys
import os


def restart_program():
    # get compile path
    # like:  >>> sys.executable
    #         'C:\\Python27\\python.exe'
    python = sys.executable

    # an os interface to replace the current process, pid dont get changed
    os.execl(python, python, * sys.argv)

if __name__ == "__main__":
    print 'start...'
#  answer = raw_input("Do you want to restart this program ? ")
#  if answer.strip() in "y Y yes Yes YES".split():
#    restart_program()
    print u"1秒后,程序将结束并重启..."#.encode("utf-8")
    time.sleep(1)
    restart_program()