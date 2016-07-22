# -*- coding: utf-8 -*-
kaixindai=['sxd','spd','kxb']
for k in kaixindai:
    print k,
print '\n'+kaixindai[-1]+'\n'
kaixindai.append('yinxinhui')
for k in kaixindai:
    print k,
shangpiaodai=['shangpiao1','shangpiao2']
kaixindai[1]=shangpiaodai
print
for i in kaixindai:
    print i,
print len(kaixindai)
#tuple
t=()
print t
t1=(1)
print t1
t2=(1,)
print t2
t3=(1,2)
print t3