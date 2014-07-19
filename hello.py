# -*- coding:utf-8 -*-
import re

def getIndex(html):
    reg_index = r'<span class="count">\((.+)\)</span>'
    indexre = re.compile(reg_index)
    indexlist = re.findall(indexre,html)
    indexnum = indexlist[0]
    num = filter(str.isdigit,indexnum)
    return num
    

html = "<span class=\"count\">(共52张)</span></div></div><div class=\"aside\">"
html = unicode(html, "utf8").encode("gbk")
index = int(getIndex(html))
for x in range(1,index):#1-51
    print x