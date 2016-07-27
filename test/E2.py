#!/usr/bin/env python
# -*- coding: utf-8 -*-
profit=int(raw_input("Profit = "))
pro = [1000000,600000,400000,200000,100000, 0]
rate = [0.01 , 0.015 , 0.03 , 0.05 , 0.075 , 0.10]
bonus = 0
for i in range(0,6):
    if profit>pro[i]:
        bonus+=(profit-pro[i])*rate[i]
        profit=pro[i]

print bonus