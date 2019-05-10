#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2019/5/7 14:06
# @Author : mingfei.net@gmail.com
# @FileName : collections_test.py
# @GitHub : https://github.com/thu/python-0426

from collections import namedtuple, deque, defaultdict, OrderedDict, Counter

Point = namedtuple('Point', ['x', 'y'])

p = Point(1, 2)

print(p.x)

print(p.y)

print(isinstance(p, Point))
print(isinstance(p, tuple))

print(type(p))

print(p._asdict())

q = deque([1, 2, 3])

print(q.pop())

print(q.popleft())

print(q)

q.appendleft(1)

q.append(3)

print(q)


def na():
    return 'N/A'  # N/G


d = defaultdict(na)

d['key'] = 'value'

print(d['key'])

print(d['k'])

d = dict([(1, 'x'), (2, 'y'), (3, 'z')])
print(d)

d = OrderedDict([(1, 'x'), (2, 'y'), (3, 'z')])
print(d)

d[-1] = 'a'
d[-2] = 'b'
d[-3] = 'c'

print(d)

counter = Counter()

for c in 'programming':
    counter[c] += 1

print(counter)

words = ['hello', 'world', 'nice', 'world']

counter = defaultdict(lambda : 0)

for word in words:
    counter[word] += 1

print(counter)

