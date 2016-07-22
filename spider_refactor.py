#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib,urllib2
import cookielib
import re
class Login(object):
    def __init__(self):
        print "Initialing : ..."
        self.sid = ''

    def get_cookie(self):
        self.cookies = cookielib.CookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookies))
        self.opener.open('http://xk.urp.seu.edu.cn/jw_service/service/lookCurriculum.action')
        for item in self.cookies:
            print item.name,' = ',item.value
        return None

    def get_sid(self):
        # print "self.sid : ",self.sid
        header = {
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','Accept-Encoding':'gzip, deflate',
            'Accept-Language':'zh-CN,zh;q=0.8',
            'Cache-Control':'max-age=0',
            'Connection':'keep-alive',
            'Content-Length':'60',
            'Content-Type':'application/x-www-form-urlencoded',
            'Cookie':self.sid,
            'Host':'xk.urp.seu.edu.cn',
            'Origin':'http://xk.urp.seu.edu.cn',
            'Referer':'http://xk.urp.seu.edu.cn/jw_service/service/lookCurriculum.action',
            'Upgrade-Insecure-Requests':'1',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36'
         }

       #post data
        data = {
            'queryStudentId':'71113317',
            'queryAcademicYear':'16-17-1'
        }
        post_data=urllib.urlencode(data)
        post_url='http://xk.urp.seu.edu.cn/jw_service/service/lookCurriculum.action'

        request = urllib2.Request(post_url,post_data,header)

        response = self.opener.open(request)
        string = str(response.geturl())
        self.sid=string[string.find(r'sid=')+4:]
        print response.read()
        # return self.sid
        return None

if __name__ == '__main__':
    log=Login()
    log.get_cookie()

    # print log.get_sid()
    log.get_sid()