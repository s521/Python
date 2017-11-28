import urllib
import urllib2
import re


user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
x = 0
for i in range (1,200):
    url = 'http://www.005.tv/Cosplay/Cosplay/list_631_'+str(i)+'.html'
    try:
        request = urllib2.Request(url, headers=headers)
        response = urllib2.urlopen(request)
        html = response.read()
    except urllib2.URLError, e:
        if hasattr(e,"code"):
            print e.code
        if hasattr(e,"reason"):
            print e.reason

    content_pattern = re.compile('<a href=".*?" class="img fl xs-100" target="_blank">.*?<img src="(.*?)"/>', re.S)
    content_list = re.findall(content_pattern, html)
    for item in content_list:
        print item
        
        '''  图片爬取'''   
    for imgurl in content_list:
        urllib.urlretrieve(imgurl,'D:\E\%s.jpg' % x)
        x+=1

        '''  爬取图片保存到本地D盘E文件夹下 '''        
    z = raw_input()
    if z == "":
        print "下一页"
        continue
    else:
        print "结束"
        break
'''  回车继续爬取下一页，否则任意键结束  '''
