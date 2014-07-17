#coding=utf-8
import urllib
import re
import datetime
import time
 
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html
 
def getImg(html):
    reg = r'src="(.+thumb.+\.jpg)"'
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
    getImg(html)