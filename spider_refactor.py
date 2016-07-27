#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib,urllib2
import cookielib
import re
import time
import random

class Login(object):
    def __init__(self, id, semester):
        print "Initialing : ..."
        self.stuid = str(id)
        self.semester = semester
        self.url = 'http://xk.urp.seu.edu.cn/jw_service/service/stuCurriculum.action'
        self.referer = 'http://xk.urp.seu.edu.cn/jw_service/service/lookCurriculum.action'
        self.cookies = cookielib.CookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookies))
        self.opener.open(self.referer)

        self.data = {'queryStudentId':self.stuid,'queryAcademicYear':self.semester}
        self.post_data = urllib.urlencode(self.data)
        # output cookies for check
        # print self.cookies

        # self.header = {
        #     'Host': 'xk.urp.seu.edu.cn',
        #     'Connection': 'keep-alive',
        #     'Content-Length':'60',
        #     'Cache-Control': 'max-age=0',
        #     'Origin': 'http://xk.urp.seu.edu.cn',
        #     'Upgrade-Insecure-Requests': '1',
        #     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36',
        #     'Referer': 'http://xk.urp.seu.edu.cn/jw_service/service/lookCurriculum.action',
        #     'Content-Type': 'application/x-www-form-urlencoded',
        #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        #     'Accept-Encoding': 'gzip, deflate',
        #     'Accept-Language': 'zh-CN,zh;q=0.8'
        #     }
        self.header = {
            'Host': 'xk.urp.seu.edu.cn',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cache-Control': 'max-age=0',
            'Origin': 'http://xk.urp.seu.edu.cn',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) Chrome/51.0.2704.106',
            'Referer': 'http://xk.urp.seu.edu.cn/jw_service/service/lookCurriculum.action',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
            }
        self.request = urllib2.Request(self.url,self.post_data,self.header)

        # self.response = self.opener.open(self.request)
        for j in range(5):
            try:
                print "The ", j+1, " times try"
                self.response = self.opener.open(self.request)
                for item in self.cookies:
                    print item.name,' = ',item.value
                break
            except urllib2.URLError, e:
                print "in the except block"
                print e.code,e.reason
                time.sleep(random.uniform(8,15))
                print "wait for 10 seconds"
                pass
        # try:
        #     self.response = self.opener.open(self.request)
        #     pass
        # except urllib2.URLError, e:
        #     if hasattr(e, "code"):
        #         print e.code
        #     if hasattr(e, "reason"):
        #         print e.reason
        # except Exception, e:
        #     print Exception, ":", e

    def get_info(self):
        page = self.response.read().decode('utf-8')
        pattern = re.compile(r'<td.*?width="20%".*?align="left">(.*?)</td>', re.S)

        if page:
            pass
        else:
            return "No.", self.stuid, " student does not exist"

        print "Result:"
        items = re.findall(pattern, page)
        if items:
            for item in items:
                print item

            return None
        else:
            return "No data"

if __name__ == '__main__':
    for i in range(213140001,213143999):
        semester='16-17-1'
        log = Login(i,semester)
        log.get_info()
        del log
        time.sleep(random.uniform(20,25))
