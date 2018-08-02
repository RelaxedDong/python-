import requests

# resp = requests.get('http://www.baidu.com')
#
# header = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
# }
# # print(resp.text)
# # print(type(resp.text))
# #
# # print(type(resp.content))
# # print(resp.content.decode('utf-8'))
# kw = {'wd':'中国'}
#
# resp1 = requests.get('http://www.baidu.com/s',params=kw,headers = header)
# with open('baidu中国.html','w',encoding='utf-8') as fp:
#     fp.write(resp1.content.decode('utf-8'))
#
# print(resp1.url)
# print(resp1.encoding)
# print(resp1.status_code)



'''POST请求'''

url = "https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false"

data = {
'first':'true',
'pn': '1',
'kd': 'python',
}

headers = {
'Referer':'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
}


resp = requests.post(url=url,data=data,headers=headers)
# print(resp.text)
print(type(resp.text))
# print(resp.content.decode('utf-8'))
# print(type(resp.content))
# print(resp.json())
print(type(resp))