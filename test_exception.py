#!/usr/bin/env python
# -*- coding: utf-8 -*-


def func(number):
    if number>1:
        raise Exception("IIIIInvalid number",number)
        print "never run"

a=int(raw_input("pls input"))
func(a)