names = ('Tom', 'Jerry')

print(names)

numbers = (1,)

print(numbers)  # (1)  声明

print(names[-1])  # 访问元素

# print(numbers[1])

print(2 not in numbers)  # 判断元素是否存在

print(len(names))  # 元祖长度

names = tuple(('test', 'test'))   # 元祖构造器

print(names)

print(names.count('test'))  # 元素统计

print(names.index('test'))  # 返回元素索引

superstars = ['Tom', 'Jerry']
names = (superstars, 'Spike')

print(names)

names[0].append('Tester')  #  不可变的理解

print(names)

for name in names:   # 迭代
    print(name)

