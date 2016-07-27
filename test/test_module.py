#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

print __name__


if len(sys.argv)>1:
    print "parameters : ",sys.argv[1:]
elif len(sys.argv)==1:
    print "no parameters."
