# -*- coding:utf-8 -*-

#---------------------------------------  
#   程序：知乎文章爬虫
#   版本：0.1  
#   作者：Will  
#   日期：2014-07-24  
#   语言：Python 2.7  
#   功能：将某个作者的文章全部爬下来并email到evernote
#---------------------------------------  
import urllib
import re
import datetime
import time
import urllib2  
import random
import cookielib
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def sendEmailSmtplib():
    #邮件发送模块
    fromaddr = "dhtcwd@163.com" #填写发送email地址
    toaddrs  = "dhtcwd@qq.com" #填写接受email地址
    username = "dhtcwd"
    password = "xiaoling860920"
    server = smtplib.SMTP('smtp.163.com')#class smtplib.SMTP([host[, port[, local_hostname[, timeout]]]])
    server.login(username,password)#SMTP.login(user, password)
    server.set_debuglevel(1)
    #msg是一个字符串，其格式是smtp协议规定的。复杂的邮件可以使用email模块来完成
    title = "test"
    msgHead = ['From: %s\r\nTo: %s\r\nSubject: %s' % (fromaddr,toaddrs,title)]
    msgBody = ['this is for u']
    msg = '\r\n\r\n'.join(['\r\n'.join(msgHead),'\r\n'.join(msgBody)])
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()

def sendEmailEmail(html):
    fromaddr = "dhtcwd@163.com" #填写发送email地址
    toaddrs  = "dhtcwd@qq.com" #填写接受email地址
    username = "dhtcwd"
    password = "xiaoling860920"
    msg = MIMEMultipart("alternative")
    msg['Subject'] = "test of the email"
    msg['From'] = fromaddr
    msg['To'] = toaddrs
    server = smtplib.SMTP('smtp.163.com')#class smtplib.SMTP([host[, port[, local_hostname[, timeout]]]])
    server.login(username,password)#SMTP.login(user, password)
    server.set_debuglevel(1)
    server.sendmail(fromaddr, toaddrs, msg.as_string())
    server.quit()
    
def getHtml(url):
    user_agents = [
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 ",
    ]    
    agent = random.choice(user_agents)
    req_header = {'User-Agent':agent}
    mycookie = urllib2.HTTPCookieProcessor(cookielib.CookieJar())
    openner = urllib2.build_opener(mycookie)
    request = urllib2.Request(url,None,req_header)
    response = urllib2.urlopen(request)
    html = response.read()
    return html

    
def getAnswerHtml(html):
#<div class=" zm-editable-content clearfix"></div>
    reg = r'<div class=\" zm-editable-content clearfix\">.*</div>'
    answerRe = re.compile(reg)
    answerList = re.findall(answerRe,html)
    print answerList
    for a in answerList:
        print a
    
userName = raw_input('please enter the userName: ')
index = int(raw_input('please enter the index: '))
for x in range(1,index+1):
    answerUrl = "http://www.zhihu.com/people/"+userName+"/answers?page=%d" % x
    html_page = getHtml(answerUrl)
    getAnswerHtml(html_page)
    time.sleep(1000)










