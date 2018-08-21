#encoding:utf-8
import pymysql

cnn = pymysql.connect('localhost','root','root','pymysql_demo',3306)
cursor = cnn.cursor()
# cursor.execute("select 1")
# data = cursor.fetchone()
# print(data)
# cnn.close()



#插入数据
# # 第一种：
#
# #insert into person (id,username,age) value(1,'donghao',20)
#
# text = '''
#     insert into person value(NULL,'donghao1',20)
# '''
# cursor.execute(text)
#
# cnn.commit()
# cnn.close()

# 第二种：

#insert into person (id,username,age) value(1,'donghao',20)

text = '''
    insert into person value(NULL,%s,%s)
'''

username = 'tanyajuan'
age = 20

cursor.execute(text,args=(username,age))

cnn.commit()
cnn.close()
