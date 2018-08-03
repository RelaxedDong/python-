#encoding:utf-8
import requests

'''cookie'''

# resp = requests.get('http://www.baidu.com')
#
# print(resp.cookies)
# print(resp.cookies.get_dict())



'''访问大鹏主页'''

login_url = 'http://www.renren.com/PLogin.do'
profile_url = 'http://www.renren.com/880151248/profile'
data = {
    'email': '17625567763',
    'password': 'isolate36'
}

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36',
}

session = requests.session()

session.post(url=login_url,data=data,headers=headers)

resp = session.get(url=profile_url,headers=headers)
with open('renren.html','w',encoding='utf-8') as fp:
    fp.write(resp.text)


'''处理不信任ssl证书'''
resp = requests.get('http://www.12306.cn/mormhweb/',verify=False)
print(resp.content.decode('utf-8'))