#!/usr/bin/env python
# -*- coding: utf-8 -*-
# class P1():
#     def foo(self):
#         print 'p1-foo'
#
# class P2():
#     def foo(self):
#         print 'p2-foo'
#     def bar(self):
#         print 'p2-bar'
#
# class C1(P1,P2):
#     pass
#
# class C2(P1,P2):
#     def bar(self):
#         print 'C2-bar'
#
# class D(C1,C2):
#     pass
#
#
# if __name__ =='__main__':
#     d=D()
#     d.foo()
#     d.bar()
#
#
class P1(object):
    def foo(self):
        print 'p1-foo'
    def bar(self):
        print 'p1-bar'


class P2(object):
    def foo(self):
        print 'p2-foo'
    def bar(self):
        print 'p2-bar'

class C1(P1,P2):
    pass

class C2(P1,P2):
    def bar(self):
        print 'C2-bar'

class D(C1,C2):
    pass


if __name__ =='__main__':
    print D.__mro__   #只有新式类有__mro__属性，告诉查找顺序是怎样的
    d=D()
    d.foo()
    d.bar()