#encoding:utf-8
import re

#^拖字号，标识以。。。开始
# text = 'hello'
# ret = re.match('^h',text)
# print(ret.group())

# text = 'hello'
# ret = re.search('^h',text)
# print(ret.group())


#在中括号中，表示取反
# text = '1alsdjf123#@'
# ret = re.match('[^a-z]',text)
# print(ret.group())


# $表示以。结尾
# text = 'xxx@163.com'
# ret = re.match(('\w+@163.com$'),text)
# print(ret.group())

# 贪婪模式和非贪婪模式

# +贪婪模式
# text = 'xxx@163.com'
# ret = re.match(('\w+@163.com'),text)
# print(ret.group())
# ？非贪婪模式




text = '<h1>标题</h1>'
ret = re.match(('<.+?>'),text)
print(ret.group())