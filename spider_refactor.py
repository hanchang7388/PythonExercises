#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib,urllib2
import cookielib
import re

class Login(object):
    def __init__(self, id , semester):
        print "Initialing : ..."
        self.stuid = id
        self.semester=semester
        self.url='http://xk.urp.seu.edu.cn/jw_service/service/stuCurriculum.action'
        self.cookies = cookielib.CookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookies))
        for item in self.cookies:
            print item.name,' = ',item.value

    def get_info(self):
        #post data
        data = {'queryStudentId':self.stuid,'queryAcademicYear':self.semester}
        post_data=urllib.urlencode(data)
        request = urllib2.Request(self.url,post_data)

        response = self.opener.open(request)



        string = str(response.geturl())

        page = response.read().decode('utf-8')
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

    for i in range(71113101,71113499):
        semester='16-17-1'
        i=str(i)
        # if isinstance(i,str):
        #     print 1
        # else:
        #     print 0
        log=Login(i,semester)
        log.get_info()