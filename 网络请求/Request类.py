#encoding:utf-8
from urllib import request,parse
'''
如果想要在请求的时候增加一些请求头，那么就必须使用request.Request类来实现。比如要增加一个User-Agent'''


'''
爬取拉勾网职位信息'''
url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36',
    'Referer':'https://www.lagou.com/jobs/list_python?px=default&city=%E5%8C%97%E4%BA%AC'
}
data = {
    'first':'true',
    'kd':'python',
    'pn':1
}
req = request.Request(url=url,headers=headers,data=parse.urlencode(data).encode('utf-8'),method='POST')
res = request.urlopen(req)

request.urlretrieve(url,'人人网.html')
# print(res.read().decode('utf-8'))
