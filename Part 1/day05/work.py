# 1
import string

a = str(input())


def fn_str(a):
    while a in string.ascii_letters:
        if a in string.ascii_uppercase:
            n: int = 0
            print('ascii_uppercase')
            n += n
            print(n)
        elif a in string.ascii_lowercase:
            m: int = 0
            print('ascii_lowercase')
            m += m
            print(m)
    return -1


# 2

li = [1, 2, 3, 4, 5, 1, 2, 3]

li = list(set(li))

print(li)


# 3.


def fn_fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fn_fibonacci(n - 1) + fn_fibonacci(n - 2)


print(fn_fibonacci(10))


#  4


def move(n, a, b, c):
    if n == 1:
        print(a, '-', c)
    else:
        print(n)
        move(n - 1, a, c, b)
        print(a, '-', c)
        move(n - 1, b, a, c)


move(3, 'A', 'B', 'C')

#  5


yanghui = []

for i in range(1, 11):
    if i == 1:
        list0 = [1]
    elif i == 2:
        list0 = [1, 1]
    else:
        list0 = [1] * i
        for j in range(1, i - 1):
            list0[j] = yanghui[-1][j - 1] + yanghui[-1][j]
    yanghui.append(list0)

for i in yanghui:
    print(i)
