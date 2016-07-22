#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
import urllib2
import cookielib
import re
# reponse = urllib2.urlopen('http://xk.urp.seu.edu.cn/jw_service/service/lookCurriculum.action')

# request = urllib2.Request('http://xk.urp.seu.edu.cn/jw_service/service/lookCurriculum.action')
# response = urllib2.urlopen(request)

values = {'queryStudentId':'71113316','queryAcademicYear':'16-17-1'}
data = urllib.urlencode(values)

user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36'
header = {
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','Accept-Encoding':'gzip, deflate',
            'Accept-Language':'zh-CN,zh;q=0.8',
            'Cache-Control':'max-age=0',
            'Connection':'keep-alive',
            'Content-Length':'60',
            'Content-Type':'application/x-www-form-urlencoded',
            'Cookie':'sto-id-20480-sg-xk.urp.seu.edu.cn=APIAEBAKFAAA; JSESSIONID=0000wyzKyebXErIr9BQWe6Zb5e5:19tf509hs',
            'Host':'xk.urp.seu.edu.cn',
            'Origin':'http://xk.urp.seu.edu.cn',
            'Referer':'http://xk.urp.seu.edu.cn/jw_service/service/lookCurriculum.action',
            'Upgrade-Insecure-Requests':'1',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36'
         }


cookies = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookies))

url = 'http://xk.urp.seu.edu.cn/jw_service/service/lookCurriculum.action'
request = urllib2.Request(url,data,header)
print request
response = opener.open(request)
print response.read()