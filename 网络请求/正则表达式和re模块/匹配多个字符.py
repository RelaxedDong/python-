
import re
#*：可以匹配0或者任意多个字符。示例代码如下：
# text = "0731x"
# ret = re.match('\d*',text)
# print(ret.group())

# +：可以匹配1个或者多个字符。最少一个。示例代码如下：
#
# text = "abc123LK_584"
# ret = re.match('\w+',text)
# print(ret.group())

# ?：匹配的字符可以出现一次或者不出现（0或者1）。示例代码如下：

# text = "1a223"
# ret = re.match('\d?',text)
# print(ret.group())

# {m}：匹配m个字符。示例代码如下：

# text = "123"
# ret = re.match('\d{5}',text)
# print(ret.group())
#
#
# {m,n}：匹配m-n个字符。在这中间的字符都可以匹配到。示例代码如下：
#
#  text = "123"
#  ret = re.match('\d{1,2}',text)
#  prit(ret.group())


# ^（脱字号）：表示以...开始
# 如果是在中括号中，那么代表的是取反操作.
# text = "hello"
# ret = re.match('[^x]+',text)
# print(ret.group())


# $：表示以...结束：

# 匹配163.com的邮箱
# text = "zxxx@163.com"
# res = re.search('\w+@163.com$',text)
# print(res.group())

# |：匹配多个表达式或者字符串：

# text = "sdfsdf|hello|world"
# ret = re.search('l',text)
# print(ret.group())
'''

贪婪模式和非贪婪模式：

贪婪模式：正则表达式会匹配尽量多的字符。默认是贪婪模式。
非贪婪模式：正则表达式会尽量少的匹配字符。'''

# text = "0123456"
# ret = re.match('\d+',text)
# print(ret.group())
# 因为默认采用贪婪模式，所以会输出0123456

# 可以改成非贪婪模式，那么就只会匹配到0。示例代码如下：

# text = "2123456"
# ret = re.match('\d+?',text)
# # print(ret.group())
# text = '<h1>哈哈</h1>'
# ret = re.search('<.+>',text)
# print(ret.group())

#匹配0-100数字
number = '1000'
ret = re.match('[1-9]\d?$|100$',number)
print(ret.group())
