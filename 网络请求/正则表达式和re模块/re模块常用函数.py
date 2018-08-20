# encoding:utf-8
import re

# 分组
# tex1 = 'app is $50 ,orange is $100'
# ret = re.search('.*(\$\d+).*(\$\d+)',tex1)
# print(type(ret.group()))
# # print(ret.group(0))
# # print(ret.group(1))
# # print(ret.group(2))
# # print(ret.group(0,1,2))
# #所有子分组拿出来
# print(ret.groups())

# findall()找出所有满足条件的，返回一个列表
# tex1 = 'app is $50 ,orange is $100'
# ret = re.findall('\$\d+',tex1)
# print(ret)


# sub函数
# 替换
# tex1 = 'app is $50 ,orange is $100'
# ret = re.sub('\$\d+',r'\\n$50',tex1)
# print(ret)
# html = '''
# <dd class="job_bt">
#         <h3 class="description">职位描述：</h3>
#         <div>
#         <p>一、岗位职责</p>
# <p>1. 实现公司整体渠道招募及运营目标计划</p>
# <p>2. 制定渠道相关营销管理政策</p>
# <p>3. 定期做好渠道招募会议策划和落地</p>
# <p>4. 做好渠道团队的培训和管理工作</p>
# <p>5. 做好领导安排的其他临时工作</p>
# <p>6、根据市场需要出差，负责目标客户的关系拓展。</p>
# <p>二、任职资格</p>
# <p>1.本科以上学历，优秀者可适当放宽条件；市场营销、企业管理、10年以上营销及渠道管理经验；</p>
# <p>2.熟悉IT、网络安全相关知识，政府采购流程；</p>
# <p>3.具有丰富的人脉资源，公关能力强，能接受出差；</p>
# <p>4.较强的渠道开拓，渠道把控能力，擅长会议营销，演讲培训；</p>
# <p>5.良好的敬业精神和职业道德操守，有很强的感召力和凝聚力，责任心、事业心强；</p>
# <p>6.具有良好的工作背景与评价口碑；</p>
# <p>三、薪资福利</p>
# <p>12000底薪+高额提成+奖金</p>
#         </div>
#     </dd>'''
# # re?	匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式
# ret = re.sub('<.*?>',"",html)
# print(ret)


#split函数

#
# text = 'my name$is*dong-hao'
# ret = re.split('[^a-zA-Z]',text)
# print(ret)



#compile函数

# text = 'apple is $5095.6525 haha'
# ret = re.compile('\d+\.?\d*')
# r = ret.search(text)
# print(r.group())

text = 'apple is $5095.123 haha'
ret = re.compile(r'''
                \d+ #前面的数字
                \. #小数点
                \d*#后面的数字
''',re.VERBOSE)
r = ret.search(text)
print(r.group())








