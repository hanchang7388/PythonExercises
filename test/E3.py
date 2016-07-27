#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
for i in range(10000):
    a= math.sqrt(i+100)
    b= math.sqrt(i+268)
    #print a,b,
    if a%1==0 and b%1==0:
        print i