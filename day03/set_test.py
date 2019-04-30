keys = {'name', 'age', 'married', 'age'}
# keys = {'name', 'age', 'married', 'age'}

print(keys)

keys.add('test_key')

print(keys)

keys.remove('test_key')

print(keys)

keys.pop()

print(keys)

names1 = {'Tom', 'Jerry'}
names2 = {'Jerry', 'Spike'}

# names1.difference_update(names2)
#
# print(names1)
# names3 = names1.difference(names2)
# print(names3)
#
# print(names1)

# names3 = names1.intersection(names2)
#
# print(names3)

print(names1.isdisjoint(names2))

print(names1.issubset(names2))
print(names1.issuperset(names2))

print(names1.symmetric_difference(names2))


print(names1.union(names2))

print(names1 & names2)
print(names1 | names2)

for key in names1| names2:
    print(key)

# list / tuple / dict / set
# 类型转换？
