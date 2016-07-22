#!/usr/bin/env python
# -*- coding: utf-8 -*-

xl=[1,2,3]
yl=[4,5,6]

print zip(xl,yl)
print sum(x*y for x,y in zip(xl,yl))