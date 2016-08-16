#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib, urllib2
import cookielib
import re
import time
import random
import codecs


class Login(object):
    def __init__(self, id, semester):
        # print "Initialing : ..."
        self.stuid = str(id)
        self.semester = semester
        self.url = 'http://xk.urp.seu.edu.cn/jw_service/service/stuCurriculum.action'
        self.referer = 'http://xk.urp.seu.edu.cn/jw_service/service/lookCurriculum.action'
        self.cookies = cookielib.CookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookies))
        self.opener.open(self.referer)

        self.data = {'queryStudentId': self.stuid, 'queryAcademicYear': self.semester}
        self.post_data = urllib.urlencode(self.data)
        # headers
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
        self.request = urllib2.Request(self.url, self.post_data, self.header)

        self.outfile = codecs.open("2016.txt", 'a+', 'utf-8')
        # self.outfile.write(u'一卡通号\t学号\t姓名\t\t院系\t\t\t专业\n')
        self.item = []

        for j in range(5):
            try:
                # print "The ", j+1, " times try"
                self.response = self.opener.open(self.request)
                # for item in self.cookies:
                #     print item.name, ' = ', item.value
                break
            except urllib2.URLError, e:
                print "in the except block"
                print e.args, e.reason
                print "wait for about 10 seconds"
                time.sleep(random.uniform(8, 15))
                pass

    def find(self, pattern, text):
        pat = re.compile(pattern, re.U)
        match = pat.search(text)
        if match:
            return match.group(1)
        else:
            return False

    def get_info(self):
        # build re
        # pattern = re.compile(r'<td.*?width="20%".*?align="left">(.*?)</td>', re.S)

        page = self.response.read().decode('utf-8')
        if self.find(ur'(没有找到该学生信息)', page):
            return "Sorry, Card_No.", self.stuid, " student does not exist"
        elif page:
            pass
        else:
            return "no data"
        card = self.find(ur'一卡通号:(\d+)', page)
        student_id = self.find(ur'学号:(\w+)', page)
        name = self.find(ur'姓名:(\w+)', page)
        college = self.find(ur'院系:\[\w+\](\w+)', page)
        major = self.find(ur'专业:\[\w+\](\w+)', page)

        print card, student_id, name, college, major

        # u'一卡通号\t学号\t姓名\t\t院系\t\t\t专业'
        self.outfile.write(u'%10s%10s%10s%10s%10s\n' % (card, student_id, name, college, major))
        self.outfile.close()

if __name__ == '__main__':
    codecs.open("2016.txt", 'w', 'utf-8').write(u'%10s%10s%15s%15s%15s\n' % ('card_id', 'stu_id', 'name', 'college', 'major'))
    for i in range(213160001,213163968):
        sem = '16-17-1'
        log = Login(i, sem)
        log.get_info()
        del log
        # time.sleep(random.uniform(20,25))
