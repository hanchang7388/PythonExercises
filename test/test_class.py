#!/usr/bin/env python
#-*- coding: utf-8 -*-
# class human:
class grandpa(object):
    def hair(self):
        print "1 hair"

class grandma(object):
    def hair(self):
        print "2 hair"

class mother(grandma):
    pass

class father(grandpa):
    def hair(self):
        print "father hair"

class son(mother,father):
    pass

tom=son()
tom.hair()
print son.__mro__
