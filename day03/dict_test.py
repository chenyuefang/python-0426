
d = {'name': 'Tom', 'age': 19, 'gender': 'male', 'isMarried': False}  # 声明

print(d)

print(d['name'])

d = {}

d = dict(key=123)  # 声明

d['test_key'] = False

d = {}.fromkeys(['name', 'age'])
d = {}.fromkeys(['name', 'age'], 'value')  # ?  初始化

print(d)

# print(d['name1'])
print(d.get('name1', 'default value'))  # 获取键对应的值


# 更新
d = {'key': 'value'}

d['key'] = 'new value'

d['new_key'] = 'new value1'
d['new_key'] = 'new value2'

print(d)

del d['new_key']

print(d)

# d.pop('key')

print(d)

# del d

# print(d)

d_new = d.copy()

print(d_new)

d = {'name': 'Tom', 'age': 18, 'married': False}

print(d)

for key in d.keys():
    print(key, d[key])
#
# for value in d.values():
#     print(value)
#
# for k, v in d.items():
#     print(k, v)
#
# list1 = ['test']
# d = {list1: 'value'}
#
# print(d)

# 迭代
import collections

d = collections.OrderedDict()

d = {'k1': 'v1', 'k2': 'v2'}

for key in d:
    print(key, d[key])