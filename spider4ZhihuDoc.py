# -*- coding:utf-8 -*-

#---------------------------------------  
#   程序：知乎文章爬虫
#   版本：0.1  
#   作者：Will  
#   日期：2014-07-24  
#   语言：Python 2.7  
#   功能：将某个作者的文章全部爬下来并email到evernote
#---------------------------------------  

import smtplib

#邮件发送模块
fromaddr = "" #填写发送email地址
toaddrs  = "" #填写接受email地址
msg = "hello world"
server = smtplib.SMTP('localhost')
server.set_debuglevel(1)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()