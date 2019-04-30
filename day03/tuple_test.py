names = ('Tom', 'Jerry')

print(names)

numbers = (1,)

print(numbers)  # (1)

print(names[-1])

# print(numbers[1])

print(2 not in numbers)

print(len(names))

names = tuple(('test', 'test'))

print(names)

print(names.count('test'))

print(names.index('test'))

superstars = ['Tom', 'Jerry']
names = (superstars, 'Spike')

print(names)

names[0].append('Tester')

print(names)

for name in names:
    print(name)

