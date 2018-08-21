#encoding:utf-8
import json

# python对象转换成json字符串

peoples = [
    {
        'username':'董豪',
        'age':18
    },
    {
        'username':'多对多',
        'age':20
    }
]

# peoples_json = json.dumps(peoples)
# print(peoples_json)
# print(type(peoples_json))

with open('person.json','w',encoding='utf-8') as fp:
    # fp.write(peoples_json)
    #直接将python对象转换成json字符串，并写入文件中
    json.dump(peoples,fp,ensure_ascii=False)






