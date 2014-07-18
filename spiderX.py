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


def getPicHtml(html):
    reg = r'href="(http://www.douban.com/photos/photo.+\/)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    for imgurl in imglist:
        newHtml = getHtml(imgurl)
        getImg(newHtml)

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html
 
def getImg(imgurl):
    reg = r'src="(.+public.+\.jpg)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    for imgurl in imglist:
        strinfo = re.compile('thumb')
        imgurl = strinfo.sub('photo',imgurl)
        x = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))+str(datetime.datetime.now().microsecond)
        local = 'E://myimage//'
        urllib.urlretrieve(imgurl,local+'%s.jpg' % x)

albumId = raw_input('please enter the albumId: ')
paper = int(raw_input('please enter the num of paper: '))
for x in range(paper):
    index = str(x * 18)
    albumUrl = "http://www.douban.com/photos/album/"+albumId+"/?start="+index
    html = getHtml(albumUrl)
    getPicHtml(html);
