#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
print os.getcwd()

fo = open("111.txt","wb")
fo.write("hello\nthis is the first word writen in the file \n");
print fo.tell()

fo.close()
print fo.name,fo.closed,fo.mode

fo=open("111.txt","r+")
print fo.read(7)
fo.close()
