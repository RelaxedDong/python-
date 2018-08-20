import re

# text = 'apple is $50084 haha'
# ret = re.search('\$\d+',text)
# print(ret.group())

#在正则表达式中，\n是专门用来转义的。python中\也是用来做转义的。因此要匹配str中的\，要匹配一个\ 要用四个\\\\
text = r'\c'
ret = re.search('\\\\c',text)
print(ret.group())

tex1 = r'\c'
ret = re.search(r'\\c',tex1)
print(ret.group())