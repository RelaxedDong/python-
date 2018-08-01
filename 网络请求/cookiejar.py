#encoding:utf-8

# http.cookiejar模块：
'''
1.CookieJar：管理HTTP cookie值、存储HTTP请求生成的cookie、向传出的HTTP请求添加cookie的对象。
整个cookie都存储在内存中，对CookieJar实例进行垃圾回收后cookie也将丢失。

2.FileCookieJar (filename,delayload=None,policy=None)：从CookieJar派生而来，用来创建FileCookieJar实例，
检索cookie信息并将cookie存储到文件中。filename是存储cookie的文件名。delayload为True时支持延迟访问访问文件，
即只有在需要时才读取文件或在文件中存储数据。

3.MozillaCookieJar (filename,delayload=None,policy=None)：从FileCookieJar派生而来，
创建与Mozilla浏览器 cookies.txt兼容的FileCookieJar实例。

4.LWPCookieJar (filename,delayload=None,policy=None)：从FileCookieJar派生而来，创建与libwww-perl标准的 Set-Cookie3 文件格式兼容的FileCookieJar实例。'''

from http.cookiejar import CookieJar
from urllib import request,parse


headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36',
}

def GetOpener():
    jar = CookieJar()
    handler = request.HTTPCookieProcessor(jar)
    opener = request.build_opener(handler)
    return opener

def login(opener):
    data = {
        'email':'x',
        'password':'x'
    }
    data = parse.urlencode(data).encode('utf-8')
    login_url = 'http://www.renren.com/PLogin.do'
    req = request.Request(url=login_url,data=data,headers=headers)
    opener.open(req)

def profile(opener):
    pro_url = 'http://www.renren.com/880151247/profile'

    req = request.Request(url=pro_url,headers=headers)
    resp = opener.open(req)
    with open('自动登录.html','w',encoding='utf-8') as fp:
        fp.write(resp.read().decode('utf-8'))


if __name__ == '__main__':
    opener = GetOpener()
    login(opener)
    profile(opener)

