#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
def match(a):
    if re.match(r'(\w+)@(\w+).(\w+)',a):
        print "yes"
    else:
        print "fail"




# a=raw_input("enter email: ")
a="123@qq.com"
print a
match(a)
print 'a b  cd'.split(' ')