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
        
        '''  ͼƬ��ȡ'''   
    for imgurl in content_list:
        urllib.urlretrieve(imgurl,'D:\E\%s.jpg' % x)
        x+=1

        '''  ��ȡͼƬ���浽����D��E�ļ����� '''        
    z = raw_input()
    if z == "":
        print "��һҳ"
        continue
    else:
        print "����"
        break
'''  �س�������ȡ��һҳ���������������  '''
