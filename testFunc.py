# -*- coding: utf-8 -*-

#可变参数
def calculate(*numbers):
    sum=0
    for n in numbers:
        sum = sum + n * n
    return sum
print calculate(1,2,3)

#关键字参数
def person(name,age, **other):
    print 'name:',name,'age:',age,'other:',other
person('gilly',23,city='citydown',job='dragon')

#递归
#实现n!
def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)

#print factorial(int(raw_input()))


d = {'a': 1, 'b': 2, 'c': 3}
for k,v in d.iteritems():
    print k,v