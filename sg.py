# -*- coding:utf-8 -*-

import sys
from urllib import urlencode
import cookielib, urllib2,urllib,re

class ElearningHacker:


    def login(self):
        try:    
            user_agents = ['Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0']    
            req_header = {'User-Agent':user_agents}
            mycookie = urllib2.HTTPCookieProcessor(cookielib.CookieJar())
            openner = urllib2.build_opener(mycookie)
            urllib2.install_opener(openner);
            loginUrl = 'http://61.177.60.86:8000/elearning/login.do?method=login&seq=1'
            hosturl = 'http://61.177.60.86:8000/elearning/'
            host = urllib2.urlopen(hosturl)
            user_data = {'userLoginName': '10033335','userLoginPassword': '860920'}
            postData = urllib.urlencode(user_data)
            request = urllib2.Request(loginUrl,postData)
            request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0')
            request.add_header('Content-Type', 'application/x-www-form-urlencoded')
            request.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
            request.add_header('request','http://61.177.60.86:8000/elearning/')
            response = urllib2.urlopen(request)
            print "login Success"
        except Exception,e:
            print 'login error %s' %e

    def getScore(self,targetUrl):
        #这个方法会把所有可以学习的课程先进行申请学习，然后结束学习
        print "Wait a moment , amazing happen..."
        request = urllib2.Request(targetUrl)
        response = urllib2.urlopen(request)
        html = response.read()
        reg = r'href=\"javascript\:entoStudy\((.*),\'1\''
        imgre = re.compile(reg)
        imglist = re.findall(imgre,html)
        for imgurl in imglist:
            courseId = imgurl.split(',')[0].strip('\'')
            assignId = imgurl.split(',')[1].strip('\'')
            entoStudyUrl = 'http://61.177.60.86:8000/elearning/stuMyStudy.do?method=entoStudy&courseId='+courseId+'&assignId='+assignId+'&type=3&cate=1'
            request = urllib2.Request(entoStudyUrl)
            response = urllib2.urlopen(request)
        #结束学习
        tobeFinishUrl = 'http://61.177.60.86:8000/elearning/stuMyStudy.do?method=stuMyStudy&type=studying&page=1&pageSize=100'
        request_fin = urllib2.Request(tobeFinishUrl)
        response_fin = urllib2.urlopen(request_fin)
        html_fin = response_fin.read()
        reg_fin= r'href=\"javascript\:toStudy\(.*,(.*)\)'
        re_fin = re.compile(reg_fin)
        finList = re.findall(re_fin,html_fin)
        print 'The number of total coureses is %d' %len(finList)
        for finUrl in finList:
            finId = finUrl.strip('\'')
            scoreUrl = 'http://61.177.60.86:8000/elearning/stuCoursestudyExt.do?method=completeStudy&id='+finId
            print 'Finish learning %s' %scoreUrl
            request_score = urllib2.Request(scoreUrl)
            response_score = urllib2.urlopen(request_score)
    print 'Done!'

dh = ElearningHacker()
dh.login()
dh.getScore('http://61.177.60.86:8000/elearning/stuMyStudy.do?method=publicCourse')
