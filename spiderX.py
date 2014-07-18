# -*- coding=utf-8 -*-

#---------------------------------------  
#   程序：豆瓣相册爬虫
#   版本：0.2  
#   作者：Will  
#   日期：2014-07-17  
#   语言：Python 2.7  
#   功能：将相册中照片全部抓下来（有大图优先抓大图——比0.1版本的改进)  
#---------------------------------------  

import urllib
import re
import datetime
import time
import urllib2  
import random
import cookielib


def getPicHtml(html):
    reg = r'href="(http://www.douban.com/photos/photo.+\/)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    for imgurl in imglist:
        print "Now downloadPage is %r" % imgurl
        newHtml = getHtml(imgurl)
        getImg(newHtml)

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


def getImg(html):
    
    reg = r'src="(.+photo\/photo\/public.+\.jpg)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    for imgurl in imglist:
        reg_large = r'<a href="http://www.douban.com.+large'
        largere = re.compile(reg_large)
        largelist = re.findall(largere,html)
        if len(largelist)>0:
            print len(largelist)
            print "There's a large version..."
            strinfo = re.compile('photo/photo')
            imgurl = strinfo.sub('photo/large',imgurl)
        print "picture url is %s" % imgurl
        x = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))+str(datetime.datetime.now().microsecond)
        local = 'E://myimage//'
        urllib.urlretrieve(imgurl,local+'%s.jpg' % x)
        # in order to avid being 403
        # hava another try latter
        time.sleep(random.randint(0, 5))



albumId = raw_input('please enter the albumId: ')
paper = int(raw_input('please enter the num of paper: '))
for x in range(paper):
    index = str(x * 18)
    albumUrl = "http://www.douban.com/photos/album/"+albumId+"/?start="+index
    print "Now we start at %r" % albumUrl
    html = getHtml(albumUrl)
    getPicHtml(html);
