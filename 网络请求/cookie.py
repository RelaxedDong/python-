#encoding:utf-8
'''cookie的格式：
Set-Cookie: NAME=VALUE；Expires/Max-age=DATE；Path=PATH；Domain=DOMAIN_NAME；SECURE
参数意义：

NAME：cookie的名字。
VALUE：cookie的值。
Expires：cookie的过期时间。
Path：cookie作用的路径。
Domain：cookie作用的域名。
SECURE：是否只在https协议下起作用。'''

'''使用cookie模拟登录'''
'''使用cookielib库和HTTPCookieProcessor模拟登录：'''
from urllib import request,parse

#不使用cookie访问一个用户界面
# url = 'http://www.renren.com/967227953/profile'
#
# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
# }
# req = request.Request(url=url,headers=headers)
#
# resp = request.urlopen(req)
# with open('人人网1.html','w') as f:
#     # write方法必须写一个str类型
#     # resp.read()是一个bytes类型
#     # str->decode()->bytes
#     f.write(resp.read().decode('utf-8'))

# 使用cookie访问用户界面


url = 'http://www.renren.com/967227953/profile'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36',
    'Cookie':'anonymid=jkaurz98o0l976; depovince=GW; _r01_=1; ick_login=e97495c3-e86e-42cd-8927-3e2d0c13a2f1; t=198bfc8569890355c567820a357c0c432; societyguester=198bfc8569890355c567820a357c0c432; id=967227952; xnsid=b740c70; jebecookies=95f96371-8aa1-4d97-9529-7b6a2c7fb540|||||; ver=7.0; loginfrom=null; jebe_key=93c93b5e-f3fc-4086-884f-0034605a117c%7C891a64ffcd8d086cd0ad91191e8280c0%7C1533111175889%7C1%7C1533111102456; wp_fold=0; XNESSESSIONID=abcr4UoH_zjqoafltJ0tw'
}
req = request.Request(url=url,headers=headers)

resp = request.urlopen(req)
with open('人人网cookie.html','w',encoding='utf-8') as f:
    f.write(resp.read().decode('utf-8'))







