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
        local = 'E://myimage//'
        urllib.urlretrieve(imgurl,local+'%s.jpg' % x)
        x+=1

html = getHtml("http://www.douban.com/photos/album/63888587/")
 
print getImg(html)