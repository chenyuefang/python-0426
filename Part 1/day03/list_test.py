names = ['Tom', 'Jerry']   # 声明

print(names)  #  访问元素

print(names[0])

print(names[-1])  # last element
print(names[-2])

print(len(names))  #  列表长度

names.append('spike')   #  追加元素

print(names)

names.insert(2, 'Tyke')   # 插入元素

print(names)

names[3] = 'Spike'  #  替换元素

print(names)

names.pop()   #  删除列尾的元素

print(names)

names.pop(0)  #  删除第一个元素

print(names)

superstars = ['Tom', 'Jerry']
names = [superstars, 'Spike']   #  嵌套

names.clear()  #  清空列表

print(names)

names = superstars.copy()

print(names)

print(superstars == names)  #  拷贝

names.append('Tom')
print(names.count('Tom')) #  元素统计


superstars = ['Tom', 'Jerry']
names = ['Spike', 'Tyke']

superstars.extend(names)  #  扩展
print(superstars)

print(superstars.index('Jerry'))  #  返回元素索引

names.append('Spike')

print(names)

names.remove('Spike')  # 删除第一个指定元素

print(names)

names.reverse()  #  逆序

print(names)

names.sort(reverse=True)  #  排序

print(names)

for name in names:   #  迭代
    print(name)
