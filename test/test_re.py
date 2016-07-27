#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
def match(a):
    pattern = re.compile(r'(\w+)@(\w+).(\w+)')
    m=re.match(pattern,a)


    if re.match(pattern,a):
        print "yes"
    else:
        print "fail"


# a=raw_input("enter email: ")
a="123@qq.com"
print a
match(a)
# print 'a b  cd'.split(' ')