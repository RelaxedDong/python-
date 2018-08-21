#encoding:utf-8

import json


# persons = '[{"username": "董豪", "age": 18}, {"username": "多对多", "age": 20}]'
# py_str = json.loads(persons)
# print(py_str)

with open('person.json','r',encoding='utf-8') as fp:
    persons = json.load(fp)
    print(persons)
    print(type(persons))