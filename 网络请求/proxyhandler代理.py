#encoding:utf-8

from urllib import request


# 没有使用代理

# resp1 = request.urlopen('http://httpbin.org/get')
# print(resp1.read())


#使用代理
url = 'http://httpbin.org/get'
handler = request.ProxyHandler({'https':'123.133.192.219:9000'})
opener = request.build_opener(handler)

req = request.Request(url)

resp = opener.open(req)
print(resp.read())

