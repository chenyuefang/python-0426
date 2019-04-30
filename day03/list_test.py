names = ['Tom', 'Jerry']

print(names)

print(names[0])

print(names[-1])  # last element
print(names[-2])

print(len(names))

names.append('spike')

print(names)

names.insert(2, 'Tyke')

print(names)

names[3] = 'Spike'

print(names)

names.pop()

print(names)

names.pop(0)

print(names)

superstars = ['Tom', 'Jerry']
names = [superstars, 'Spike']

names.clear()

print(names)

names = superstars.copy()

print(names)

print(superstars == names)

names.append('Tom')
print(names.count('Tom'))


superstars = ['Tom', 'Jerry']
names = ['Spike', 'Tyke']

superstars.extend(names)
print(superstars)

print(superstars.index('Jerry'))

names.append('Spike')

print(names)

names.remove('Spike')

print(names)

names.reverse()

print(names)

names.sort(reverse=True)

print(names)

for name in names:
    print(name)
