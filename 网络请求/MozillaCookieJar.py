from http.cookiejar import MozillaCookieJar
from urllib import request


mozila = MozillaCookieJar('cookie.txt')

handler = request.HTTPCookieProcessor(mozila)

opener = request.build_opener(handler)

url = 'http://www.httpbin.org/cookies/set?username=donghao'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
}
req = request.Request(url=url,headers=headers)

resp = opener.open(req)
print(resp.read())
mozila.load(ignore_discard=True)

for cookie in mozila:
    print(cookie)
# mozila.save(ignore_discard=True,ignore_expires=True)

#ignore_discard把即将过期的cookie信息保存

