#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
import urllib2
import cookielib

url = 'http://xk.urp.seu.edu.cn/jw_service/service/stuCurriculum.action'
# request = urllib2.Request(url,data,headers)

stuid='71113333'
values = {'queryStudentId':stuid,'queryAcademicYear':'16-17-1'}
data = urllib.urlencode(values)

cookies = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookies))
request= urllib2.Request(url,data)
response = opener.open(request)

for item in cookies:
    print item.name,' = ',item.value

print response.read()




