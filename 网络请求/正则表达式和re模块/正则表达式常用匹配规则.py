#encoding:utf-8
import re
# 匹配某个字符串：
# text = 'hello'
# res = re.match('re',text)
# print(res.group())
#
# 点（.）匹配任意的字符：
# 但是点（.）不能匹配不到换行符
# text = "ab"
# ret = re.match('.',text)
# print(ret.group())

# \d匹配任意的数字：
# text = "123"
# ret = re.match('\d',text)
# print(ret.group())


# \D匹配任意的非数字：
#
# text = "a"
# ret = re.match('\D',text)
# print(ret.group())
# >> a
#
# 而如果text是等于一个数字，那么就匹配不成功了。示例代码如下：
#
# text = "1"
# ret = re.match('\D',text)
# print(ret.group())
# >> AttributeError: 'NoneType' object has no attribute 'group'


# \s匹配的是空白字符（包括：\n，\t，\r和空格）：
#
# text = "\t"
# ret = re.match('\s',text)
# print(ret.group())
# >> 空白
#
# \w匹配的是a-z和A-Z以及数字和下划线：
#
# text = "_"
# ret = re.match('\w',text)
# print(ret.group())
# >> _
#
# 而如果要匹配一个其他的字符，那么就匹配不到。示例代码如下：
#
# text = "+"
# ret = re.match('\w',text)
# print(ret.group())
# >> AttributeError: 'NoneType' object has no attribute
#
# \W匹配的是和\w相反的：
#
# text = "+"
# ret = re.match('\W',text)
# print(ret.group())
# >> +
#
# 而如果你的text是一个下划线或者英文字符，那么就匹配不到了。示例代码如下：
#
# text = "_"
# ret = re.match('\W',text)
# print(ret.group())
# >> AttributeError: 'NoneType' object has no attribute


'''[]组合的方式，只要满足中括号中的某一项都算匹配成功：'''
text = '0731-154-88888888'
ret = re.match('[\d\-]+',text)
print(ret.group())

'''之前讲到的几种匹配规则，其实可以使用中括号的形式来进行替代：

    \d：[0-9]
    \D：0-9
    \w：[0-9a-zA-Z_]
    \W：[^0-9a-zA-Z_]
'''

