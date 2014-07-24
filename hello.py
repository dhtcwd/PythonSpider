# -*- coding:utf-8 -*-
import re

def getIndex(html):
    reg_index = r'<span>...</span><span><a href=.*>(.+)</a></span>'
    indexre = re.compile(reg_index)
    indexlist = re.findall(indexre,html)
    indexnum = indexlist[0]
    num = filter(str.isdigit,indexnum)
    return num
    

html = "<span>...</span><span><a href='?page=7'>7</a></span>"
html = unicode(html, "utf8").encode("gbk")
index = int(getIndex(html))
print index 