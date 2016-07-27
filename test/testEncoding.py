#!/usr/bin/env python
# -*- coding: utf-8 -*-

a = "abc"
b = 'abc'
c = 333
d = 3.333
print a
print b

print ord('a')

print u'中文正常'
print u'中文正常'
print len(u'中文正常')
print len(u'abc123')


print 'hello %s' %a
print 'hello %04d' %c
print 'hello %d' %d
print 'hello %.2f' %d
print 'hello %%'