#coding=utf-8
import urllib
import re
 
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html
 
def getImg(html):
    reg = r'src="(.+?\.jpg)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    x = 0
    for imgurl in imglist:
        strinfo = re.compile('thumb')
        imgurl = strinfo.sub('large',imgurl)
       	print imgurl
        urllib.urlretrieve(imgurl,'%s.jpg' % x)
        x+=1

html = getHtml("http://www.douban.com/photos/album/82457678/")
 
print getImg(html)